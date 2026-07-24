import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const NLM_GATEWAY_DIR = '/Users/yuan/Projects/Notebooklm/NLM_MCQs';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

// Helper to strip `- 原檔` suffix
export function cleanPaperTitle(rawName) {
  return rawName.replace(/\s*-\s*原檔$/i, '').trim();
}

// Parse markdown file into questions array
export function parseExamMarkdown(mdContent, paperTitle) {
  const questions = [];
  // Split by Question markers (題號 or 題目 with optional whitespace and full/half-width colons)
  const blocks = mdContent.split(/(?=題號\s*[:：]|題目\s*[:：]|\bQuestion\s+\d+[:：]?)/i);

  let qCount = 0;
  for (const block of blocks) {
    if (!block.trim() || !/題目\s*[:：]/i.test(block)) continue;
    qCount++;

    const numMatch = block.match(/題號\s*[:：]\s*_*([0-9]+)/i) || block.match(/Question\s+([0-9]+)/i);
    const qNum = numMatch ? parseInt(numMatch[1], 10) : qCount;

    // Extract Stem
    let stem = '';
    const stemMatch = block.match(/題目\s*[:：]\s*\n?([\s\S]*?)(?=答案\s*[:：]|\([A-Ea-e]\)|\([a-e]\)|正確答案\s*[:：]|$)/i);
    if (stemMatch) {
      stem = stemMatch[1].trim();
    }

    // Extract Options
    const options = [];
    const optRegex = /\(([A-Ea-e])\)\s*([\s\S]*?)(?=\([A-Ea-e]\)|正確答案\s*[:：]|出題原則|難易程度|$)/gi;
    let m;
    while ((m = optRegex.exec(block)) !== null) {
      const optId = m[1].toUpperCase();
      const optText = m[2].trim().replace(/\n+/g, ' ');
      if (!options.some((o) => o.id === optId)) {
        options.push({ id: optId, text: optText });
      }
    }

    // Extract Ground Truth Answer
    let sourceAnswerStatus = 'absent';
    let sourceProvidedAnswer = null;
    const ansMatch = block.match(/正確答案\s*[:：]\s*\(\s*([A-Ea-e])\s*\)/i) || block.match(/答案\s*[:：]\s*\(\s*([A-Ea-e])\s*\)/i);
    if (ansMatch) {
      sourceAnswerStatus = 'provided';
      sourceProvidedAnswer = ansMatch[1].toUpperCase();
    }

    if (stem && options.length > 0) {
      questions.push({
        id: `${paperTitle.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5]/g, '_')}_q${qNum}`,
        number: qNum,
        stem,
        options,
        sourceAnswerStatus,
        sourceProvidedAnswer,
        nlmResponses: [],
        reconciliationStatus: sourceProvidedAnswer ? 'UNVERIFIED' : 'UNVERIFIED',
        reconciliationNotes: '',
        resolvedImages: [],
      });
    }
  }

  return questions;
}


// Prepare 2x NLM asking JSON payload
export function buildDualNlmPayload(questions) {
  const payloadQuestions = [];
  for (const q of questions) {
    const optsObj = {};
    q.options.forEach((o) => {
      optsObj[o.id] = o.text;
    });

    // Run 1
    payloadQuestions.push({
      q_id: `${q.id}_run1`,
      question_text: q.stem,
      options: optsObj,
    });
    // Run 2
    payloadQuestions.push({
      q_id: `${q.id}_run2`,
      question_text: q.stem,
      options: optsObj,
    });
  }
  return { questions: payloadQuestions };
}

// Perform Reconciliation
export function reconcileResponses(sourceAnswer, nlmList) {
  const nlmAnswers = nlmList.map((r) => r.selectedOption).filter(Boolean);

  if (nlmAnswers.length === 0) {
    return {
      status: 'INSUFFICIENT_EVIDENCE',
      notes: 'NotebookLM 檢索無有效回應。',
    };
  }

  const nlmAgreed = nlmAnswers.every((ans) => ans === nlmAnswers[0]);
  const nlmPrimaryAns = nlmAnswers[0];

  if (sourceAnswer) {
    if (nlmAgreed && nlmPrimaryAns === sourceAnswer) {
      return {
        status: 'HIGH_CONFIDENCE',
        notes: `原始答案 (${sourceAnswer}) 與兩組 NotebookLM 檢索結果完全一致。`,
      };
    } else if (nlmAgreed && nlmPrimaryAns !== sourceAnswer) {
      return {
        status: 'DISPUTED_SOURCE_VS_NLM',
        notes: `有爭議：原始答案給予 (${sourceAnswer})，但 NotebookLM 推論為 (${nlmPrimaryAns})。`,
      };
    } else {
      return {
        status: 'DISPUTED_NLM_VS_NLM',
        notes: `有爭議：NotebookLM 兩次提問回答不一致 (${nlmAnswers.join(' vs ')})，原始答案為 (${sourceAnswer})。`,
      };
    }
  } else {
    if (nlmAgreed) {
      return {
        status: 'HIGH_CONFIDENCE',
        notes: `原始檔案無解答，兩組 NotebookLM 一致推論答案為 (${nlmPrimaryAns})。`,
      };
    } else {
      return {
        status: 'DISPUTED_NLM_VS_NLM',
        notes: `原始檔案無解答，兩組 NotebookLM 回答不一致 (${nlmAnswers.join(' vs ')})。`,
      };
    }
  }
}

// Main CLI logic
export async function processDirectories(targetDirs, options = { dryRun: false }) {
  if (!fs.existsSync(SERVER_DATA_DIR)) {
    fs.mkdirSync(SERVER_DATA_DIR, { recursive: true });
  }

  const manifestPath = path.join(SERVER_DATA_DIR, 'exams_manifest.json');
  let manifest = [];
  if (fs.existsSync(manifestPath)) {
    try {
      manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
    } catch (e) {
      manifest = [];
    }
  }

  for (const rawDir of targetDirs) {
    if (!fs.existsSync(rawDir)) {
      console.warn(`[WARN] Target dir does not exist: ${rawDir}`);
      continue;
    }

    const dirName = path.basename(rawDir);
    const paperTitle = cleanPaperTitle(dirName);
    console.log(`Processing Paper: ${paperTitle} (Source: ${dirName})`);

    // Find .md file inside office/ or root
    let mdFile = null;
    function findMd(searchPath) {
      const entries = fs.readdirSync(searchPath, { withFileTypes: true });
      for (const e of entries) {
        const full = path.join(searchPath, e.name);
        if (e.isDirectory()) {
          findMd(full);
        } else if (e.name.endsWith('.md')) {
          mdFile = full;
        }
      }
    }
    findMd(rawDir);

    if (!mdFile) {
      console.warn(`[SKIP] No .md question file found in ${rawDir}`);
      continue;
    }

    console.log(`Reading Markdown: ${mdFile}`);
    const mdContent = fs.readFileSync(mdFile, 'utf-8');
    const questions = parseExamMarkdown(mdContent, paperTitle);

    console.log(`Found ${questions.length} questions in ${paperTitle}`);
    if (questions.length === 0) continue;

    if (options.dryRun) {
      console.log(`[DRY RUN] Would process ${questions.length} questions for ${paperTitle}`);
      continue;
    }

    // Call NLM Gateway via uv run
    const tmpInputJson = path.join(process.cwd(), 'tmp_nlm_input.json');
    const tmpOutputJson = path.join(process.cwd(), 'tmp_nlm_output.json');

    const dualPayload = buildDualNlmPayload(questions);
    fs.writeFileSync(tmpInputJson, JSON.stringify(dualPayload, null, 2), 'utf-8');

    console.log(`Executing NLM Dual Asking Gateway for ${dualPayload.questions.length} question instances...`);
    try {
      const cmd = `uv run --directory "${NLM_GATEWAY_DIR}" python -m MCQ_manufacturer.nlm_asking_gateway --input-json "${tmpInputJson}" --output-json "${tmpOutputJson}"`;
      execSync(cmd, { stdio: 'inherit' });

      if (fs.existsSync(tmpOutputJson)) {
        const nlmResults = JSON.parse(fs.readFileSync(tmpOutputJson, 'utf-8'));
        // Group results back by base q.id
        for (const q of questions) {
          const run1 = nlmResults.find((r) => r.q_id === `${q.id}_run1`);
          const run2 = nlmResults.find((r) => r.q_id === `${q.id}_run2`);

          const resList = [];
          if (run1) {
            const optMatch = run1.raw_response?.match(/(?:Answer|解答|選項)\s*:\s*\(?\s*([A-Ea-e])\s*\)?/i);
            resList.push({
              notebookTitle: run1.notebook_title || 'Notebook #1',
              notebookId: run1.notebook_id || '',
              accountProfile: run1.account_profile || '',
              selectedOption: optMatch ? optMatch[1].toUpperCase() : null,
              rawResponse: run1.raw_response || '',
              citations: [],
              figureMentions: [],
              databaseSufficiency: run1.database_sufficiency || 'SUFFICIENT',
              error: run1.error || null,
            });
          }
          if (run2) {
            const optMatch = run2.raw_response?.match(/(?:Answer|解答|選項)\s*:\s*\(?\s*([A-Ea-e])\s*\)?/i);
            resList.push({
              notebookTitle: run2.notebook_title || 'Notebook #2',
              notebookId: run2.notebook_id || '',
              accountProfile: run2.account_profile || '',
              selectedOption: optMatch ? optMatch[1].toUpperCase() : null,
              rawResponse: run2.raw_response || '',
              citations: [],
              figureMentions: [],
              databaseSufficiency: run2.database_sufficiency || 'SUFFICIENT',
              error: run2.error || null,
            });
          }

          q.nlmResponses = resList;
          const rec = reconcileResponses(q.sourceProvidedAnswer, resList);
          q.reconciliationStatus = rec.status;
          q.reconciliationNotes = rec.notes;
        }
      }
    } catch (err) {
      console.warn(`[WARN] NLM Gateway execution skipped or failed: ${err.message}`);
    } finally {
      if (fs.existsSync(tmpInputJson)) fs.unlinkSync(tmpInputJson);
      if (fs.existsSync(tmpOutputJson)) fs.unlinkSync(tmpOutputJson);
    }

    // Save Paper JSON
    const paperId = paperTitle.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5]/g, '_');
    const paperJsonFile = path.join(SERVER_DATA_DIR, `${paperId}.json`);
    const paperData = {
      id: paperId,
      title: paperTitle,
      rawTitle: dirName,
      sourceCategory: 'Processed Ingestion',
      year: 2025,
      questionCount: questions.length,
      createdAt: new Date().toISOString(),
      questions,
    };

    fs.writeFileSync(paperJsonFile, JSON.stringify(paperData, null, 2), 'utf-8');
    console.log(`Saved paper dataset: ${paperJsonFile}`);

    // Update Manifest
    manifest = manifest.filter((m) => m.id !== paperId);
    manifest.push({
      id: paperId,
      title: paperTitle,
      sourceCategory: 'Processed Ingestion',
      questionCount: questions.length,
      year: 2025,
    });
  }

  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf-8');
  console.log(`[SUCCESS] Updated Manifest at ${manifestPath}`);
}

// Run if called from CLI directly
if (process.argv[1].endsWith('ingest_exam.mjs')) {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const dirs = args.filter((a) => a !== '--dry-run');
  if (dirs.length > 0) {
    processDirectories(dirs, { dryRun });
  } else {
    console.log('Usage: node scripts/ingest_exam.mjs [--dry-run] <dir1> <dir2> ...');
  }
}

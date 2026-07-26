import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const NLM_GATEWAY_DIR = '/Users/yuan/Projects/Notebooklm/NLM_MCQs';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

// Helper to strip `- 原檔` suffix
export function cleanPaperTitle(rawName) {
  return rawName.replace(/\s*-\s*原檔$/i, '').trim();
}

// DEPRECATED REGEX EXTRACTION: Option extractions MUST be performed via Subagent LLM semantic parsing.
export function extractNlmOption() {
  throw new Error('[AGENTS.md GOVERNANCE VIOLATION] Regex option extraction is strictly banned. NLM selectedOption must be determined by Subagent semantic reading.');
}


// Parse markdown file into questions array
export function parseExamMarkdown(mdContent, paperTitle) {
  const questions = [];

  const bottomAnswers = {};
  const rawLines = mdContent.split('\n');
  
  let bottomTableStartIndex = -1;
  for (let i = rawLines.length - 1; i >= 0; i--) {
    const line = rawLines[i].trim();
    if (!line) continue;
    const m = line.match(/^([0-9]+)\s*[\.\:]?\s*\(?\s*([A-Ea-e])\s*\)?$/);
    if (m) {
      bottomAnswers[parseInt(m[1], 10)] = m[2].toUpperCase();
      bottomTableStartIndex = i;
    } else if (line.includes('答案') || line.toLowerCase().includes('answer key')) {
      bottomTableStartIndex = i;
      break;
    } else if (bottomTableStartIndex !== -1 && i < bottomTableStartIndex - 10) {
      break;
    }
  }

  const lines = bottomTableStartIndex > -1 ? rawLines.slice(0, bottomTableStartIndex) : rawLines;

  let currentChapter = '';
  let currentVignette = '';
  let currentQNum = null;
  let currentStemLines = [];
  let currentOptions = [];
  let currentAnswer = null;
  let currentExplanation = [];
  let inExplanation = false;

  const numToLetter = { '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E' };

  function pushQuestion() {
    if (currentStemLines.length > 0 && currentOptions.length >= 4) {
      let stem = currentStemLines.join('\n').trim();
      if (currentVignette) {
        stem = `${currentVignette}\n\n${stem}`;
      }
      if (currentChapter) {
        stem = `[${currentChapter}] ${stem}`;
      }
      if (currentExplanation.length > 0) {
        const exp = currentExplanation.join('\n').trim();
        if (exp) stem = `${stem}\n\n*Explanation:* ${exp}`;
      }

      const qNum = currentQNum || (questions.length + 1);
      const sourceProvidedAnswer = currentAnswer || bottomAnswers[qNum] || null;

      questions.push({
        id: `${paperTitle.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5]/g, '_')}_q${questions.length + 1}`,
        number: qNum,
        stem,
        options: currentOptions,
        sourceAnswerStatus: sourceProvidedAnswer ? 'provided' : 'absent',
        sourceProvidedAnswer,
        nlmResponses: [],
        reconciliationStatus: 'UNVERIFIED',
        reconciliationNotes: '',
        resolvedImages: [],
        attachedImages: [],
        qcVerified: false,
        qcStatus: 'UNVERIFIED',
        qcVerifiedAt: null,
        qcNotes: '',
      });
    }
    currentQNum = null;
    currentStemLines = [];
    currentOptions = [];
    currentAnswer = null;
    currentExplanation = [];
    inExplanation = false;
  }

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const lineTrim = line.trim();
    if (!lineTrim) continue;

    // Chapter header
    const chapMatch = lineTrim.match(/^Chapter\s+([0-9\+]+)$/i);
    if (chapMatch) {
      pushQuestion();
      currentChapter = lineTrim;
      currentVignette = '';
      continue;
    }

    // Answer line
    const ansMatch = lineTrim.match(/^(?:Answer|Ans|正確答案|答案)\s*[:：]?\s*\(?\s*([A-Ea-e])\s*\)?(.*)$/i);
    if (ansMatch) {
      currentAnswer = ansMatch[1].toUpperCase();
      inExplanation = true;
      if (ansMatch[2] && ansMatch[2].trim()) {
        currentExplanation.push(ansMatch[2].trim());
      }
      continue;
    }

    // Page line
    if (lineTrim.match(/^Page\s*[:：]/i)) {
      continue;
    }

    // Letter option: (A) text or A. text
    const optLetterMatch = lineTrim.match(/^(?:\(([A-Ea-e])\)|([A-Ea-e])[\.\)])\s+(.*)$/);

    // Number option: 1. text, 2. text ... 5. text
    const optNumMatch = lineTrim.match(/^([1-5])[\.\)]\s+(.*)$/);

    // Reset explanation mode if new question or option starts
    if (inExplanation) {
      if (optLetterMatch || lineTrim.match(/^(?:Question\s+[0-9]+|#[0-9]+\b|Quiz\b|[0-9]+\.\s+|Which|What|In|A|Among|The|According|Regarding|This)/i)) {
        pushQuestion();
        inExplanation = false;
      }
    }

    const hasLetterOptions = currentOptions.some(o => ['A','B','C','D','E'].includes(o.id));

    // Numbered Option check:
    const isNumberedOption = !hasLetterOptions && optNumMatch && currentStemLines.length > 0 && !inExplanation && (
      (optNumMatch[1] === '1' && currentOptions.length === 0) ||
      (currentOptions.length > 0 && parseInt(optNumMatch[1], 10) === currentOptions.length + 1)
    );

    // Question header match
    const qHeaderMatch = !isNumberedOption && !optLetterMatch && (
      lineTrim.match(/^(?:Question\s+([0-9]+)|#([0-9]+)\b|題號\s*[:：]\s*([0-9]+))/i) ||
      lineTrim.match(/^([0-9]+)\.\s+(.*)$/)
    );

    if (qHeaderMatch) {
      pushQuestion();
      const num = parseInt(qHeaderMatch[1] || qHeaderMatch[2] || qHeaderMatch[3] || qHeaderMatch[4], 10);
      currentQNum = num;

      let stemText = lineTrim.replace(/^(?:Question\s+[0-9]+|#[0-9]+\b|題號\s*[:：]\s*[0-9]+|[0-9]+\.)\s*/i, '').trim();
      if (stemText) {
        currentStemLines.push(stemText);
      }
      continue;
    }

    // Process Letter option
    if (optLetterMatch) {
      const letter = optLetterMatch[1] || optLetterMatch[2];
      const text = optLetterMatch[3].trim();
      const optId = letter.toUpperCase();

      if (optId === 'A' && (currentOptions.length >= 3 || inExplanation)) {
        pushQuestion();
      }

      currentOptions.push({ id: optId, text });
      inExplanation = false;
      continue;
    }

    // Process Numbered option
    if (isNumberedOption) {
      const num = optNumMatch[1];
      const text = optNumMatch[2].trim();
      const optId = numToLetter[num];

      if (num === '1' && currentOptions.length >= 3) {
        pushQuestion();
      }

      currentOptions.push({ id: optId, text });
      continue;
    }

    if (inExplanation) {
      currentExplanation.push(lineTrim);
      continue;
    }

    if (currentOptions.length >= 5) {
      pushQuestion();
    }

    if (currentStemLines.length > 0 || currentQNum !== null) {
      currentStemLines.push(lineTrim);
    } else if (lineTrim.match(/^(?:Quiz\b|Instructions\b)/i)) {
      continue;
    } else {
      if (lineTrim.match(/^(?:Which|In|A|Among|The|What|According|Regarding|This)\b/i)) {
        currentStemLines.push(lineTrim);
      } else {
        currentVignette = currentVignette ? `${currentVignette}\n${lineTrim}` : lineTrim;
      }
    }
  }

  pushQuestion();

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
  if (!nlmList || nlmList.length < 2) {
    return {
      status: 'INSUFFICIENT_EVIDENCE',
      notes: `NotebookLM 提問次數不足（僅 ${nlmList ? nlmList.length : 0} 次，規範需要 2 次獨立提問）。`,
    };
  }

  const nlmAnswers = nlmList.map((r) => r.selectedOption).filter(Boolean);

  if (nlmAnswers.length === 0) {
    return {
      status: 'INSUFFICIENT_EVIDENCE',
      notes: 'NotebookLM 檢索無有效回應。',
    };
  }

  const nlmAgreed = nlmAnswers.every((ans) => ans === nlmAnswers[0]);
  const nlmPrimaryAns = nlmAnswers[0];
  const joinStr = nlmAnswers.join(' vs ');

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
        notes: `有爭議：NotebookLM 兩次提問回答不一致 (${joinStr})，原始答案為 (${sourceAnswer})。`,
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
        notes: `原始檔案無解答，兩組 NotebookLM 回答不一致 (${joinStr})。`,
      };
    }
  }
}

// Main CLI logic
export async function processDirectories(targetDirs, options = { dryRun: false, force: false }) {
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
    const paperId = paperTitle.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5]/g, '_');
    const paperJsonFile = path.join(SERVER_DATA_DIR, `${paperId}.json`);

    const isAlreadyProcessed = manifest.some((m) => m.id === paperId) || fs.existsSync(paperJsonFile);
    if (isAlreadyProcessed && !options.force) {
      console.log(`[SKIP] Paper "${paperTitle}" (ID: ${paperId}) is already processed. Use --force to re-process.`);
      continue;
    }

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
            const optVal = run1.selectedOption || run1.selected_option || null;
            resList.push({
              notebookTitle: run1.notebook_title || 'Notebook #1',
              notebookId: run1.notebook_id || '',
              accountProfile: run1.account_profile || '',
              selectedOption: optVal,
              rawResponse: run1.raw_response || '',
              citations: [],
              figureMentions: [],
              databaseSufficiency: run1.database_sufficiency || 'SUFFICIENT',
              error: run1.error || null,
            });
          }
          if (run2) {
            const optVal = run2.selectedOption || run2.selected_option || null;
            resList.push({
              notebookTitle: run2.notebook_title || 'Notebook #2',
              notebookId: run2.notebook_id || '',
              accountProfile: run2.account_profile || '',
              selectedOption: optVal,
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
if (process.argv[1] && process.argv[1].endsWith('ingest_exam.mjs')) {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const force = args.includes('--force');
  const dirs = args.filter((a) => a !== '--dry-run' && a !== '--force');
  if (dirs.length > 0) {
    processDirectories(dirs, { dryRun, force });
  } else {
    console.log('Usage: node scripts/ingest_exam.mjs [--dry-run] [--force] <dir1> <dir2> ...');
  }
}

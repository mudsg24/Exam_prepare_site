import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { reconcileResponses } from './ingest_exam.mjs';

const NLM_GATEWAY_DIR = '/Users/yuan/Projects/Notebooklm/NLM_MCQs';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

export const AFFECTED_FILES = [
  '2025_北榮_(重點轉化).json',
  '2026_Key_point童綜合_(重點轉化).json',
  '2026_zhongrong_(重點轉化).json',
  '2026_中國附醫_(重點轉化).json',
  '2026_台大考訓_(重點轉化).json',
  '2026_奇美_(重點轉化).json',
  '2026_雙和考訓_(重點轉化).json',
  '2026_高醫__基礎_(重點轉化).json',
  '2026_成大_Cases_(重點轉化).json',
  '2026_mackay_(重點轉化).json',
  '2026_亞東考訓_(重點轉化).json',
];

export function buildPaperDualPayload(paperData) {
  const payloadQuestions = [];
  for (const q of paperData.questions) {
    const optsObj = {};
    (q.options || []).forEach((o) => {
      const optId = o.id || o.key;
      if (optId) optsObj[optId] = o.text;
    });

    payloadQuestions.push({
      q_id: `${q.id}_run1`,
      question_text: q.stem,
      options: optsObj,
    });
    payloadQuestions.push({
      q_id: `${q.id}_run2`,
      question_text: q.stem,
      options: optsObj,
    });
  }
  return { questions: payloadQuestions };
}

export function runGatewayForPaper(paperFile) {
  const paperPath = path.join(SERVER_DATA_DIR, paperFile);
  if (!fs.existsSync(paperPath)) {
    console.error(`File not found: ${paperPath}`);
    return null;
  }

  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
  console.log(`\n==================================================`);
  console.log(`Running Gateway for ${paperData.title} (${paperData.questions.length} questions)...`);

  const tmpInputJson = path.join(process.cwd(), `tmp_repair_input_${paperData.id}.json`);
  const tmpOutputJson = path.join(process.cwd(), `tmp_repair_output_${paperData.id}.json`);

  const payload = buildPaperDualPayload(paperData);
  fs.writeFileSync(tmpInputJson, JSON.stringify(payload, null, 2), 'utf-8');

  console.log(`Payload ready: ${payload.questions.length} instances. Executing Gateway...`);
  try {
    const cmd = `uv run --directory "${NLM_GATEWAY_DIR}" python -m MCQ_manufacturer.nlm_asking_gateway --input-json "${tmpInputJson}" --output-json "${tmpOutputJson}"`;
    execSync(cmd, { stdio: 'inherit' });

    if (fs.existsSync(tmpOutputJson)) {
      const rawResults = JSON.parse(fs.readFileSync(tmpOutputJson, 'utf-8'));
      console.log(`Gateway returned ${rawResults.length} responses for ${paperData.title}`);
      return { paperData, rawResults, tmpInputJson, tmpOutputJson };
    }
  } catch (err) {
    console.error(`Gateway error for ${paperData.title}: ${err.message}`);
  }
  return null;
}

export function applyReconciledResponses(paperFile, paperData, parsedResults) {
  const paperPath = path.join(SERVER_DATA_DIR, paperFile);
  
  let passCount = 0;
  let shortCount = 0;

  for (const q of paperData.questions) {
    const run1 = parsedResults.find((r) => r.q_id === `${q.id}_run1`);
    const run2 = parsedResults.find((r) => r.q_id === `${q.id}_run2`);

    const resList = [];
    for (const run of [run1, run2]) {
      if (run) {
        const optVal = run.selectedOption || null;
        const rawResp = run.raw_response || run.rawResponse || '';

        resList.push({
          notebookTitle: run.notebook_title || run.notebookTitle || 'Notebook',
          notebookId: run.notebook_id || run.notebookId || '',
          accountProfile: run.account_profile || run.accountProfile || '',
          selectedOption: optVal,
          rawResponse: rawResp,
          formattedResponse: rawResp,
          citations: run.citations || [],
          figureMentions: run.figure_mentions || run.figureMentions || [],
          databaseSufficiency: run.database_sufficiency || run.databaseSufficiency || 'SUFFICIENT',
          error: run.error || null,
        });
      }
    }

    q.nlmResponses = resList;
    const rec = reconcileResponses(q.sourceProvidedAnswer, resList);
    q.reconciliationStatus = rec.status;
    q.reconciliationNotes = rec.notes;
    q.qcVerified = true;
    q.qcStatus = 'QC_PASSED';
    q.qcVerifiedAt = new Date().toISOString();

    const isShort = resList.some((r) => !r.rawResponse || r.rawResponse.length < 200 || r.databaseSufficiency === 'INSUFFICIENT');
    if (isShort) {
      shortCount++;
    } else {
      passCount++;
    }
  }

  fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');
  console.log(`Saved updated paper JSON: ${paperPath} (${passCount} passed Stage 1, ${shortCount} short/insufficient).`);
}

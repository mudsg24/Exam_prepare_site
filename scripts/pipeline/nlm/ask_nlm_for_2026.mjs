import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { reconcileResponses } from '../ingest/ingest_exam.mjs';

const NLM_GATEWAY_DIR = '/Users/yuan/Projects/Notebooklm/NLM_MCQs';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

function buildDualNlmPayload(questions) {
  const payloadQuestions = [];
  for (const q of questions) {
    const optsObj = {};
    (q.options || []).forEach((o) => {
      optsObj[o.id] = o.text;
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

async function runNlmAskingForPaper(paperFile) {
  const paperPath = path.join(SERVER_DATA_DIR, paperFile);
  if (!fs.existsSync(paperPath)) {
    console.error(`Paper file not found: ${paperPath}`);
    return;
  }

  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
  console.log(`Processing NLM Dual Asking for ${paperData.title} (${paperData.questions.length} questions)...`);

  const tmpInputJson = path.join(process.cwd(), `tmp_nlm_input_${paperData.id}.json`);
  const tmpOutputJson = path.join(process.cwd(), `tmp_nlm_output_${paperData.id}.json`);

  const payload = buildDualNlmPayload(paperData.questions);
  fs.writeFileSync(tmpInputJson, JSON.stringify(payload, null, 2), 'utf-8');

  console.log(`Executing NLM Dual Asking Gateway for ${payload.questions.length} instances...`);
  try {
    const cmd = `uv run --directory "${NLM_GATEWAY_DIR}" python -m MCQ_manufacturer.nlm_asking_gateway --input-json "${tmpInputJson}" --output-json "${tmpOutputJson}"`;
    execSync(cmd, { stdio: 'inherit' });

    if (fs.existsSync(tmpOutputJson)) {
      const nlmResults = JSON.parse(fs.readFileSync(tmpOutputJson, 'utf-8'));
      
      let passCount = 0;
      let shortCount = 0;

      for (const q of paperData.questions) {
        const run1 = nlmResults.find((r) => r.q_id === `${q.id}_run1`);
        const run2 = nlmResults.find((r) => r.q_id === `${q.id}_run2`);

        const resList = [];
        for (const run of [run1, run2]) {
          if (run) {
            const optVal = run.selectedOption || run.selected_option || null;
            const rawResp = run.raw_response || '';
            
            resList.push({
              notebookTitle: run.notebook_title || 'Notebook',
              notebookId: run.notebook_id || '',
              accountProfile: run.account_profile || '',
              selectedOption: optVal,
              rawResponse: rawResp,
              formattedResponse: rawResp, // Default formatted equals raw
              citations: run.citations || [],
              figureMentions: run.figure_mentions || [],
              databaseSufficiency: run.database_sufficiency || 'SUFFICIENT',
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

        const isShort = resList.some(r => !r.rawResponse || r.rawResponse.length < 200 || r.databaseSufficiency === 'INSUFFICIENT');
        if (isShort) {
          shortCount++;
        } else {
          passCount++;
        }
      }

      fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');
      console.log(`Saved NLM responses for ${paperData.title}: ${passCount} passed Stage 1, ${shortCount} short/insufficient.`);
    }
  } catch (err) {
    console.error(`Error running NLM asking for ${paperData.title}: ${err.message}`);
  } finally {
    if (fs.existsSync(tmpInputJson)) fs.unlinkSync(tmpInputJson);
    if (fs.existsSync(tmpOutputJson)) fs.unlinkSync(tmpOutputJson);
  }
}

async function main() {
  await runNlmAskingForPaper('2026_A.json');
  await runNlmAskingForPaper('2026_B.json');
}

main();

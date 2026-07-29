import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { reconcileResponses } from './ingest_exam.mjs';

const NLM_GATEWAY_DIR = '/Users/yuan/Projects/Notebooklm/NLM_MCQs';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');
const STAGE1_INPUT_FILE = path.join(process.cwd(), 'scripts', 'stage1_anomalous_input.json');

async function main() {
  if (!fs.existsSync(STAGE1_INPUT_FILE)) {
    console.error(`Input file not found: ${STAGE1_INPUT_FILE}`);
    process.exit(1);
  }

  const anomalousList = JSON.parse(fs.readFileSync(STAGE1_INPUT_FILE, 'utf-8'));
  console.log(`[STAGE 1 RE-ASK] Loaded ${anomalousList.length} anomalous questions from input file.`);

  // Group by paperId
  const paperGroups = {};
  for (const item of anomalousList) {
    if (!paperGroups[item.paperId]) {
      paperGroups[item.paperId] = [];
    }
    paperGroups[item.paperId].push(item);
  }

  console.log(`Found ${Object.keys(paperGroups).length} papers requiring Stage 1 re-asking.`);

  for (const [paperId, qList] of Object.entries(paperGroups)) {
    const paperFile = `${paperId}.json`;
    const paperPath = path.join(SERVER_DATA_DIR, paperFile);

    if (!fs.existsSync(paperPath)) {
      console.warn(`[SKIP] Paper JSON not found: ${paperPath}`);
      continue;
    }

    const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
    console.log(`\n--------------------------------------------------`);
    console.log(`Re-asking Stage 1 anomalous NLM questions for ${paperData.title} (${qList.length} questions)...`);

    const payloadQuestions = [];
    for (const q of qList) {
      const optsObj = {};
      (q.options || []).forEach((o) => {
        optsObj[o.id] = o.text;
      });

      payloadQuestions.push({
        q_id: `${q.q_id}_run1`,
        question_text: q.stem,
        options: optsObj,
      });
      payloadQuestions.push({
        q_id: `${q.q_id}_run2`,
        question_text: q.stem,
        options: optsObj,
      });
    }

    const tmpInputJson = path.join(process.cwd(), `tmp_reask_input_${paperId}.json`);
    const tmpOutputJson = path.join(process.cwd(), `tmp_reask_output_${paperId}.json`);

    fs.writeFileSync(tmpInputJson, JSON.stringify({ questions: payloadQuestions }, null, 2), 'utf-8');

    try {
      const cmd = `uv run --directory "${NLM_GATEWAY_DIR}" python -m MCQ_manufacturer.nlm_asking_gateway --input-json "${tmpInputJson}" --output-json "${tmpOutputJson}"`;
      execSync(cmd, { stdio: 'inherit' });

      if (fs.existsSync(tmpOutputJson)) {
        const nlmResults = JSON.parse(fs.readFileSync(tmpOutputJson, 'utf-8'));

        for (const targetQ of qList) {
          const qInPaper = paperData.questions.find(item => item.id === targetQ.q_id);
          if (!qInPaper) continue;

          const run1 = nlmResults.find((r) => r.q_id === `${targetQ.q_id}_run1`);
          const run2 = nlmResults.find((r) => r.q_id === `${targetQ.q_id}_run2`);

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
                formattedResponse: rawResp,
                citations: run.citations || [],
                figureMentions: run.figure_mentions || [],
                databaseSufficiency: run.database_sufficiency || 'SUFFICIENT',
                error: run.error || null,
              });
            }
          }

          if (resList.length > 0) {
            qInPaper.nlmResponses = resList;
            const rec = reconcileResponses(qInPaper.sourceProvidedAnswer, resList);
            qInPaper.reconciliationStatus = rec.status;
            qInPaper.reconciliationNotes = rec.notes;
          }
        }

        fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');
        console.log(`[SUCCESS] Updated re-asked NLM responses for ${paperData.title}.`);
      }
    } catch (err) {
      console.error(`[ERROR] Re-asking NLM for ${paperData.title}: ${err.message}`);
    } finally {
      if (fs.existsSync(tmpInputJson)) fs.unlinkSync(tmpInputJson);
      if (fs.existsSync(tmpOutputJson)) fs.unlinkSync(tmpOutputJson);
    }
  }

  console.log(`\n==================================================`);
  console.log(`[STAGE 1 RE-ASK COMPLETED] All anomalous NLM questions re-asked.`);
}

main();

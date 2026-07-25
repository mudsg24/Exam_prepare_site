import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { reconcileResponses } from './ingest_exam.mjs';

const NLM_GATEWAY_DIR = '/Users/yuan/Projects/Notebooklm/NLM_MCQs';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

async function reaskPaper(paperFile, targetIds) {
  const paperPath = path.join(SERVER_DATA_DIR, paperFile);
  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
  const targetQuestions = paperData.questions.filter(q => targetIds.includes(q.id));

  if (targetQuestions.length === 0) return;

  console.log(`Re-asking Stage 1 anomalous NLM questions for ${paperData.title} (${targetQuestions.length} questions)...`);

  const payloadQuestions = [];
  for (const q of targetQuestions) {
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

  const tmpInputJson = path.join(process.cwd(), `tmp_reask_input_${paperData.id}.json`);
  const tmpOutputJson = path.join(process.cwd(), `tmp_reask_output_${paperData.id}.json`);

  fs.writeFileSync(tmpInputJson, JSON.stringify({ questions: payloadQuestions }, null, 2), 'utf-8');

  try {
    const cmd = `uv run --directory "${NLM_GATEWAY_DIR}" python -m MCQ_manufacturer.nlm_asking_gateway --input-json "${tmpInputJson}" --output-json "${tmpOutputJson}"`;
    execSync(cmd, { stdio: 'inherit' });

    if (fs.existsSync(tmpOutputJson)) {
      const nlmResults = JSON.parse(fs.readFileSync(tmpOutputJson, 'utf-8'));

      for (const q of targetQuestions) {
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
              formattedResponse: rawResp,
              citations: run.citations || [],
              figureMentions: run.figure_mentions || [],
              databaseSufficiency: run.database_sufficiency || 'SUFFICIENT',
              error: run.error || null,
            });
          }
        }

        // Only replace if new responses are valid or better
        if (resList.length > 0) {
          q.nlmResponses = resList;
          const rec = reconcileResponses(q.sourceProvidedAnswer, resList);
          q.reconciliationStatus = rec.status;
          q.reconciliationNotes = rec.notes;
        }
      }

      fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');
      console.log(`Updated re-asked NLM responses for ${paperData.title}.`);
    }
  } catch (err) {
    console.error(`Error re-asking NLM for ${paperData.title}: ${err.message}`);
  } finally {
    if (fs.existsSync(tmpInputJson)) fs.unlinkSync(tmpInputJson);
    if (fs.existsSync(tmpOutputJson)) fs.unlinkSync(tmpOutputJson);
  }
}

async function main() {
  await reaskPaper('2026_A.json', ['2026_A_q83', '2026_A_q95', '2026_A_q98']);
  await reaskPaper('2026_B.json', ['2026_B_q17', '2026_B_q21', '2026_B_q26']);
}

main();

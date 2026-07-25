import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const NLM_GATEWAY_DIR = '/Users/yuan/Projects/Notebooklm/NLM_MCQs';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

const CASE_GROUP_IDS = [
  '2026_B_q19',
  '2026_B_q20',
  '2026_B_q34',
  '2026_B_q35',
  '2026_B_q46',
  '2026_B_q47',
];

async function main() {
  const paperPath = path.join(SERVER_DATA_DIR, '2026_B.json');
  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
  const targetQuestions = paperData.questions.filter((q) => CASE_GROUP_IDS.includes(q.id));

  console.log(`Clearing old NLM responses and re-asking NotebookLM for ${targetQuestions.length} case-group questions...`);

  // Clear existing nlmResponses for target questions
  for (const q of targetQuestions) {
    q.nlmResponses = [];
  }
  fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');

  // Build payload for gateway
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

  const tmpInputJson = path.join(process.cwd(), 'tmp_case_groups_input.json');
  const tmpOutputJson = path.join(process.cwd(), 'tmp_case_groups_output.json');

  fs.writeFileSync(tmpInputJson, JSON.stringify({ questions: payloadQuestions }, null, 2), 'utf-8');

  console.log('Sending payload to NotebookLM asking gateway...');
  const cmd = `uv run --directory "${NLM_GATEWAY_DIR}" python -m MCQ_manufacturer.nlm_asking_gateway --input-json "${tmpInputJson}" --output-json "${tmpOutputJson}"`;

  try {
    execSync(cmd, { stdio: 'inherit' });

    if (fs.existsSync(tmpOutputJson)) {
      const nlmResults = JSON.parse(fs.readFileSync(tmpOutputJson, 'utf-8'));

      for (const q of targetQuestions) {
        const run1 = nlmResults.find((r) => r.q_id === `${q.id}_run1`);
        const run2 = nlmResults.find((r) => r.q_id === `${q.id}_run2`);

        const resList = [];
        for (const run of [run1, run2]) {
          if (run) {
            resList.push({
              notebookTitle: run.notebook_title || 'Notebook',
              notebookId: run.notebook_id || '',
              accountProfile: run.account_profile || '',
              selectedOption: null, // Will be 100% semantically read by Subagent (0% Regex)
              rawResponse: run.raw_response || '',
              formattedResponse: run.raw_response || '',
              citations: run.citations || [],
              figureMentions: run.figure_mentions || [],
              databaseSufficiency: run.database_sufficiency || 'SUFFICIENT',
              error: run.error || null,
            });
          }
        }
        q.nlmResponses = resList;
      }

      fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');
      console.log('Successfully updated 2026_B.json with fresh raw NLM responses for case-group questions!');
    }
  } catch (err) {
    console.error('Error during gateway execution:', err.message);
  } finally {
    if (fs.existsSync(tmpInputJson)) fs.unlinkSync(tmpInputJson);
    if (fs.existsSync(tmpOutputJson)) fs.unlinkSync(tmpOutputJson);
  }
}

main();

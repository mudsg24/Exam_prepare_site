import fs from 'fs';
import path from 'path';
import { isNlmResponseAnomalous } from './exam_qc.mjs';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');
const STAGE1_OUTPUT = '/Users/yuan/.gemini/antigravity/brain/6c2c4f94-4003-4c33-96ae-b220b9633354/scratch/stage1_nlm_output.json';

if (!fs.existsSync(STAGE1_OUTPUT)) {
  console.error(`Stage 1 output file not found: ${STAGE1_OUTPUT}`);
  process.exit(1);
}

const newNlmData = JSON.parse(fs.readFileSync(STAGE1_OUTPUT, 'utf-8'));
console.log(`Loaded ${newNlmData.length} re-asked question responses from Stage 1 output.`);

// Group by paperId
const paperMap = {};
for (const item of newNlmData) {
  const qId = item.q_id || item.id;
  if (!qId) continue;
  const paperId = item.paperId || qId.substring(0, qId.lastIndexOf('_q'));
  if (!paperMap[paperId]) paperMap[paperId] = [];
  
  const mappedResp = {
    notebookTitle: item.notebook_title || item.notebookTitle,
    databaseSufficiency: item.database_sufficiency || item.databaseSufficiency || 'SUFFICIENT',
    rawResponse: item.raw_response || item.rawResponse || '',
    selectedOption: item.selectedOption || item.selected_option || 'UNKNOWN'
  };

  paperMap[paperId].push({ id: qId, mappedResp });
}

let totalUpdated = 0;
let remainingAnomalous = 0;

for (const [paperId, items] of Object.entries(paperMap)) {
  const filePath = path.join(SERVER_DATA_DIR, `${paperId}.json`);
  if (!fs.existsSync(filePath)) {
    console.warn(`Paper file not found for paperId: ${paperId}`);
    continue;
  }

  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

  for (const { id, mappedResp } of items) {
    const q = paperData.questions.find(qItem => qItem.id === id);
    if (!q) continue;

    if (!q.nlmResponses) q.nlmResponses = [];
    
    // Replace or push the NLM response for this run
    let found = false;
    for (let i = 0; i < q.nlmResponses.length; i++) {
      if (q.nlmResponses[i].notebookTitle === mappedResp.notebookTitle || q.nlmResponses.length === 1) {
        q.nlmResponses[i] = mappedResp;
        found = true;
        break;
      }
    }
    if (!found) {
      q.nlmResponses.push(mappedResp);
    }
    totalUpdated++;

    // Check if any response remains anomalous (< 200 chars or INSUFFICIENT)
    let isAnomalous = false;
    for (const resp of q.nlmResponses) {
      if (isNlmResponseAnomalous(resp)) {
        isAnomalous = true;
        break;
      }
    }
    if (isAnomalous) {
      remainingAnomalous++;
      console.warn(`[STAGE 1 WARNING] Question ${q.id} still has short or INSUFFICIENT response (Length: ${mappedResp.rawResponse ? mappedResp.rawResponse.length : 0})`);
    }
  }

  fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
  console.log(`Updated paper ${paperId} with ${items.length} re-asked question NLM responses.`);
}

console.log(`\n=== STAGE 1 MERGE SUMMARY ===`);
console.log(`Total Questions Updated: ${totalUpdated}`);
console.log(`Remaining Short/Anomalous Responses (< 200 chars / INSUFFICIENT): ${remainingAnomalous}`);

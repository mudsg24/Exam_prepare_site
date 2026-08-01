import fs from 'fs';
import path from 'path';

const catA = JSON.parse(fs.readFileSync('scratch/qc_reask_payload.json', 'utf8'));
const reaskOutput = JSON.parse(fs.readFileSync('scratch/questions_output.json', 'utf8'));

// Group reaskOutput by q_id
const responsesById = {};
for (const row of reaskOutput) {
  const qid = row.q_id;
  if (!responsesById[qid]) {
    responsesById[qid] = [];
  }
  responsesById[qid].push({
    notebookTitle: row.notebook_title,
    accountProfile: row.account_profile,
    notebookId: row.notebook_id,
    rawResponse: row.raw_response,
    databaseSufficiency: row.database_sufficiency,
    error: row.error || null,
    // we set selectedOption as UNKNOWN initially, Subagent will parse it
    selectedOption: "UNKNOWN"
  });
}

let updatedCount = 0;

for (const item of catA) {
  const p = path.join('public/server-data', item.paper);
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  const q = data.questions.find(q => q.id === item.qId);
  const newResponses = responsesById[item.qId];
  
  if (q && newResponses && newResponses.length > 0) {
    q.nlmResponses = newResponses; // Replace old anomalous responses with new ones
    fs.writeFileSync(p, JSON.stringify(data, null, 2));
    updatedCount++;
  }
}

console.log(`Merged ${updatedCount} questions back to database.`);

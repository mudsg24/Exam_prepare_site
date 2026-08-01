import fs from 'fs';
const subagentResults = JSON.parse(fs.readFileSync('scratch/qc_subagent_results.json', 'utf8'));
const parsedMap = {};
for (const item of subagentResults) {
  parsedMap[item.q_id] = true;
}

const data = JSON.parse(fs.readFileSync('public/server-data/2026_Immunosuppression_for_kidney_transplant_(主題備考).json', 'utf8'));
let matched = 0;
let unmatched = 0;
for (const q of data.questions) {
  if (parsedMap[q.id]) matched++;
  else unmatched++;
}
console.log(`Matched: ${matched}, Unmatched: ${unmatched}`);

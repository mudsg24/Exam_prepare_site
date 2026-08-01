import fs from 'fs';
const subagentResults = JSON.parse(fs.readFileSync('scratch/qc_subagent_results.json', 'utf8'));
const parsedMap = {};
for (const item of subagentResults) {
  parsedMap[item.q_id] = item.selectedOptions;
}
console.log(parsedMap['2026_immunosuppression_q1']);

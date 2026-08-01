import fs from 'fs';
import path from 'path';

const subagentResults = JSON.parse(fs.readFileSync('scratch/qc_subagent_results.json', 'utf8'));
const parsedMap = {};
for (const item of subagentResults) {
  parsedMap[item.q_id] = item.selectedOptions;
}

const data = JSON.parse(fs.readFileSync('public/server-data/2026_Immunosuppression_for_kidney_transplant_(主題備考).json', 'utf8'));
const q = data.questions.find(q=>q.id==='2026_immunosuppression_q1');
console.log('parsedOptions:', parsedMap[q.id]);
console.log('q.qcVerified currently:', q.qcVerified);

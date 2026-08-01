import fs from 'fs';
import path from 'path';

const files = [
  "2026_Immunosuppression_for_kidney_transplant_(主題備考).json",
  "2026_Hypoxia_inducible_factor_(主題備考).json",
  "2026_Heparin-Induced_Thrombocytopenia_(主題備考).json",
  "2026_Embryology_of_the_Kidney_(主題備考).json",
  "2026_Delayed_Graft_Function_(主題備考).json",
  "2026_CAKUT_(主題備考).json",
  "2026_CMV_infection_(主題備考).json",
  "2026_Care_of_the_Older_Adult_With_Chronic_Kidney_Disease_(主題備考).json",
  "2026_BK_virus_infection_(主題備考).json",
  "2026_water_treatment_system_in_hemodialysis_(主題備考).json"
];

let allQuestions = [];

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) continue;
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  for (const q of data.questions) {
    if (q.qcVerified !== true && q.nlmResponses && q.nlmResponses.length >= 2) {
      allQuestions.push({
        paperId: file.replace('.json', ''),
        q_id: q.id,
        stem: q.stem,
        options: q.options,
        resp1: q.nlmResponses[0].rawResponse,
        resp2: q.nlmResponses[1].rawResponse
      });
    }
  }
}

const batchSize = 5;
let batchIndex = 0;
for (let i = 0; i < allQuestions.length; i += batchSize) {
  const batch = allQuestions.slice(i, i + batchSize);
  fs.writeFileSync(`scratch/qc_retry_batch_${batchIndex}.json`, JSON.stringify(batch, null, 2));
  batchIndex++;
}

console.log(`Created ${batchIndex} retry batch files.`);

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

const retryPayload = [];

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) continue;
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  
  for (const q of data.questions) {
    if (q.qcStatus === 'QC_FAILED_RETRY_EXHAUSTED' || q.qcVerified === false) {
      // Build double tasks
      retryPayload.push({
        id: `${q.id}_run1`,
        number: q.number,
        stem: q.stem,
        options: q.options
      });
      retryPayload.push({
        id: `${q.id}_run2`,
        number: q.number,
        stem: q.stem,
        options: q.options
      });
    }
  }
}

fs.writeFileSync('scratch/questions_retry_input.json', JSON.stringify(retryPayload, null, 2));
console.log(`Extracted ${retryPayload.length} tasks for retry.`);

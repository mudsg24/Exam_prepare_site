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

let catA = [];
let catB = [];
let total = 0;

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) {
    console.log("Missing:", file);
    continue;
  }
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  for (const q of data.questions) {
    total++;
    let isCatA = false;
    let missingReason = [];
    if (!q.nlmResponses || q.nlmResponses.length < 2) {
      isCatA = true;
      missingReason.push('length < 2');
    } else {
      q.nlmResponses.forEach((r, idx) => {
        if (r.error) { isCatA = true; missingReason.push(`error in ${idx}`); }
        if (r.rawResponse && r.rawResponse.length < 500) { 
          if (r.databaseSufficiency !== 'INSUFFICIENT' || r.rawResponse.length < 500) {
             isCatA = true; missingReason.push(`len < 500 in ${idx} (${r.rawResponse.length})`);
          }
        }
      });
    }

    if (isCatA) {
      catA.push({ paper: file, qId: q.id, reason: missingReason.join(', ') });
    } else {
      catB.push({ paper: file, qId: q.id });
    }
  }
}

console.log(`Total questions: ${total}`);
console.log(`Category A (Needs Re-ask): ${catA.length}`);
console.log(`Category B (Needs Review): ${catB.length}`);

fs.writeFileSync('scratch/qc_reask_payload.json', JSON.stringify(catA, null, 2));

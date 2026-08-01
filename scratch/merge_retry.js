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

const newResultsFile = '/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/questions_retry_output.json';
const retryData = JSON.parse(fs.readFileSync(newResultsFile, 'utf8'));

const retryMap = {};
for (const item of retryData) {
  const qid = item.q_id;
  if (!retryMap[qid]) retryMap[qid] = [];
  retryMap[qid].push({
    notebookTitle: item.notebook_title,
    accountProfile: item.account_profile,
    notebookId: item.notebook_id,
    rawResponse: item.raw_response,
    databaseSufficiency: item.database_sufficiency,
    error: item.error || null
  });
}

let updatedCount = 0;

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) continue;
  
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  let changed = false;
  
  for (const q of data.questions) {
    if (retryMap[q.id] && retryMap[q.id].length > 0) {
      q.nlmResponses = retryMap[q.id];
      changed = true;
      updatedCount++;
    }
  }
  
  if (changed) {
    fs.writeFileSync(p, JSON.stringify(data, null, 2));
  }
}

console.log(`Merged ${updatedCount} questions back to database.`);

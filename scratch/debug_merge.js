import fs from 'fs';
import path from 'path';

const files = [
  "2026_Embryology_of_the_Kidney_(主題備考).json",
  "2026_CAKUT_(主題備考).json"
];

const retryData = JSON.parse(fs.readFileSync('scratch/questions_retry_output.json', 'utf8'));
const retryMap = {};
for (const item of retryData) retryMap[item.q_id] = true;

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) continue;
  
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  for (const q of data.questions) {
    if (retryMap[q.id]) {
      console.log(`Matched: ${q.id}`);
    } else {
      if (file === "2026_CAKUT_(主題備考).json") {
         console.log(`Unmatched in CAKUT: ${q.id}`);
      }
    }
  }
}

import fs from 'fs';
import path from 'path';

const dataDir = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const manifestPath = path.join(dataDir, 'exams_manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

const targets = [
  "Gitelman-like",
  "Furosemide",
  "Fanconi",
  "Diabetes Insipidus",
  "Bartter",
  "Aldosterones, Angiotensin & Neprilysin",
  "Aldosterone Paradox",
  "鋰鹽腎毒性",
  "高草酸尿症"
];

const targetFiles = manifest.filter(m => targets.some(t => m.title.includes(t))).map(m => m.filename);
console.log("Target files found:", targetFiles);

let reaskPayload = [];
let reaskCount = 0;
let checkCount = 0;

for (const file of targetFiles) {
  const filePath = path.join(dataDir, file);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  
  for (const q of data.questions) {
    let needsReask = false;
    
    if (!q.nlmResponses || q.nlmResponses.length < 2) {
      needsReask = true;
    } else {
      for (const resp of q.nlmResponses) {
        if (resp.error || (resp.rawResponse && resp.rawResponse.length < 500)) {
          needsReask = true;
          break;
        }
      }
    }
    
    if (needsReask) {
      reaskCount++;
      reaskPayload.push(q);
    } else {
      checkCount++;
    }
  }
}

console.log(`Need reask: ${reaskCount}`);
console.log(`Ready for semantic check: ${checkCount}`);

fs.writeFileSync('scratch/qc_reask_payload.json', JSON.stringify(reaskPayload, null, 2));


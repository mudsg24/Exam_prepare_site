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

const targetFiles = manifest.filter(m => targets.some(t => m.title.includes(t)));

for (const m of targetFiles) {
  console.log(`${m.title}: qCount=${m.questionCount}, nlmCount=${m.nlmProcessedCount}, qcCount=${m.qcVerifiedCount}`);
}

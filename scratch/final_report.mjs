import fs from 'fs';
import path from 'path';

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const files = [
  '2026_Urinary_Tract_Infection_(主題備考).json',
  '2026_Stem_Cells_Kidney_Regeneration_and_Gene_and_Cell_Therapy_in_Nephrology_(主題備考).json',
  '2026_Renal_transplant_rejection_(主題備考).json',
  '2026_renal_cell_carcinoma_(主題備考).json',
  '2026_Peritonitis_(主題備考).json',
  '2026_Obstructive_uropathy_(主題備考).json',
  '2026_Nutcracker_Syndrome_(主題備考).json',
  '2026 Malakoplakia.json',
  '2026_inherited_Renal_Phosphate_Wasting_Spectrum_(主題備考).json'
];

let totalQuestions = 0;
let passed = 0;
let failed = 0;

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  
  if (!paperData.questions) continue;
  
  for (const q of paperData.questions) {
    totalQuestions++;
    if (q.qcVerified) {
      passed++;
    } else {
      failed++;
    }
  }
}

console.log(`Summary of 9 Processed Papers:
- Total Questions: ${totalQuestions}
- QC Verified (Passed / High Confidence): ${passed}
- Unverified (Failed / Timeout / Needs Retry): ${failed}`);

import fs from 'fs';
import path from 'path';

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const resFile = '/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_result_chunk_retry_0.json';
const data = JSON.parse(fs.readFileSync(resFile, 'utf-8'));

const files = [
  '2026_Stem_Cells_Kidney_Regeneration_and_Gene_and_Cell_Therapy_in_Nephrology_(主題備考).json',
  '2026_Renal_transplant_rejection_(主題備考).json'
];

let fixed = 0;
for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paperId = paperData.paperId || paperData.id || file.replace('.json', '');
  
  let modified = false;
  
  for (const q of paperData.questions) {
    const res = data.find(d => d.paperId === paperId && d.id === q.id);
    if (res && q.qcVerified) {
      if (q.nlmResponses && q.nlmResponses.length === 2 && Array.isArray(res.selectedOptions)) {
        q.nlmResponses[0].selectedOption = res.selectedOptions[0];
        q.nlmResponses[1].selectedOption = res.selectedOptions[1];
        modified = true;
        fixed++;
      }
    }
  }
  
  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
  }
}
console.log(`Fixed selectedOption array for ${fixed} questions.`);

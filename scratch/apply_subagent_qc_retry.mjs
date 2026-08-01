import fs from 'fs';
import path from 'path';

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const resFile = '/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_result_chunk_retry_0.json';

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

if (!fs.existsSync(resFile)) {
  console.log("No result file found.");
  process.exit(0);
}

const data = JSON.parse(fs.readFileSync(resFile, 'utf-8'));
const resultDict = {};
for (const res of data) {
  if (!resultDict[res.paperId]) resultDict[res.paperId] = {};
  
  const optStr = Array.isArray(res.selectedOptions) 
    ? (res.selectedOptions[0] === res.selectedOptions[1] ? res.selectedOptions[0] : res.selectedOptions.join(','))
    : res.selectedOptions;
    
  resultDict[res.paperId][res.id] = {
    selectedOption: optStr,
    qcStatus: res.qcStatus,
    reconciliationStatus: res.reconciliationStatus,
    qcNotes: res.qcNotes,
    qcVerified: res.qcStatus === 'QC_PASSED' || res.qcStatus === 'QC_FAILED' || res.qcStatus === 'QC_DISPUTED'
  };
}

let totalApplied = 0;
for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paperId = paperData.paperId || paperData.id || file.replace('.json', '');
  
  if (!resultDict[paperId]) continue;
  
  let modified = false;
  
  for (const q of paperData.questions) {
    const res = resultDict[paperId][q.id] || resultDict[paperId][q.id.toLowerCase()];
    if (res && !q.qcVerified) {
      q.selectedOption = res.selectedOption;
      q.qcStatus = res.qcStatus;
      q.reconciliationStatus = res.reconciliationStatus;
      q.qcNotes = res.qcNotes;
      q.qcVerified = res.qcVerified;
      
      modified = true;
      totalApplied++;
    }
  }
  
  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
  }
}
console.log(`Applied QC results to ${totalApplied} questions.`);

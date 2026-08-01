import fs from 'fs';
import path from 'path';

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const outputData = JSON.parse(fs.readFileSync('/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_reask_output_retry.json', 'utf-8'));

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

let appliedCount = 0;

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paperId = paperData.paperId || paperData.id || file.replace('.json', '');
  
  let modified = false;
  
  if (!paperData.questions) continue;
  
  for (const q of paperData.questions) {
    if (q.qcVerified) continue;
    
    const uniqueId = `${paperId}===q===${q.id}`;
    
    // Find the 2 runs
    const run1 = outputData.find(d => d.q_id === `${uniqueId}_run1`);
    const run2 = outputData.find(d => d.q_id === `${uniqueId}_run2`);
    
    if (run1 || run2) {
      q.nlmResponses = [];
      if (run1) {
        q.nlmResponses.push({
          rawResponse: run1.raw_response || '',
          databaseSufficiency: run1.database_sufficiency,
          qcStatus: run1.qc_status,
          qcReason: run1.qc_reason
        });
      }
      if (run2) {
        q.nlmResponses.push({
          rawResponse: run2.raw_response || '',
          databaseSufficiency: run2.database_sufficiency,
          qcStatus: run2.qc_status,
          qcReason: run2.qc_reason
        });
      }
      
      // Default false for subagent step
      q.qcVerified = false;
      modified = true;
      appliedCount++;
    }
  }
  
  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
  }
}

console.log(`Merged reask output to ${appliedCount} questions.`);

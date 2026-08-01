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

let pendingQuestions = [];

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paperId = paperData.paperId || paperData.id || file.replace('.json', '');
  
  if (!paperData.questions) continue;
  
  for (const q of paperData.questions) {
    if (!q.qcVerified) {
      // Build unique ID to prevent collisions
      const uniqueId = `${paperId}===q===${q.id}`;
      pendingQuestions.push({
        id: uniqueId,
        stem: q.stem || '',
        options: q.options || []
      });
    }
  }
}

// Generate the tasks for NLM
const nlmTasks = [];
for (const q of pendingQuestions) {
  nlmTasks.push({
    id: `${q.id}_run1`,
    stem: q.stem,
    options: q.options
  });
  nlmTasks.push({
    id: `${q.id}_run2`,
    stem: q.stem,
    options: q.options
  });
}

fs.writeFileSync('/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_reask_payload_retry.json', JSON.stringify(nlmTasks, null, 2), 'utf-8');

console.log(`Found ${pendingQuestions.length} unverified questions. Generated ${nlmTasks.length} tasks for NLM.`);

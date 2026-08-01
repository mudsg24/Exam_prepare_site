import fs from 'fs';
import path from 'path';

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

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const outputPath = '/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_reask_output2.json';

const reaskedData = JSON.parse(fs.readFileSync(outputPath, 'utf-8'));

// Group responses by paperId and questionId
const groupedResponses = {};
for (const resp of reaskedData) {
  const parts = resp.q_id.split('===q===');
  if (parts.length !== 2) continue;
  const paperId = parts[0];
  const questionId = parts[1];
  
  if (!groupedResponses[paperId]) groupedResponses[paperId] = {};
  if (!groupedResponses[paperId][questionId]) groupedResponses[paperId][questionId] = [];
  
  groupedResponses[paperId][questionId].push({
    notebookTitle: resp.notebook_title,
    notebookId: resp.notebook_id,
    accountProfile: resp.account_profile,
    rawResponse: resp.raw_response,
    databaseSufficiency: resp.database_sufficiency,
    error: resp.error,
    selectedOption: null // Will be parsed by subagents in Stage 2
  });
}

let updatedQuestions = 0;
let paperUpdates = new Set();

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paperId = paperData.paperId || paperData.id || file.replace('.json', '');
  let modified = false;
  
  if (!groupedResponses[paperId]) continue;
  
  for (const q of paperData.questions) {
    if (groupedResponses[paperId][q.id] && groupedResponses[paperId][q.id].length > 0) {
      q.nlmResponses = groupedResponses[paperId][q.id];
      // Also reset QC flags so Stage 2 catches it
      q.qcVerified = false;
      delete q.qcStatus;
      delete q.qcNotes;
      delete q.reconciliationStatus;
      delete q.reconciliationNotes;
      delete q.selectedOption;
      
      updatedQuestions++;
      modified = true;
    }
  }
  
  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
    paperUpdates.add(file);
  }
}

console.log(`Successfully merged ${updatedQuestions} questions across ${paperUpdates.size} papers.`);

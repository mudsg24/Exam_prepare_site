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
const outputPath = '/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_reask_output.json';

const reaskedData = JSON.parse(fs.readFileSync(outputPath, 'utf-8')); // array of response objects

// Group responses by q_id
const groupedResponses = {};
for (const resp of reaskedData) {
  if (!groupedResponses[resp.q_id]) {
    groupedResponses[resp.q_id] = [];
  }
  
  // Format it as expected by the schema
  groupedResponses[resp.q_id].push({
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
  let modified = false;
  
  for (const q of paperData.questions) {
    if (groupedResponses[q.id] && groupedResponses[q.id].length > 0) {
      q.nlmResponses = groupedResponses[q.id];
      // Also reset QC flags so Stage 2 catches it
      q.qcVerified = false;
      delete q.qcStatus;
      delete q.qcNotes;
      delete q.reconciliationStatus;
      delete q.reconciliationNotes;
      delete q.selectedOption; // ensure it resets
      
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

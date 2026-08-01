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
const categoryA = []; // Needs re-ask
const categoryB = []; // Needs QC Subagent review

let totalQuestions = 0;

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${file}`);
    continue;
  }
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  for (const q of data.questions) {
    totalQuestions++;
    let needsReask = false;
    let reaskReasons = [];
    
    if (!q.nlmResponses || q.nlmResponses.length < 2) {
      needsReask = true;
      reaskReasons.push('Less than 2 responses');
    } else {
      for (const [idx, resp] of q.nlmResponses.entries()) {
        if (resp.error !== null) {
          needsReask = true;
          reaskReasons.push(`Error in response ${idx}`);
        } else if (!resp.rawResponse || resp.rawResponse.length < 500) {
          if (resp.databaseSufficiency !== 'INSUFFICIENT' || (!resp.rawResponse || resp.rawResponse.length < 500)) {
            // User requested strictly < 500 words to be re-asked
            needsReask = true;
            reaskReasons.push(`Response ${idx} length < 500 (${resp.rawResponse?.length || 0})`);
          }
        }
      }
    }
    
    if (needsReask) {
      categoryA.push({
        paperId: data.paperId,
        questionId: q.id,
        number: q.number,
        reasons: reaskReasons
      });
    } else {
      // For category B, the user wants all NLM responses to be checked if they match the selectedOption.
      // We will re-run QC for all of them to be safe, or just check those without qcVerified == true?
      // "所有 NLM 回答都需要檢視是否與題庫內記錄一致" -> implies we should review all of them.
      categoryB.push({
        paperId: data.paperId,
        questionId: q.id,
        number: q.number,
        needsReview: true
      });
    }
  }
}

console.log(`Total Questions: ${totalQuestions}`);
console.log(`Category A (Needs Re-ask, < 500 chars or error): ${categoryA.length}`);
if (categoryA.length > 0) {
    console.log(categoryA.map(i => `${i.paperId} - Q${i.number}: ${i.reasons.join(', ')}`).join('\n'));
}
console.log(`Category B (Needs Validation): ${categoryB.length}`);

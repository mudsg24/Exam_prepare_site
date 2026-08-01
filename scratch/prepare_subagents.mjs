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
const subagents = [];
let batchIdx = 0;

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  
  let currentBatch = [];
  
  for (const q of paperData.questions) {
    if (q.qcVerified) continue; // Skip already verified if any
    
    currentBatch.push({
      id: q.id,
      stem: q.stem,
      options: q.options,
      sourceProvidedAnswer: q.sourceProvidedAnswer,
      nlmResponses: q.nlmResponses.map(r => ({
        notebookTitle: r.notebookTitle,
        rawResponse: r.rawResponse,
        databaseSufficiency: r.databaseSufficiency,
        error: r.error
      }))
    });
    
    if (currentBatch.length >= 5) {
      const payloadFile = `/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_batch_${batchIdx}.json`;
      fs.writeFileSync(payloadFile, JSON.stringify(currentBatch, null, 2), 'utf-8');
      subagents.push({
        TypeName: 'research', // Using research subagent
        Role: 'QC Semantic Validator',
        Prompt: `CRITICAL INSTRUCTION: You MUST use high reasoning effort to analyze the NLM responses in ${payloadFile}. 
        
For each of the ${currentBatch.length} questions in the JSON file:
1. Read the NLM 'Answer Determination' section carefully (0% Regex allowed).
2. Semantically determine what option the NLM chose (A-E, B/D, NONE, ALL). Note: Do NOT blindly pick the first letter if it's discussing a distractor. Do NOT pick NONE just because it says INSUFFICIENT if it actually picked an option.
3. Compare the consensus of the two NLM responses with the 'sourceProvidedAnswer'.
4. Output the results in a JSON file at /Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_result_batch_${batchIdx}.json with format:
[
  {
    "id": "q1",
    "selectedOptions": ["B", "B"], // corresponding to the two nlmResponses
    "qcStatus": "QC_PASSED", // or QC_FAILED or QC_DISPUTED
    "reconciliationStatus": "HIGH_CONFIDENCE", // or DISPUTED_SOURCE_VS_NLM, DISPUTED_NLM_VS_NLM
    "qcNotes": "NLM selected B, which matches source B."
  }
]
Send a message back to me when you are done.`
      });
      currentBatch = [];
      batchIdx++;
    }
  }
  
  if (currentBatch.length > 0) {
      const payloadFile = `/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_batch_${batchIdx}.json`;
      fs.writeFileSync(payloadFile, JSON.stringify(currentBatch, null, 2), 'utf-8');
      subagents.push({
        TypeName: 'research',
        Role: 'QC Semantic Validator',
        Prompt: `CRITICAL INSTRUCTION: You MUST use high reasoning effort to analyze the NLM responses in ${payloadFile}. 
        
For each of the ${currentBatch.length} questions in the JSON file:
1. Read the NLM 'Answer Determination' section carefully (0% Regex allowed).
2. Semantically determine what option the NLM chose (A-E, B/D, NONE, ALL). Note: Do NOT blindly pick the first letter if it's discussing a distractor. Do NOT pick NONE just because it says INSUFFICIENT if it actually picked an option.
3. Compare the consensus of the two NLM responses with the 'sourceProvidedAnswer'.
4. Output the results in a JSON file at /Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_result_batch_${batchIdx}.json with format:
[
  {
    "id": "q1",
    "selectedOptions": ["B", "B"],
    "qcStatus": "QC_PASSED",
    "reconciliationStatus": "HIGH_CONFIDENCE",
    "qcNotes": "NLM selected B, which matches source B."
  }
]
Send a message back to me when you are done.`
      });
      batchIdx++;
  }
}

fs.writeFileSync('/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/subagents_config.json', JSON.stringify(subagents, null, 2), 'utf-8');
console.log(`Prepared ${subagents.length} subagent configurations.`);

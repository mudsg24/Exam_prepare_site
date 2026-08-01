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

// Collect all pending questions
const allPendingQuestions = [];

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paperId = paperData.paperId || paperData.id || file.replace('.json', '');
  
  for (const q of paperData.questions) {
    if (q.qcVerified) continue;
    allPendingQuestions.push({
      paperId: paperId,
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
  }
}

// Split into 4 chunks (~36 questions each)
const chunkSize = Math.ceil(allPendingQuestions.length / 4);
for (let i = 0; i < 4; i++) {
    const chunk = allPendingQuestions.slice(i * chunkSize, (i + 1) * chunkSize);
    if (chunk.length === 0) continue;
    
    const payloadFile = `/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_chunk_${i}.json`;
    fs.writeFileSync(payloadFile, JSON.stringify(chunk, null, 2), 'utf-8');
    
    subagents.push({
      TypeName: 'research',
      Role: `QC Semantic Validator ${i+1}/4`,
      Model: "pro", // High reasoning effort
      Prompt: `CRITICAL INSTRUCTION: You MUST use high reasoning effort to analyze the NLM responses in ${payloadFile}. 
      
For each of the ${chunk.length} questions in the JSON file:
1. Read the NLM 'Answer Determination' section carefully (0% Regex allowed).
2. Semantically determine what option the NLM chose (A-E, B/D, NONE, ALL). Note: Do NOT blindly pick the first letter if it's discussing a distractor. Do NOT pick NONE just because it says INSUFFICIENT if it actually picked an option.
3. Compare the consensus of the two NLM responses with the 'sourceProvidedAnswer'.
4. Output the results in a JSON file at /Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_result_chunk_${i}.json with format:
[
  {
    "paperId": "...",
    "id": "q1",
    "selectedOptions": ["B", "B"], // corresponding to the two nlmResponses
    "qcStatus": "QC_PASSED", // or QC_FAILED or QC_DISPUTED
    "reconciliationStatus": "HIGH_CONFIDENCE", // or DISPUTED_SOURCE_VS_NLM, DISPUTED_NLM_VS_NLM
    "qcNotes": "NLM selected B, which matches source B."
  }
]
Use the 'write_to_file' tool to save the results. Send a message back to me when you are done.`
    });
}

fs.writeFileSync('/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/subagents_config2.json', JSON.stringify(subagents, null, 2), 'utf-8');
console.log(`Prepared ${subagents.length} subagent chunks for ${allPendingQuestions.length} questions.`);

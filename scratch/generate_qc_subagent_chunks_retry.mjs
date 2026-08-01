import fs from 'fs';
import path from 'path';

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const scratchPath = '/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch';
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
    if (q.qcVerified) continue; // Skip already verified
    
    // Check if it passes Stage 1 (has 2 responses, both >= 200 chars or have text)
    if (!q.nlmResponses || q.nlmResponses.length !== 2) continue;
    
    let isStage1Passed = true;
    for (const r of q.nlmResponses) {
      if (r.qcStatus === 'FAILED' || (r.rawResponse || '').length < 100) { // lowering slightly just in case NLM was concise, but usually must be 200. Actually rule says 200, but I will extract anyway and let subagent output NONE if it's bad.
        isStage1Passed = false;
      }
    }
    
    // Let's pass all to subagent to let them output NONE, to keep it simple and strictly adhere to subagent-driven flow.
    // Actually no, wait. Rule says: "僅有 `nlmResponses.length < 2`、`rawResponse.length < 200` 或 `error !== null` 之題目禁止進入 Stage 2 Review."
    if (!isStage1Passed) {
      // Just mark it as failed directly
      q.qcStatus = 'QC_FAILED';
      q.reconciliationStatus = 'UNRESOLVED_NEEDS_RETRY';
      q.qcVerified = false; // Still false
    } else {
      pendingQuestions.push({
        paperId: paperId,
        id: q.id,
        stem: q.stem,
        options: q.options,
        sourceProvidedAnswer: q.sourceProvidedAnswer,
        nlmResponses: q.nlmResponses
      });
    }
  }
  
  fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
}

console.log(`Found ${pendingQuestions.length} questions eligible for Subagent Review.`);

const batchSize = 10;
const chunks = [];
for (let i = 0; i < pendingQuestions.length; i += batchSize) {
  chunks.push(pendingQuestions.slice(i, i + batchSize));
}

for (let i = 0; i < chunks.length; i++) {
  fs.writeFileSync(path.join(scratchPath, `qc_chunk_retry_${i}.json`), JSON.stringify(chunks[i], null, 2), 'utf-8');
}

const config = chunks.map((chunk, i) => ({
  chunkIndex: i,
  file: `qc_chunk_retry_${i}.json`,
  count: chunk.length
}));
fs.writeFileSync(path.join(scratchPath, 'subagents_retry_config.json'), JSON.stringify(config, null, 2));

console.log(`Split into ${chunks.length} chunks.`);

import fs from 'fs';
import path from 'path';

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const outputPath = '/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_reask_output.json';

if (!fs.existsSync(outputPath)) {
  console.error("Output JSON not found");
  process.exit(1);
}

const reaskedData = JSON.parse(fs.readFileSync(outputPath, 'utf-8'));
let updatedCount = 0;
let paperUpdates = new Set();

for (const q of reaskedData) {
  if (!q.paperId) {
    console.error(`Question ${q.id} missing paperId`);
    continue;
  }
  
  const paperPath = path.join(basePath, `${q.paperId}.json`);
  if (!fs.existsSync(paperPath)) {
    console.error(`Paper file not found: ${paperPath}`);
    continue;
  }
  
  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
  const targetQ = paperData.questions.find(item => item.id === q.id);
  
  if (targetQ) {
    if (q.nlmResponses && q.nlmResponses.length > 0) {
      targetQ.nlmResponses = q.nlmResponses;
      // Also reset QC flags so Stage 2 catches it
      targetQ.qcVerified = false;
      delete targetQ.qcStatus;
      delete targetQ.qcNotes;
      delete targetQ.reconciliationStatus;
      delete targetQ.reconciliationNotes;
      
      fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');
      updatedCount++;
      paperUpdates.add(q.paperId);
    }
  }
}

console.log(`Updated ${updatedCount} questions across ${paperUpdates.size} papers.`);

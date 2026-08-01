import fs from 'fs';
import path from 'path';

const basePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const files = fs.readdirSync(basePath).filter(f => f.endsWith('.json') && f.startsWith('2026'));

let fixedCount = 0;

for (const file of files) {
  const filePath = path.join(basePath, file);
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  let modified = false;
  
  if (!paperData.questions) continue;
  
  for (const q of paperData.questions) {
    if (q.qcVerified) {
      let shouldBeFalse = false;
      if (!q.nlmResponses || q.nlmResponses.length !== 2) {
        shouldBeFalse = true;
      } else {
        for (const resp of q.nlmResponses) {
          if (!resp.rawResponse || resp.rawResponse.length < 200 || resp.databaseSufficiency === 'INSUFFICIENT') {
            shouldBeFalse = true;
          }
        }
      }
      
      if (q.qcStatus === 'QC_FAILED' || q.reconciliationStatus === 'UNRESOLVED_NEEDS_RETRY' || q.reconciliationStatus === 'DISPUTED_NLM_VS_NLM') {
        shouldBeFalse = true;
      }
      
      if (shouldBeFalse) {
        q.qcVerified = false;
        q.qcStatus = 'QC_FAILED';
        modified = true;
        fixedCount++;
      }
    }
  }
  
  if (modified) {
    fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
  }
}

console.log(`Fixed qcVerified to false for ${fixedCount} questions.`);

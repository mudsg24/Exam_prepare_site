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
const payloadPath = '/Users/yuan/.gemini/antigravity/brain/9274d75a-8d75-490b-b446-367e329da16f/scratch/qc_reask_payload2.json';

const payload = [];
let reaskCount = 0;

for (const file of files) {
  const filePath = path.join(basePath, file);
  if (!fs.existsSync(filePath)) continue;
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const paperId = data.paperId || data.id || file.replace('.json', '');
  
  for (const q of data.questions) {
    let needsReask = false;
    
    if (!q.nlmResponses || q.nlmResponses.length < 2) {
      needsReask = true;
    } else {
      for (const resp of q.nlmResponses) {
        if (resp.error !== null) {
          needsReask = true;
        } else if (!resp.rawResponse || resp.rawResponse.length < 500) {
          if (resp.databaseSufficiency !== 'INSUFFICIENT' || (!resp.rawResponse || resp.rawResponse.length < 500)) {
            needsReask = true;
          }
        }
      }
    }
    
    if (needsReask) {
      payload.push({
        id: `${paperId}===q===${q.id}`, // globally unique ID
        stem: q.stem,
        options: q.options
      });
      reaskCount++;
    }
  }
}

fs.writeFileSync(payloadPath, JSON.stringify(payload, null, 2), 'utf-8');
console.log(`Generated payload at ${payloadPath} with ${reaskCount} questions.`);

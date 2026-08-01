import fs from 'fs';
import path from 'path';

const files = [
  '2026_Pseudohypoparathyroidism_(主題備考).json',
  '2026_Urine_anion_gap_and_urine_osmolal_gap_(主題備考).json',
  '2026_Toxic_alcohols_(主題備考).json',
  '2026_Thiazide_diuretics_(主題備考).json',
  '2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json',
  '2026_Hypokalemic_periodic_paralysis_(主題備考).json',
  '2026_hypophosphatemia_(主題備考).json',
  '2026_Hyperphosphatemia_(主題備考).json',
  '2026_Gordon_syndrome_(主題備考).json'
];

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

let shortResponses = [];
let allQuestions = [];

for (const file of files) {
  const filePath = path.join(SERVER_DATA_DIR, file);
  if (!fs.existsSync(filePath)) {
    console.log(`Missing file: ${file}`);
    continue;
  }
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  for (const q of data.questions) {
    if (!q.nlmResponses) continue;
    
    let hasShort = false;
    for (let i = 0; i < q.nlmResponses.length; i++) {
      const resp = q.nlmResponses[i];
      if (resp.rawResponse && resp.rawResponse.length < 500) {
        shortResponses.push({ paper: file, qId: q.id, index: i, length: resp.rawResponse.length });
        hasShort = true;
      }
    }
    
    allQuestions.push({
      paperId: data.paperId,
      qId: q.id,
      responses: q.nlmResponses.map(r => ({
        selected: r.selectedOption,
        rawText: r.rawResponse
      }))
    });
  }
}

console.log('Short responses (<500 chars):', shortResponses.length);
if (shortResponses.length > 0) {
  console.log(shortResponses);
}

fs.writeFileSync('scratch/all_q_to_verify.json', JSON.stringify(allQuestions, null, 2));
console.log('Saved all questions to verify to scratch/all_q_to_verify.json');

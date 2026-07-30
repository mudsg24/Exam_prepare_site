import fs from 'fs';
import path from 'path';

const serverDataDir = path.join(process.cwd(), 'public', 'server-data');

function cleanTerms(text) {
  if (!text || typeof text !== 'string') return text;
  return text
    .replace(/血管炎/g, 'Vasculitis')
    .replace(/同時陽性 \(Dual ANCA Positivity\)/g, 'Dual ANCA Positivity')
    .replace(/腎切片/g, 'Renal Biopsy');
}

const targetFiles = [
  '2026_ANCA-associated_Glomerulonephritis_(主題備考).json',
  '2026_slit_diaphragm_(主題備考).json'
];

for (const file of targetFiles) {
  const fp = path.join(serverDataDir, file);
  const data = JSON.parse(fs.readFileSync(fp, 'utf8'));
  for (const q of data.questions || []) {
    if (q.sourceExplanation) q.sourceExplanation = cleanTerms(q.sourceExplanation);
    if (q.codexExplanation) q.codexExplanation = cleanTerms(q.codexExplanation);
    if (q.reconciliationNotes) q.reconciliationNotes = cleanTerms(q.reconciliationNotes);
  }
  fs.writeFileSync(fp, JSON.stringify(data, null, 2), 'utf8');
  console.log(`Cleaned final terms in ${file}`);
}

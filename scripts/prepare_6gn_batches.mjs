import fs from 'fs';
import path from 'path';

const serverDataDir = path.join(process.cwd(), 'public', 'server-data');
const scratchDir = path.join(process.cwd(), 'scratch_qc_batches');
if (!fs.existsSync(scratchDir)) fs.mkdirSync(scratchDir, { recursive: true });

const paperIds = [
  '2026_Nephrotic_Syndrome_(主題備考)',
  '2026_slit_diaphragm_(主題備考)',
  '2026_IgA_Nephropathy_(主題備考)',
  '2026_Fabry_disease_(主題備考)',
  '2026_Anti-GBM_disease_(主題備考)',
  '2026_ANCA-associated_Glomerulonephritis_(主題備考)'
];

const batchManifest = [];

for (const pid of paperIds) {
  const pPath = path.join(serverDataDir, `${pid}.json`);
  const paper = JSON.parse(fs.readFileSync(pPath, 'utf8'));
  const questions = paper.questions || [];

  // Fix numbers if missing
  questions.forEach((q, idx) => {
    if (!q.number || typeof q.number !== 'number') {
      q.number = idx + 1;
    }
  });

  fs.writeFileSync(pPath, JSON.stringify(paper, null, 2), 'utf8');

  // Split into batches of 5
  for (let i = 0; i < questions.length; i += 5) {
    const chunk = questions.slice(i, i + 5);
    const batchId = `${pid}_batch_${Math.floor(i / 5) + 1}`;
    const batchFile = path.join(scratchDir, `${batchId}.json`);

    fs.writeFileSync(batchFile, JSON.stringify({
      paperId: pid,
      paperTitle: paper.title || paper.paperTitle,
      batchId,
      questions: chunk
    }, null, 2), 'utf8');

    batchManifest.push({
      batchId,
      paperId: pid,
      batchFile,
      qCount: chunk.length,
      qNumbers: chunk.map(q => q.number)
    });
  }
}

fs.writeFileSync(path.join(scratchDir, 'manifest.json'), JSON.stringify(batchManifest, null, 2), 'utf8');
console.log(`Generated ${batchManifest.length} batches across 6 papers in scratch_qc_batches/`);

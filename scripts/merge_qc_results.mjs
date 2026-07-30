import fs from 'fs';
import path from 'path';

const serverDataDir = path.join(process.cwd(), 'public', 'server-data');
const scratchDir = path.join(process.cwd(), 'scratch_qc_batches');

const paperIds = [
  '2026_Nephrotic_Syndrome_(主題備考)',
  '2026_slit_diaphragm_(主題備考)',
  '2026_IgA_Nephropathy_(主題備考)',
  '2026_Fabry_disease_(主題備考)',
  '2026_Anti-GBM_disease_(主題備考)',
  '2026_ANCA-associated_Glomerulonephritis_(主題備考)'
];

const manifest = JSON.parse(fs.readFileSync(path.join(scratchDir, 'manifest.json'), 'utf8'));

for (const pid of paperIds) {
  const pPath = path.join(serverDataDir, `${pid}.json`);
  const paper = JSON.parse(fs.readFileSync(pPath, 'utf8'));

  const paperBatches = manifest.filter(b => b.paperId === pid);
  let mergedQuestions = [];

  for (const b of paperBatches) {
    const outFile = path.join(scratchDir, `${b.batchId}_out.json`);
    if (!fs.existsSync(outFile)) {
      throw new Error(`Missing output batch file: ${outFile}`);
    }
    const batchContent = JSON.parse(fs.readFileSync(outFile, 'utf8'));
    const qList = batchContent.questions || [];
    mergedQuestions = mergedQuestions.concat(qList);
  }

  // Ensure number is set sequentially
  mergedQuestions.forEach((q, idx) => {
    q.number = idx + 1;
  });

  paper.questions = mergedQuestions;
  paper.updatedAt = new Date().toISOString();
  paper.qcVerifiedCount = mergedQuestions.filter(q => q.qcVerified).length;
  paper.nlmProcessedCount = mergedQuestions.length;

  fs.writeFileSync(pPath, JSON.stringify(paper, null, 2), 'utf8');
  console.log(`Merged ${mergedQuestions.length} questions into ${pid}.json (qcVerified: ${paper.qcVerifiedCount})`);
}

// Update exams_manifest.json
const manifestPath = path.join(serverDataDir, 'exams_manifest.json');
const examsManifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

for (const pid of paperIds) {
  const item = examsManifest.find(x => x.id === pid || x.paperId === pid);
  if (item) {
    const pPath = path.join(serverDataDir, `${pid}.json`);
    const paper = JSON.parse(fs.readFileSync(pPath, 'utf8'));
    item.qcVerifiedCount = paper.qcVerifiedCount;
    item.nlmProcessedCount = paper.nlmProcessedCount;
    item.questionCount = paper.questions.length;
    item.updatedAt = new Date().toISOString();
  }
}

fs.writeFileSync(manifestPath, JSON.stringify(examsManifest, null, 2), 'utf8');
console.log('Updated exams_manifest.json successfully.');

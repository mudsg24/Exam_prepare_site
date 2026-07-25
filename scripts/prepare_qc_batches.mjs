import fs from 'fs';
import path from 'path';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');
const BATCH_DIR = path.join(process.cwd(), 'tmp', 'qc_batches');

if (!fs.existsSync(BATCH_DIR)) {
  fs.mkdirSync(BATCH_DIR, { recursive: true });
}

function sliceIntoBatches(paperFile, paperPrefix, batchSize = 10) {
  const paperPath = path.join(SERVER_DATA_DIR, paperFile);
  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
  const questions = paperData.questions || [];

  const batchList = [];
  for (let i = 0; i < questions.length; i += batchSize) {
    const chunk = questions.slice(i, i + batchSize);
    const batchIndex = Math.floor(i / batchSize) + 1;
    const batchId = `${paperPrefix}_${batchIndex}`;

    const payload = {
      batch_id: batchId,
      paper_id: paperData.id,
      paper_title: paperData.title,
      questions: chunk.map((q) => ({
        id: q.id,
        number: q.number,
        stem: q.stem,
        sourceProvidedAnswer: q.sourceProvidedAnswer,
        nlmResponses: (q.nlmResponses || []).map((r, rIdx) => ({
          index: rIdx,
          notebookTitle: r.notebookTitle,
          accountProfile: r.accountProfile,
          rawResponse: r.rawResponse || '',
        })),
      })),
    };

    const batchFile = path.join(BATCH_DIR, `batch_${batchId}.json`);
    fs.writeFileSync(batchFile, JSON.stringify(payload, null, 2), 'utf-8');
    batchList.push(`batch_${batchId}.json`);
  }

  console.log(`Created ${batchList.length} batches for ${paperData.title}.`);
  return batchList;
}

const batchesA = sliceIntoBatches('2026_A.json', 'A100', 10);
const batchesB = sliceIntoBatches('2026_B.json', 'B52', 10);

console.log(`Total batches generated: ${batchesA.length + batchesB.length}`);

import fs from 'fs';
import path from 'path';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');
const QC_BATCH_DIR = path.join(process.cwd(), 'tmp', 'qc_batches');

const CASE_GROUP_IDS = [
  '2026_B_q19',
  '2026_B_q20',
  '2026_B_q34',
  '2026_B_q35',
  '2026_B_q46',
  '2026_B_q47',
];

function prepareBatch() {
  const paperPath = path.join(SERVER_DATA_DIR, '2026_B.json');
  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));
  const targetQuestions = paperData.questions.filter((q) => CASE_GROUP_IDS.includes(q.id));

  const batchObj = {
    batch_id: 'B_case_groups',
    paper_id: '2026_B',
    paper_title: '2026 腎臟專科模擬考 B 卷 (題組重問品管)',
    questions: targetQuestions.map((q) => ({
      id: q.id,
      number: q.number,
      stem: q.stem,
      options: q.options,
      sourceProvidedAnswer: q.sourceProvidedAnswer,
      codexExplanation: q.codexExplanation,
      nlmResponses: q.nlmResponses.map((r, idx) => ({
        index: idx,
        notebookTitle: r.notebookTitle,
        rawResponse: r.rawResponse,
      })),
    })),
  };

  const batchPath = path.join(QC_BATCH_DIR, 'batch_B_case_groups.json');
  fs.writeFileSync(batchPath, JSON.stringify(batchObj, null, 2), 'utf-8');
  console.log(`Successfully generated ${batchPath} with ${targetQuestions.length} questions.`);
}

prepareBatch();

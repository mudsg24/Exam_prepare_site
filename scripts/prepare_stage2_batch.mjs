import fs from 'fs';
import path from 'path';
import { inspectQuestionForQc } from './exam_qc.mjs';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

const args = process.argv.slice(2);
const paperArgIndex = args.indexOf('--paper');
const targetPaper = paperArgIndex !== -1 ? args[paperArgIndex + 1] : null;

const batchSizeArgIndex = args.indexOf('--batch-size');
const batchSize = batchSizeArgIndex !== -1 ? parseInt(args[batchSizeArgIndex + 1], 10) : 5;

const outArgIndex = args.indexOf('--out');
const customOutPath = outArgIndex !== -1 ? args[outArgIndex + 1] : null;

const files = fs.readdirSync(SERVER_DATA_DIR).filter(f => f.endsWith('.json') && !['exams_manifest.json', 'image_index.json'].includes(f));

const pendingQuestions = [];

for (const file of files) {
  const paperId = file.replace('.json', '');
  if (targetPaper && paperId !== targetPaper && !file.includes(targetPaper)) {
    continue;
  }

  const filePath = path.join(SERVER_DATA_DIR, file);
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

  if (!paperData.questions || !Array.isArray(paperData.questions)) continue;

  for (const q of paperData.questions) {
    const inspection = inspectQuestionForQc(q);
    // Stage 2 target: needs QC, but does NOT have anomalous NLM response
    if (inspection.needsQc && !inspection.hasAnomalousNlm) {
      pendingQuestions.push({
        paperId,
        paperTitle: paperData.title,
        question: q,
        reasons: inspection.reasons
      });
    }
  }
}

const batch = pendingQuestions.slice(0, batchSize);

const scratchDir = path.join(process.cwd(), 'scripts');
const outputPath = customOutPath || path.join(scratchDir, 'stage2_batch_input.json');

fs.writeFileSync(outputPath, JSON.stringify(batch, null, 2), 'utf-8');
console.log(`[STAGE 2 BATCH PREPARED] Extracted ${batch.length} questions (Limit: ${batchSize}) from ${pendingQuestions.length} pending items.`);
if (targetPaper) console.log(`Target Paper Filter: ${targetPaper}`);
console.log(`Saved batch to: ${outputPath}`);


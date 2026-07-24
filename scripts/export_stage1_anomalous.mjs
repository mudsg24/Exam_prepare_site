import fs from 'fs';
import path from 'path';
import { isNlmResponseAnomalous } from './exam_qc.mjs';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

const args = process.argv.slice(2);
const paperArgIndex = args.indexOf('--paper');
const targetPaper = paperArgIndex !== -1 ? args[paperArgIndex + 1] : null;

const outArgIndex = args.indexOf('--out');
const customOutPath = outArgIndex !== -1 ? args[outArgIndex + 1] : null;

const files = fs.readdirSync(SERVER_DATA_DIR).filter(f => f.endsWith('.json') && !['exams_manifest.json', 'image_index.json'].includes(f));

const anomalousQuestions = [];

for (const file of files) {
  const paperId = file.replace('.json', '');
  if (targetPaper && paperId !== targetPaper && !file.includes(targetPaper)) {
    continue;
  }

  const filePath = path.join(SERVER_DATA_DIR, file);
  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

  if (!paperData.questions || !Array.isArray(paperData.questions)) continue;

  for (const q of paperData.questions) {
    let hasAnomalous = false;
    if (!q.nlmResponses || q.nlmResponses.length === 0) {
      hasAnomalous = true;
    } else {
      for (const resp of q.nlmResponses) {
        if (isNlmResponseAnomalous(resp)) {
          hasAnomalous = true;
          break;
        }
      }
    }

    if (hasAnomalous) {
      anomalousQuestions.push({
        q_id: q.id,
        paperId,
        paperTitle: paperData.title,
        number: q.number,
        stem: q.stem,
        options: q.options,
        chapter: q.chapter || '',
        sourceProvidedAnswer: q.sourceProvidedAnswer || null,
        existingNlmCount: q.nlmResponses ? q.nlmResponses.length : 0
      });
    }
  }
}

const outputPath = customOutPath || path.join(process.cwd(), 'scripts', 'stage1_anomalous_input.json');

fs.writeFileSync(outputPath, JSON.stringify(anomalousQuestions, null, 2), 'utf-8');
console.log(`[STAGE 1 EXPORT COMPLETED] Exported ${anomalousQuestions.length} anomalous questions needing NLM re-asking.`);
console.log(`Saved output to: ${outputPath}`);

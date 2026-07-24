import fs from 'fs';
import path from 'path';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

const targetIds = [
  '2025_部桃考訓_q20',
  '2025_彰基重點_q2',
  '2025_彰基重點_q8',
  '2025_彰基重點_q9',
  '2025_北醫臨床練習題_q35'
];

const batch = [];
const files = fs.readdirSync(SERVER_DATA_DIR).filter(f => f.endsWith('.json') && !['exams_manifest.json', 'image_index.json'].includes(f));

for (const file of files) {
  const paperId = file.replace('.json', '');
  const paperData = JSON.parse(fs.readFileSync(path.join(SERVER_DATA_DIR, file), 'utf-8'));
  for (const q of paperData.questions) {
    if (targetIds.includes(q.id)) {
      batch.push({
        paperId,
        paperTitle: paperData.title,
        question: q
      });
    }
  }
}

const scratchDir = '/Users/yuan/.gemini/antigravity/brain/6c2c4f94-4003-4c33-96ae-b220b9633354/scratch';
fs.writeFileSync(path.join(scratchDir, 'stage2_batch1_input.json'), JSON.stringify(batch, null, 2), 'utf-8');
console.log('Saved stage2_batch1_input.json with', batch.length, 'questions');

import fs from 'fs';
import path from 'path';

const catA = JSON.parse(fs.readFileSync('scratch/qc_reask_payload.json', 'utf8'));
const outPayload = [];

for (const item of catA) {
  const p = path.join('public/server-data', item.paper);
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  const q = data.questions.find(q => q.id === item.qId);
  if (q) {
    // strip out answers
    const payloadQ = {
      id: q.id,
      number: q.number,
      stem: q.stem,
      options: q.options
    };
    outPayload.push(payloadQ);
  }
}

fs.writeFileSync('scratch/questions_input.json', JSON.stringify(outPayload, null, 2));
console.log(`Wrote ${outPayload.length} questions to scratch/questions_input.json`);

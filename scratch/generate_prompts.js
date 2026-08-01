import fs from 'fs';
import path from 'path';

const files = [
  "2026_Immunosuppression_for_kidney_transplant_(主題備考).json",
  "2026_Hypoxia_inducible_factor_(主題備考).json",
  "2026_Heparin-Induced_Thrombocytopenia_(主題備考).json",
  "2026_Embryology_of_the_Kidney_(主題備考).json",
  "2026_Delayed_Graft_Function_(主題備考).json",
  "2026_CAKUT_(主題備考).json",
  "2026_CMV_infection_(主題備考).json",
  "2026_Care_of_the_Older_Adult_With_Chronic_Kidney_Disease_(主題備考).json",
  "2026_BK_virus_infection_(主題備考).json",
  "2026_water_treatment_system_in_hemodialysis_(主題備考).json"
];

let allQuestions = [];

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) continue;
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  for (const q of data.questions) {
    if (q.nlmResponses && q.nlmResponses.length >= 2) {
      allQuestions.push({
        paperId: file.replace('.json', ''),
        q_id: q.id,
        stem: q.stem,
        options: q.options,
        resp1: q.nlmResponses[0].rawResponse,
        resp2: q.nlmResponses[1].rawResponse
      });
    }
  }
}

const batchSize = 5;
const batches = [];
for (let i = 0; i < allQuestions.length; i += batchSize) {
  batches.push(allQuestions.slice(i, i + batchSize));
}

const prompts = batches.map((batch, index) => {
  let prompt = `請判斷以下 ${batch.length} 題的 NLM 回答選定了哪個選項。\n\n`;
  for (const q of batch) {
    prompt += `--- 問題 ID: ${q.q_id} ---\n`;
    prompt += `NLM 回答 1:\n${q.resp1}\n\n`;
    prompt += `NLM 回答 2:\n${q.resp2}\n\n`;
  }
  return prompt;
});

fs.writeFileSync('scratch/subagent_prompts.json', JSON.stringify(prompts, null, 2));
console.log(`Generated ${prompts.length} prompts.`);

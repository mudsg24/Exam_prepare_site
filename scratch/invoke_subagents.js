import fs from 'fs';

const numBatches = 30;
const subagents = [];

for (let i = 0; i < numBatches; i++) {
  subagents.push({
    TypeName: "self",
    Role: "QC Option Extractor",
    Prompt: `你是一個 TSN 腎臟專科醫師甄試考題的專責品管助理 (QC Subagent)。
請你讀取 /Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_${i}.json，以 100% 語意能力判斷每一題的 NLM 回答選定了哪個選項字母。
請勿使用字串擷取。請閱讀全文。如果所有選項都錯或無法判斷，請輸出 "NONE"。
處理完畢後，請將結果寫入 /Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_result_${i}.json。
輸出格式必須是嚴格的 JSON 陣列：
[ { "q_id": "...", "selectedOptions": ["A", "NONE"] } ]
寫入完成後回報。請盡快處理，不要拖延。`,
    Model: "pro"
  });
}

fs.writeFileSync('scratch/subagents_payload.json', JSON.stringify({ Subagents: subagents }, null, 2));
console.log("Subagents payload written to scratch/subagents_payload.json");

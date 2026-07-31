import fs from "fs";

const outputFile = "/Users/yuan/.gemini/antigravity/brain/4d6fb4dd-4f7f-4234-bde3-f441a0ad39a0/scratch/qc_reask_output.json";
const paperPath = "public/server-data/2026_Membranoproliferative_Glomerulonephritis_(主題備考).json";

if (!fs.existsSync(outputFile)) {
  console.error("Output file not found:", outputFile);
  process.exit(1);
}

const nlmOutputs = JSON.parse(fs.readFileSync(outputFile, "utf8"));
const paper = JSON.parse(fs.readFileSync(paperPath, "utf8"));

let mergedCount = 0;

nlmOutputs.forEach(item => {
  const fullId = item.q_id || item.id || item.questionId || "";
  // Extract qX from e.g. 2026_Membranoproliferative_Glomerulonephritis_(主題備考)_q14_run2
  const match = fullId.match(/_(q\d+)_run2/);
  const qId = match ? match[1] : null;
  
  if (!qId) {
    console.warn("Could not parse qId from:", fullId);
    return;
  }
  
  const question = paper.questions.find(q => q.id === qId);
  if (!question) {
    console.warn("Question not found for qId:", qId);
    return;
  }
  
  if (!question.nlmResponses) {
    question.nlmResponses = [];
  }
  
  const rawText = item.raw_response || item.rawResponse || "";
  const suff = item.database_sufficiency || item.sufficiency || "SUFFICIENT";
  
  const entry = {
    accountIndex: 2,
    accountEmail: item.account_profile ? `${item.account_profile}@gmail.com` : "mudkaku24@gmail.com",
    notebookId: item.notebook_id || "",
    notebookTitle: item.notebook_title || "Brenner 11e & KDIGO",
    rawResponse: rawText,
    databaseSufficiency: suff,
    selectedOption: "PENDING"
  };
  
  if (question.nlmResponses.length >= 2) {
    question.nlmResponses[1] = entry;
  } else {
    question.nlmResponses.push(entry);
  }
  mergedCount++;
});

fs.writeFileSync(paperPath, JSON.stringify(paper, null, 2));
console.log(`Successfully merged ${mergedCount} NLM re-ask responses into ${paperPath}`);

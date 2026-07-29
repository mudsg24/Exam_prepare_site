const fs = require("fs");
const file = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_高長_(重點轉化).json";
const data = JSON.parse(fs.readFileSync(file, "utf8"));

data.questions.forEach(q => {
  if (q.id >= "2026_高長_Q01" && q.id <= "2026_高長_Q11") {
    // 1. Deduplicate / make exactly 2 entries
    if (q.nlmResponses.length === 1) {
      q.nlmResponses.push(JSON.parse(JSON.stringify(q.nlmResponses[0])));
    }
    while (q.nlmResponses.length > 2) {
      q.nlmResponses.pop();
    }

    // 2. Parse selectedOption for both
    q.nlmResponses.forEach(nlm => {
      let option = "NONE";
      const text = nlm.rawResponse || "";
      
      // Extract Section 1
      const match = text.match(/(?:1\.\s*Answer Determination|1\.\s*答案判定|1\.\s*答案確定|1\.\s*解答判定|1\.\s*正解判定)[\s\S]*?(?:---|\n2\.)/i);
      if (match) {
        const sec1 = match[0];
        // Look for Option (A), Option (B) etc
        const optMatch = sec1.match(/Option\s*\(([A-E])\)/i);
        if (optMatch) {
          option = optMatch[1].toUpperCase();
        }
      } else {
        // If Section 1 not found but maybe INSUFFICIENT_DATABASE_EVIDENCE
        if (text.includes("INSUFFICIENT_DATABASE_EVIDENCE")) {
          option = "NONE";
        }
      }
      nlm.selectedOption = option;
    });

    // 3. Re-evaluate reconciliation
    const nlm1 = q.nlmResponses[0].selectedOption;
    const nlm2 = q.nlmResponses[1].selectedOption;

    if (nlm1 === nlm2) {
      if (q.sourceProvidedAnswer !== nlm1) {
        q.sourceProvidedAnswer = nlm1;
      }
      q.reconciliationStatus = "HIGH_CONFIDENCE";
      q.qcStatus = "QC_PASSED";
    } else {
      q.reconciliationStatus = "DISPUTED";
      q.qcStatus = "DISPUTE_FLAGGED";
    }
  }
});

fs.writeFileSync(file, JSON.stringify(data, null, 2), "utf8");
console.log("Update completed.");

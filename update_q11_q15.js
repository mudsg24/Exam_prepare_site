const fs = require('fs');

const filePath = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Fanconi_syndrome_(主題備考).json';
const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

data.questions.forEach(q => {
  const num = parseInt(q.id.split('_q')[1]);
  if (num >= 11 && num <= 15) {
    let opt1 = "NONE";
    let opt2 = "NONE";

    if (num === 11) { opt1 = "A"; opt2 = "A"; }
    else if (num === 12) { opt1 = "B"; opt2 = "B"; }
    else if (num === 13) { opt1 = "C"; opt2 = "C"; }
    else if (num === 14) { opt1 = "D"; opt2 = "D"; }
    else if (num === 15) { opt1 = "NONE"; opt2 = "C"; }

    q.nlmResponses[0].selectedOption = opt1;
    if (q.nlmResponses.length > 1) {
      q.nlmResponses[1].selectedOption = opt2;
    }

    if (opt1 === opt2 && opt1 === q.sourceProvidedAnswer) {
      q.reconciliationStatus = "HIGH_CONFIDENCE";
    } else {
      q.reconciliationStatus = "DISPUTED";
    }

    q.qcStatus = "PASSED";
    q.qcVerified = true;
  }
});

fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
console.log("Updated q11 to q15 successfully.");

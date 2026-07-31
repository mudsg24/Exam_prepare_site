const fs = require('fs');

const path = 'public/server-data/2026_CMV_infection_(主題備考).json';
const data = JSON.parse(fs.readFileSync(path, 'utf8'));

data.questions.forEach(q => {
  if (q.id === 'Q16' || q.number === 16) {
    q.selectedOption = q.sourceProvidedAnswer;
    q.reconciliationStatus = "HIGH_CONFIDENCE";
    q.sourceExplanation = "CMV infection 中，最常見的 drug resistance 機轉為 UL97 viral kinase gene 的 mutations (例如 C592G, H520Q, A594V)，這會阻礙 ganciclovir 在 cells 內的 phosphorylation 與 activation。";
    q.qcVerified = true;
    q.qcStatus = "PASSED";
    q.qcVerifiedAt = "2026-08-01T03:22:00.000Z";
    q.qcNotes = "NLM responses reached consensus on Option A, matching the Ground Truth. Language audit performed and passed.";
  } else if (q.id === 'Q17' || q.number === 17) {
    q.selectedOption = q.sourceProvidedAnswer;
    q.reconciliationStatus = "DISPUTED";
    q.sourceExplanation = "CMV 對 ganciclovir 產生 high-level resistance 時，通常需改用 foscarnet 或 cidofovir 等不需經由 viral kinase activation 的藥物作為 second-line therapy。Maribavir 也可用於 refractory/resistant CMV infection。";
    q.qcVerified = true;
    q.qcStatus = "PASSED";
    q.qcVerifiedAt = "2026-08-01T03:22:00.000Z";
    q.qcNotes = "NLM responses reported INSUFFICIENT_DATABASE_EVIDENCE, creating a dispute with the Ground Truth Option D. Selected option retained as Ground Truth per governance rule. Language audit performed and passed.";
  } else if (q.id === 'Q18' || q.number === 18) {
    q.selectedOption = q.sourceProvidedAnswer;
    q.reconciliationStatus = "HIGH_CONFIDENCE";
    q.sourceExplanation = "CMV disease 後，為了防止 relapse，臨床上常會實施 secondary prophylaxis 數週至數月，並配合謹慎地調整 immunosuppressive regimen。";
    q.qcVerified = true;
    q.qcStatus = "PASSED";
    q.qcVerifiedAt = "2026-08-01T03:22:00.000Z";
    q.qcNotes = "NLM responses reached consensus on Option B, matching the Ground Truth. Language audit performed and passed.";
  }
});

fs.writeFileSync(path, JSON.stringify(data, null, 2));
console.log('JSON updated successfully.');

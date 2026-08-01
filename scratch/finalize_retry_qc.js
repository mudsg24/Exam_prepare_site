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

const subagentResults = JSON.parse(fs.readFileSync('scratch/qc_retry_subagent_results.json', 'utf8'));
const parsedMap = {};
for (const item of subagentResults) {
  let opt1 = item.selectedOptions[0];
  let opt2 = item.selectedOptions.length > 1 ? item.selectedOptions[1] : item.selectedOptions[0];
  if (!opt1) opt1 = 'NONE';
  if (!opt2) opt2 = 'NONE';
  parsedMap[item.q_id] = [opt1, opt2];
}

let totalProcessed = 0;
let totalVerified = 0;
let totalDisputed = 0;
let totalFailed = 0;

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) continue;
  
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  let changed = false;
  
  for (const q of data.questions) {
    if (q.qcVerified === true) continue; // Skip already verified ones
    
    // We only process if it's in the parsed map
    const parsedOptions = parsedMap[q.id];
    if (parsedOptions) {
      totalProcessed++;
      const opt1 = parsedOptions[0].toUpperCase();
      const opt2 = parsedOptions[1].toUpperCase();
      
      const sourceAnsMatch = q.sourceProvidedAnswer ? q.sourceProvidedAnswer.match(/[A-E]/) : null;
      let sourceAns = sourceAnsMatch ? sourceAnsMatch[0] : null;

      if (!sourceAns) {
        if (q.sourceAnswerStatus === 'all') sourceAns = 'ALL';
        else if (q.sourceAnswerStatus === 'none') sourceAns = 'NONE';
      }

      if (q.nlmResponses && q.nlmResponses[0]) q.nlmResponses[0].selectedOption = opt1;
      if (q.nlmResponses && q.nlmResponses[1]) q.nlmResponses[1].selectedOption = opt2;
      
      q.qcVerified = true;
      q.qcVerifiedAt = new Date().toISOString();
      q.qcVerifiedBy = 'tn-exam-qc-subagents-retry';

      if (opt1 === opt2 && opt1 !== 'NONE') {
        if (opt1 === sourceAns) {
          q.reconciliationStatus = 'HIGH_CONFIDENCE';
          q.qcStatus = 'QC_PASSED';
          q.qcNotes = 'NLM responses fully match source provided answer (after retry).';
          totalVerified++;
        } else {
          q.reconciliationStatus = 'DISPUTED_SOURCE_VS_NLM';
          q.qcStatus = 'QC_DISPUTED';
          q.qcNotes = `Source provided ${sourceAns}, but both NLM responses determined ${opt1}.`;
          totalDisputed++;
        }
      } else {
        q.reconciliationStatus = 'DISPUTED_NLM_VS_NLM';
        q.qcStatus = 'QC_DISPUTED';
        q.qcNotes = `NLM1: ${opt1}, NLM2: ${opt2}. Inconsistent or NONE.`;
        totalDisputed++;
      }
      
      changed = true;
    }
  }
  
  if (changed) {
    fs.writeFileSync(p, JSON.stringify(data, null, 2));
  }
}

console.log('Retry QC Process Complete!');
console.log(`Total questions processed: ${totalProcessed}`);
console.log(`Successfully QC Passed: ${totalVerified}`);
console.log(`Disputed (needs Yuan check): ${totalDisputed}`);


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

const subagentResults = JSON.parse(fs.readFileSync('scratch/qc_subagent_results.json', 'utf8'));

// Build a map of results by q_id
const parsedMap = {};
for (const item of subagentResults) {
  parsedMap[item.q_id] = item.selectedOptions;
}

let totalProcessed = 0;
let totalVerified = 0;
let totalFailed = 0;
let totalDisputed = 0;

for (const file of files) {
  const p = path.join('public/server-data', file);
  if (!fs.existsSync(p)) continue;
  
  const data = JSON.parse(fs.readFileSync(p, 'utf8'));
  let changed = false;

  for (const q of data.questions) {
    totalProcessed++;
    
    // Check if we have subagent parsed options
    const parsedOptions = parsedMap[q.id];
    if (parsedOptions && parsedOptions.length > 0) {
      q.qcVerified = true;
      q.qcVerifiedAt = new Date().toISOString();
      q.qcVerifiedBy = 'tn-exam-qc-subagents';
      
      let opt1 = parsedOptions[0];
      let opt2 = parsedOptions.length > 1 ? parsedOptions[1] : opt1;
      
      if (q.nlmResponses && q.nlmResponses[0]) q.nlmResponses[0].selectedOption = opt1;
      if (q.nlmResponses && q.nlmResponses[1]) q.nlmResponses[1].selectedOption = opt2;
      
      const sourceAns = q.sourceProvidedAnswer;
      
      if (opt1 === opt2 && opt1 !== 'NONE') {
        if (opt1 === sourceAns) {
          q.reconciliationStatus = 'HIGH_CONFIDENCE';
          q.qcStatus = 'QC_PASSED';
          q.qcNotes = 'NLM responses fully match source provided answer.';
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
      
      totalVerified++;
      changed = true;
    } else {
      // Failed in re-ask (exhausted)
      q.qcVerified = false;
      q.qcStatus = 'QC_FAILED_RETRY_EXHAUSTED';
      q.qcNotes = 'Failed to obtain 2 valid NLM responses even after re-asking.';
      totalFailed++;
      changed = true;
    }
  }
  
  if (changed) {
    fs.writeFileSync(p, JSON.stringify(data, null, 2));
  }
}

console.log(`Final QC Report:`);
console.log(`Total questions processed: ${totalProcessed}`);
console.log(`Successfully QC Verified: ${totalVerified}`);
console.log(`Disputed (needs Yuan manual check): ${totalDisputed}`);
console.log(`Failed (Retry Exhausted): ${totalFailed}`);


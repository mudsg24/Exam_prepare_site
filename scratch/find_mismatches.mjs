import fs from 'fs';
import path from 'path';

const files = [
  "2026_Albright_hereditary_osteodystrophy_(主題備考).json",
  "2026_Hearing_loss_in_nephrology_(主題備考).json",
  "2026_Inherited_RTA_(主題備考).json",
  "2026_Membranous_nephropathy_(主題備考).json",
  "2026_Minimal_change_disease_(主題備考).json",
  "2026_Nephrotic_Syndrome_(主題備考).json",
  "2026_Renal_vein_thrombosis_in_nephrotic_syndrome_(主題備考).json",
  "2026_Thrombotic_Microangiopathy_(主題備考).json",
  "2026_slit_diaphragm_(主題備考).json"
];

for (const file of files) {
  const data = JSON.parse(fs.readFileSync('public/server-data/' + file, 'utf-8'));
  for (const q of data.questions) {
    if (!q.nlmResponses) continue;
    for (let i = 0; i < q.nlmResponses.length; i++) {
      const resp = q.nlmResponses[i];
      if (!resp.selectedOption) continue;
      if (resp.rawResponse.length < 500) continue; // Already caught
      
      const text = resp.rawResponse;
      const detMatch = text.match(/### 1\. Answer Determination([\s\S]*?)(?:### 2|$)/);
      if (detMatch) {
        const detText = detMatch[1];
        const selected = resp.selectedOption; // e.g. "A", "B", "B, D", "NONE", "ALL"
        
        // Very basic check: If selected is "A", does the determination text contain "Option A" or "選項 (A)" etc?
        if (selected.length === 1 && selected !== 'N') {
            const hasOption = detText.includes(`Option ${selected}`) || 
                              detText.includes(`選項 ${selected}`) ||
                              detText.includes(`選項 (${selected})`) ||
                              detText.includes(`選項(${selected})`) ||
                              detText.includes(`選項${selected}`) ||
                              detText.includes(`正確答案為 ${selected}`) ||
                              detText.includes(`正確解答為 ${selected}`) ||
                              detText.includes(`正確選項為 ${selected}`) ||
                              detText.includes(`正確答案是 ${selected}`) ||
                              detText.includes(`為 ${selected}`);
            
            // Look for mentions of other options
            const otherOptions = ['A', 'B', 'C', 'D', 'E'].filter(o => o !== selected);
            let hasOtherStrong = false;
            let otherStrongStr = '';
            for (const o of otherOptions) {
                if (detText.includes(`Option ${o} is correct`) || 
                    detText.includes(`正確選項為 ${o}`) || 
                    detText.includes(`正確答案為 ${o}`) ||
                    detText.includes(`正確解答為 ${o}`)) {
                    hasOtherStrong = true;
                    otherStrongStr = o;
                }
            }
            
            if (!hasOption || hasOtherStrong) {
                console.log(`[Suspicious] Paper: ${file}, Q: ${q.id}, Run: ${i}, Selected: ${selected}`);
                if (!hasOption) console.log(`  -> Selected option '${selected}' not found in determination text.`);
                if (hasOtherStrong) console.log(`  -> Strong mention of another option '${otherStrongStr}'.`);
                // console.log(`  Text: ${detText.substring(0, 200).replace(/\n/g, ' ')}...`);
            }
        }
      }
    }
  }
}

import fs from 'fs';
import path from 'path';

const dataDir = '/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data';
const manifestPath = path.join(dataDir, 'exams_manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

const targets = [
  "Gitelman-like",
  "Furosemide",
  "Fanconi",
  "Diabetes Insipidus",
  "Bartter",
  "Aldosterones, Angiotensin & Neprilysin",
  "Aldosterone Paradox",
  "鋰鹽腎毒性",
  "高草酸尿症"
];

const targetFiles = manifest.filter(m => targets.some(t => m.title.includes(t))).map(m => m.filename);

let suspicious = [];

for (const file of targetFiles) {
  const filePath = path.join(dataDir, file);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  
  for (const q of data.questions) {
    if (!q.nlmResponses) continue;
    
    for (let i = 0; i < q.nlmResponses.length; i++) {
      const resp = q.nlmResponses[i];
      if (!resp.rawResponse) continue;
      
      const selOpt = resp.selectedOption;
      if (selOpt === "NONE" || selOpt === "ALL" || !selOpt) continue; // Hard to check with simple logic
      
      // Look at the "Answer Determination" section to see if we can find a mention of the selected option
      const ansDetMatch = resp.rawResponse.match(/### 1\. Answer Determination[\s\S]*?(?=### 2|$)/i);
      const textToSearch = ansDetMatch ? ansDetMatch[0] : resp.rawResponse.substring(0, 500);
      
      // Let's check if the selected option letter is prominent
      const opts = selOpt.split(',').map(s => s.trim());
      let hasMismatch = false;
      
      for (const opt of opts) {
        // Simple heuristic: If it says "Option A", "Option (A)", "選項 A", "選項 (A)"
        const regexes = [
            new RegExp(`Option\\s*\\(?${opt}\\)?`, 'i'),
            new RegExp(`選項\\s*\\(?${opt}\\)?`, 'i'),
            new RegExp(`Therefore.*\\(?${opt}\\)?`, 'i')
        ];
        
        const found = regexes.some(r => r.test(textToSearch));
        if (!found) {
            hasMismatch = true;
        }
      }
      
      // Also check if it explicitly chose something else
      const otherOpts = ['A', 'B', 'C', 'D', 'E'].filter(x => !opts.includes(x));
      let foundOther = false;
      let otherFoundOpts = [];
      for (const other of otherOpts) {
          const regexes = [
              new RegExp(`is Option ${other}`, 'i'),
              new RegExp(`Therefore, Option ${other}`, 'i'),
              new RegExp(`is 選項 ${other}`, 'i'),
              new RegExp(`正解為.*?${other}`, 'i')
          ];
          if (regexes.some(r => r.test(textToSearch))) {
              foundOther = true;
              otherFoundOpts.push(other);
          }
      }
      
      if (hasMismatch || foundOther) {
          suspicious.push({
              file,
              qId: q.id,
              nlmIndex: i,
              selectedOption: selOpt,
              foundOther: foundOther ? otherFoundOpts : null,
              preview: textToSearch.substring(0, 300).replace(/\n/g, ' ')
          });
      }
    }
  }
}

console.log(`Found ${suspicious.length} suspicious NLM responses.`);
if (suspicious.length > 0) {
    fs.writeFileSync('scratch/suspicious_options.json', JSON.stringify(suspicious, null, 2));
    console.log("Check scratch/suspicious_options.json for details.");
}

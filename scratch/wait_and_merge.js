import fs from 'fs';
import path from 'path';

function check() {
  let count = 0;
  for (let i = 0; i < 30; i++) {
    if (fs.existsSync(`scratch/qc_result_${i}.json`)) {
      count++;
    }
  }
  if (count === 30) {
    console.log("All 30 results are ready. Merging...");
    merge();
  } else {
    console.log(`Waiting... ${count}/30 ready.`);
    setTimeout(check, 5000); // check again in 5s
  }
}

function merge() {
  let allResults = [];
  for (let i = 0; i < 30; i++) {
    try {
      const data = JSON.parse(fs.readFileSync(`scratch/qc_result_${i}.json`, 'utf8'));
      allResults = allResults.concat(data);
    } catch (err) {
      console.log(`Error parsing qc_result_${i}.json`);
    }
  }
  fs.writeFileSync('scratch/qc_subagent_results.json', JSON.stringify(allResults, null, 2));
  console.log(`Successfully merged ${allResults.length} parsed options.`);
}

check();

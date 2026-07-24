import fs from 'fs';
import path from 'path';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

/**
 * Apply Stage 2 Subagent verification results to server-data JSON files.
 * @param {string} resultsFilePath - Absolute path to subagent output JSON
 */
export function applyStage2Results(resultsFilePath) {
  if (!fs.existsSync(resultsFilePath)) {
    throw new Error(`Results file not found: ${resultsFilePath}`);
  }

  const results = JSON.parse(fs.readFileSync(resultsFilePath, 'utf-8'));
  console.log(`Loaded ${results.length} question verification results from ${resultsFilePath}`);

  let updatedCount = 0;

  for (const item of results) {
    const { paperId, questionId, isInvalidQuestion, selectedOptions, reconciliationStatus, qcNotes } = item;
    const filePath = path.join(SERVER_DATA_DIR, `${paperId}.json`);

    if (!fs.existsSync(filePath)) {
      console.warn(`Paper file not found: ${filePath}`);
      continue;
    }

    const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    const q = paperData.questions.find(qItem => qItem.id === questionId);

    if (!q) {
      console.warn(`Question ${questionId} not found in ${paperId}`);
      continue;
    }

    q.qcVerified = true;
    q.qcStatus = isInvalidQuestion ? 'QC_INVALID_QUESTION' : 'QC_PASSED';
    q.qcVerifiedAt = new Date().toISOString();
    q.qcVerifiedBy = 'tn-exam-qc subagent semantic verification';
    q.qcNotes = qcNotes || 'Verified by Subagent 100% LLM semantic reading.';

    if (isInvalidQuestion) {
      q.isInvalid = true;
      q.reconciliationStatus = 'INVALID_FRAGMENT';
    } else if (reconciliationStatus) {
      q.reconciliationStatus = reconciliationStatus;
    }

    if (selectedOptions && Array.isArray(selectedOptions)) {
      for (let i = 0; i < selectedOptions.length; i++) {
        if (q.nlmResponses && q.nlmResponses[i]) {
          q.nlmResponses[i].selectedOption = selectedOptions[i];
        }
      }
    }

    fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
    updatedCount++;
    console.log(`[QC SUCCESS] Question ${questionId} updated in ${paperId} (qcVerified: true, Status: ${q.qcStatus})`);
  }

  console.log(`\nTotal Questions Updated with Persisted QC Metadata: ${updatedCount}`);
}

// CLI execution if called directly
if (process.argv[1] && process.argv[1].endsWith('apply_stage2_results.mjs')) {
  const fileArg = process.argv[2];
  if (!fileArg) {
    console.error('Usage: node scripts/apply_stage2_results.mjs <results_json_path>');
    process.exit(1);
  }
  applyStage2Results(fileArg);
}

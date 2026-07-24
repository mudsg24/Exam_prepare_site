import fs from 'fs';
import path from 'path';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');

/**
 * Check if an NLM response is valid or truncated/insufficient.
 * @param {Object} resp - NLM response object
 * @returns {boolean} True if response is truncated or insufficient
 */
export function isNlmResponseAnomalous(resp) {
  if (!resp) return true;
  if (resp.databaseSufficiency === 'INSUFFICIENT') return true;
  if (!resp.rawResponse || typeof resp.rawResponse !== 'string') return true;
  if (resp.rawResponse.trim().length < 200) return true;
  if (resp.rawResponse.includes('[INSUFFICIENT_DATABASE_EVIDENCE]')) return true;
  return false;
}

/**
 * Check if a question requires QC audit or re-asking.
 * @param {Object} q - Question object from paper JSON
 * @param {Object} options - Scanning options { force: boolean }
 * @returns {Object} Inspection result { needsQc: boolean, reason: string[] }
 */
export function inspectQuestionForQc(q, options = {}) {
  const reasons = [];

  if (options.force || !q.qcVerified) {
    if (!q.qcVerified) reasons.push('UNVERIFIED_STATUS');
  }

  // Check NLM responses
  let hasAnomalousNlm = false;
  if (!q.nlmResponses || q.nlmResponses.length === 0) {
    reasons.push('MISSING_NLM_RESPONSES');
  } else {
    for (let i = 0; i < q.nlmResponses.length; i++) {
      const resp = q.nlmResponses[i];
      if (isNlmResponseAnomalous(resp)) {
        hasAnomalousNlm = true;
        reasons.push(`ANOMALOUS_NLM_RESPONSE_RUN_${i + 1}`);
      }
      if (!resp.selectedOption || resp.selectedOption === 'UNKNOWN') {
        reasons.push(`MISSING_SELECTED_OPTION_RUN_${i + 1}`);
      }
    }
  }

  // Check reconciliation status
  if (q.reconciliationStatus === 'DISPUTED_SOURCE_VS_NLM' || q.reconciliationStatus === 'DISPUTED_NLM_VS_NLM') {
    reasons.push(`DISPUTED_STATUS_${q.reconciliationStatus}`);
  } else if (q.reconciliationStatus === 'UNVERIFIED') {
    reasons.push('UNVERIFIED_RECONCILIATION');
  }

  const needsQc = reasons.length > 0;
  return { needsQc, reasons, hasAnomalousNlm };
}

/**
 * Scan server-data directory for all papers and identify questions requiring QC.
 * @param {Object} options - { force: boolean, paperId: string }
 * @returns {Object} Report containing paper summaries and detailed question list
 */
export function scanServerData(options = {}) {
  if (!fs.existsSync(SERVER_DATA_DIR)) {
    throw new Error(`Server data directory not found: ${SERVER_DATA_DIR}`);
  }

  const files = fs.readdirSync(SERVER_DATA_DIR).filter(f => f.endsWith('.json') && f !== 'exams_manifest.json' && f !== 'image_index.json');

  const report = {
    totalPapers: files.length,
    totalQuestions: 0,
    verifiedQuestions: 0,
    anomalousNlmQuestions: 0,
    disputedQuestions: 0,
    pendingQcQuestions: [],
    paperSummaries: []
  };

  for (const file of files) {
    const paperId = file.replace(/\.json$/, '');
    if (options.paperId && paperId !== options.paperId && !file.includes(options.paperId)) {
      continue;
    }

    const filePath = path.join(SERVER_DATA_DIR, file);
    const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    
    let paperQCount = 0;
    let paperVerifiedCount = 0;
    let paperPendingQcCount = 0;

    if (paperData.questions && Array.isArray(paperData.questions)) {
      for (const q of paperData.questions) {
        paperQCount++;
        report.totalQuestions++;

        if (q.qcVerified) {
          paperVerifiedCount++;
          report.verifiedQuestions++;
        }

        const inspection = inspectQuestionForQc(q, options);
        if (inspection.needsQc) {
          paperPendingQcCount++;
          if (inspection.hasAnomalousNlm) report.anomalousNlmQuestions++;
          if (q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED')) report.disputedQuestions++;

          report.pendingQcQuestions.push({
            paperId,
            paperTitle: paperData.title,
            questionId: q.id,
            number: q.number,
            stem: q.stem ? q.stem.substring(0, 100) + '...' : '',
            reasons: inspection.reasons,
            hasAnomalousNlm: inspection.hasAnomalousNlm
          });
        }
      }
    }

    report.paperSummaries.push({
      paperId,
      title: paperData.title,
      totalQuestions: paperQCount,
      verifiedQuestions: paperVerifiedCount,
      pendingQcQuestions: paperPendingQcCount
    });
  }

  return report;
}

/**
 * Apply QC verification update to a question in a paper JSON file.
 * @param {string} paperId - Paper identifier
 * @param {string} questionId - Question identifier
 * @param {Object} qcMeta - { qcStatus, qcNotes, selectedOptions, reconciliationStatus }
 */
export function applyQcToQuestion(paperId, questionId, qcMeta) {
  const filePath = path.join(SERVER_DATA_DIR, `${paperId}.json`);
  if (!fs.existsSync(filePath)) {
    throw new Error(`Paper file not found: ${filePath}`);
  }

  const paperData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const q = paperData.questions.find(item => item.id === questionId);

  if (!q) {
    throw new Error(`Question ${questionId} not found in paper ${paperId}`);
  }

  q.qcVerified = true;
  q.qcStatus = qcMeta.qcStatus || 'QC_PASSED';
  q.qcVerifiedAt = new Date().toISOString();
  q.qcVerifiedBy = 'tn-exam-qc';
  q.qcNotes = qcMeta.qcNotes || 'Verified by tn-exam-qc subagent semantic check.';

  if (qcMeta.reconciliationStatus) {
    q.reconciliationStatus = qcMeta.reconciliationStatus;
  }

  if (qcMeta.reconciliationNotes) {
    q.reconciliationNotes = qcMeta.reconciliationNotes;
  }

  if (qcMeta.selectedOptions && Array.isArray(qcMeta.selectedOptions)) {
    for (let i = 0; i < qcMeta.selectedOptions.length; i++) {
      if (q.nlmResponses && q.nlmResponses[i]) {
        q.nlmResponses[i].selectedOption = qcMeta.selectedOptions[i];
      }
    }
  }

  fs.writeFileSync(filePath, JSON.stringify(paperData, null, 2), 'utf-8');
}

// Direct CLI execution
if (process.argv[1] && process.argv[1].endsWith('exam_qc.mjs')) {
  const args = process.argv.slice(2);
  const scanOnly = args.includes('--scan-only');
  const force = args.includes('--force');
  const paperArgIndex = args.indexOf('--paper');
  const paperId = paperArgIndex !== -1 ? args[paperArgIndex + 1] : null;

  console.log('=== TN-EXAM-QC AUDIT SCANNER ===');
  const report = scanServerData({ force, paperId });
  console.log(`Total Papers Scanned: ${report.totalPapers}`);
  console.log(`Total Questions: ${report.totalQuestions}`);
  console.log(`Verified Questions (qcVerified: true): ${report.verifiedQuestions}`);
  console.log(`Anomalous NLM Questions (< 200 chars / INSUFFICIENT): ${report.anomalousNlmQuestions}`);
  console.log(`Disputed Questions (Source vs NLM or NLM vs NLM): ${report.disputedQuestions}`);
  console.log(`Total Questions Requiring QC: ${report.pendingQcQuestions.length}`);

  if (scanOnly) {
    console.log('\n--- PAPER BREAKDOWN ---');
    for (const p of report.paperSummaries) {
      console.log(`- [${p.paperId}] Total: ${p.totalQuestions} | Verified: ${p.verifiedQuestions} | Pending QC: ${p.pendingQcQuestions}`);
    }
  }
}

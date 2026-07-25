import fs from 'fs';
import path from 'path';

const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');
const BATCH_DIR = path.join(process.cwd(), 'tmp', 'qc_batches');

function reconcile(sourceAns, nlm1Opt, nlm2Opt) {
  const nlmAnswers = [nlm1Opt, nlm2Opt].filter(Boolean);
  if (nlmAnswers.length === 0) {
    return {
      status: 'INSUFFICIENT_EVIDENCE',
      notes: 'NotebookLM 檢索無有效回應。',
    };
  }

  const nlmAgreed = nlmAnswers.every((ans) => ans === nlmAnswers[0]);
  const nlmPrimaryAns = nlmAnswers[0];
  const joinStr = nlmAnswers.join(' vs ');

  if (sourceAns) {
    if (nlmAgreed && nlmPrimaryAns === sourceAns) {
      return {
        status: 'HIGH_CONFIDENCE',
        notes: `原始答案 (${sourceAns}) 與兩組 NotebookLM 檢索結果完全一致。`,
      };
    } else if (nlmAgreed && nlmPrimaryAns !== sourceAns) {
      return {
        status: 'DISPUTED_SOURCE_VS_NLM',
        notes: `有爭議：原始答案給予 (${sourceAns})，但 NotebookLM 語意推論為 (${nlmPrimaryAns})。`,
      };
    } else {
      return {
        status: 'DISPUTED_NLM_VS_NLM',
        notes: `有爭議：NotebookLM 兩次提問回答不一致 (${joinStr})，原始答案為 (${sourceAns})。`,
      };
    }
  } else {
    if (nlmAgreed) {
      return {
        status: 'HIGH_CONFIDENCE',
        notes: `原始檔案無解答，兩組 NotebookLM 一致語意推論答案為 (${nlmPrimaryAns})。`,
      };
    } else {
      return {
        status: 'DISPUTED_NLM_VS_NLM',
        notes: `原始檔案無解答，兩組 NotebookLM 回答不一致 (${joinStr})。`,
      };
    }
  }
}

function applyResultsToPaper(paperFile, prefix) {
  const paperPath = path.join(SERVER_DATA_DIR, paperFile);
  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));

  const resultFiles = fs.readdirSync(BATCH_DIR).filter(f => f.startsWith(`result_${prefix}_`));
  let updatedCount = 0;

  for (const resFile of resultFiles) {
    const resPath = path.join(BATCH_DIR, resFile);
    const resData = JSON.parse(fs.readFileSync(resPath, 'utf-8'));

    for (const item of resData.results || []) {
      const q = paperData.questions.find(q => q.id === item.id);
      if (!q) continue;

      if (q.nlmResponses && item.nlmResponses) {
        for (let i = 0; i < q.nlmResponses.length; i++) {
          if (item.nlmResponses[i]) {
            q.nlmResponses[i].selectedOption = item.nlmResponses[i].selectedOption || null;
            if (item.nlmResponses[i].formattedResponse) {
              q.nlmResponses[i].formattedResponse = item.nlmResponses[i].formattedResponse;
            }
          }
        }
      }

      const opt1 = q.nlmResponses[0]?.selectedOption;
      const opt2 = q.nlmResponses[1]?.selectedOption;

      const rec = reconcile(q.sourceProvidedAnswer, opt1, opt2);
      q.reconciliationStatus = item.reconciliationStatus || rec.status;
      q.reconciliationNotes = item.reconciliationNotes || rec.notes;
      q.qcVerified = true;
      q.qcStatus = 'QC_PASSED';
      q.qcVerifiedAt = new Date().toISOString();

      updatedCount++;
    }
  }

  fs.writeFileSync(paperPath, JSON.stringify(paperData, null, 2), 'utf-8');
  console.log(`Applied Subagent QC results to ${paperData.title}: ${updatedCount} questions updated.`);
}

applyResultsToPaper('2026_A.json', 'A100');
applyResultsToPaper('2026_B.json', 'B52');

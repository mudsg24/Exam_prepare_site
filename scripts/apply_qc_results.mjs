import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

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

function restoreAndApply(paperFile, paperPrefix) {
  const paperPath = path.join(SERVER_DATA_DIR, paperFile);
  const paperData = JSON.parse(fs.readFileSync(paperPath, 'utf-8'));

  // Get base nlmResponses structure from commit e3224c1 if needed
  let gitPrevData = null;
  try {
    const gitJsonStr = execSync(`git show e3224c1:public/server-data/${paperFile}`, {
      encoding: 'utf-8',
      maxBuffer: 100 * 1024 * 1024,
    });
    gitPrevData = JSON.parse(gitJsonStr);
  } catch (e) {
    console.warn(`Could not load e3224c1 for ${paperFile}:`, e.message);
  }

  if (gitPrevData && gitPrevData.questions) {
    for (const currQ of paperData.questions) {
      if (!currQ.nlmResponses || currQ.nlmResponses.length === 0) {
        const prevQ = gitPrevData.questions.find((p) => p.id === currQ.id);
        if (prevQ && prevQ.nlmResponses) {
          currQ.nlmResponses = prevQ.nlmResponses;
        }
      }
    }
  }

  // Find all matching result files in tmp/qc_batches/
  const resultFiles = fs.readdirSync(BATCH_DIR).filter((f) => f.startsWith(`result_${paperPrefix}`));
  console.log(`Processing ${resultFiles.length} result files for ${paperFile}:`, resultFiles);

  let updatedCount = 0;
  for (const resFile of resultFiles) {
    const resPath = path.join(BATCH_DIR, resFile);
    const resData = JSON.parse(fs.readFileSync(resPath, 'utf-8'));

    for (const item of resData.results || []) {
      const q = paperData.questions.find((q) => q.id === item.id);
      if (!q) continue;

      if (item.nlmResponses && item.nlmResponses.length > 0) {
        if (!q.nlmResponses || q.nlmResponses.length === 0) {
          q.nlmResponses = item.nlmResponses;
        } else {
          for (let i = 0; i < item.nlmResponses.length; i++) {
            if (item.nlmResponses[i]) {
              if (!q.nlmResponses[i]) {
                q.nlmResponses[i] = item.nlmResponses[i];
              } else {
                if (item.nlmResponses[i].selectedOption !== undefined) {
                  q.nlmResponses[i].selectedOption = item.nlmResponses[i].selectedOption;
                }
                if (item.nlmResponses[i].formattedResponse) {
                  q.nlmResponses[i].formattedResponse = item.nlmResponses[i].formattedResponse;
                }
              }
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
  console.log(`Successfully applied QC results to ${paperData.title}: ${updatedCount} questions updated.`);
}

restoreAndApply('2026_A.json', 'A');
restoreAndApply('2026_B.json', 'B');

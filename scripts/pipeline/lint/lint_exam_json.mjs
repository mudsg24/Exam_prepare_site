import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SERVER_DATA_DIR = path.resolve(__dirname, '../../../public/server-data');

// Regex matching synthetic standalone section headers inserted by subagents (e.g. **History & Clinical Presentation:** or \nQuestion:)
const SYNTHETIC_HEADER_REGEX = /(\*\*|^\s*|\n\s*)(History & Clinical Presentation|Physical Examination & Vitals|Physical Examination & Imaging|Physical Examination|Laboratory Evaluation \(ABG\)|Laboratory & Genetic Evaluation|Laboratory Evaluation|Laboratory Studies|Laboratory & Imaging|Urine Diagnostics|24-hour Urine Collection|Arterial blood gas|Clinical Course|Clinical Decision & Question|Question)\s*(\*\*:?|:\s*\n)/gi;

function lintExamFile(filePath) {
  const fileName = path.basename(filePath);
  if (fileName === 'exams_manifest.json' || fileName === 'image_index.json' || !fileName.endsWith('.json')) {
    return { errors: [], warnings: [] };
  }

  const raw = fs.readFileSync(filePath, 'utf-8');
  let data;
  try {
    data = JSON.parse(raw);
  } catch (err) {
    return { errors: [`Failed to parse JSON file ${fileName}: ${err.message}`], warnings: [] };
  }

  if (!data.questions || !Array.isArray(data.questions)) {
    return { errors: [], warnings: [] };
  }

  const errors = [];
  const warnings = [];

  data.questions.forEach((q, idx) => {
    const qLabel = `Q${q.number || idx + 1} (${q.id || 'no-id'})`;
    const stem = q.stem || '';

    // Check 1: Synthetic Headers (Bold markdown headers or standalone category header lines)
    SYNTHETIC_HEADER_REGEX.lastIndex = 0;
    let hdrMatch;
    while ((hdrMatch = SYNTHETIC_HEADER_REGEX.exec(stem)) !== null) {
      errors.push(`[${fileName} -> ${qLabel}] Synthetic header detected: "${hdrMatch[0].trim()}" in stem.`);
    }

    // Check 2: Regex Artifacts / Broken Sentences (e.g. \n\n between lowercase words: "on \n\n physical")
    const brokenSentenceRegex = /([a-z]{3,})\s*\n\n\s*([a-z]{3,})/g;
    let match;
    while ((match = brokenSentenceRegex.exec(stem)) !== null) {
      errors.push(`[${fileName} -> ${qLabel}] Broken sentence detected across lowercase words: "${match[1]}" <\\n\\n> "${match[2]}".`);
    }

    // Check 3: Unescaped Tildes causing GFM Strikethroughs
    // Match unescaped ~ in ranges (e.g., 3.5~5 instead of 3.5\~5) when multiple ~ exist
    const tildes = (stem.match(/(?<!\\)~/g) || []).length;
    if (tildes >= 2) {
      warnings.push(`[${fileName} -> ${qLabel}] Unescaped paired tildes (${tildes}) detected in stem. Run /tn-exam-expert to fix GFM strikethroughs.`);
    }

    // Check 4: Wall of Text (Stems > 350 chars with zero newlines)
    const newlines = (stem.match(/\n/g) || []).length;
    if (stem.length > 350 && newlines === 0) {
      warnings.push(`[${fileName} -> ${qLabel}] Wall of text detected (${stem.length} chars with 0 newlines). Run /tn-exam-expert to de-wall.`);
    }

    // Check 5: Integrity
    if (!stem.trim()) {
      errors.push(`[${fileName} -> ${qLabel}] Empty stem.`);
    }

    if (!Array.isArray(q.options) || q.options.length < 2) {
      errors.push(`[${fileName} -> ${qLabel}] Insufficient options (count: ${q.options ? q.options.length : 0}).`);
    }

    // Check 6: Image Schema & Asset Existence Gate
    const PUBLIC_DIR = path.resolve(SERVER_DATA_DIR, '..');
    const imagesToCheck = [...(q.resolvedImages || []), ...(q.stemImages || [])];
    imagesToCheck.forEach((img, iIdx) => {
      if (typeof img === 'object' && img !== null) {
        if (!img.relPath && img.imagePath) {
          errors.push(`[${fileName} -> ${qLabel}] Image #${iIdx + 1} uses prohibited key "imagePath" instead of standard "relPath".`);
        } else if (!img.relPath) {
          errors.push(`[${fileName} -> ${qLabel}] Image #${iIdx + 1} is missing mandatory field "relPath".`);
        } else {
          const cleanRel = img.relPath.trim().replace(/^\//, '');
          const diskPath = path.join(PUBLIC_DIR, cleanRel);
          if (!fs.existsSync(diskPath)) {
            errors.push(`[${fileName} -> ${qLabel}] Referenced image file does not exist on disk: "${img.relPath}"`);
          }
        }
      }
    });

    // Check 7: QC Verification Integrity Gate (Zero Fake QC / Zero Null SelectedOption)
    if (q.qcVerified === true) {
      if (!Array.isArray(q.nlmResponses) || q.nlmResponses.length < 2) {
        errors.push(`[${fileName} -> ${qLabel}] qcVerified is true but nlmResponses count is ${q.nlmResponses ? q.nlmResponses.length : 0} (must be exactly 2).`);
      } else {
        q.nlmResponses.forEach((resp, rIdx) => {
          const rawLen = (resp.rawResponse || '').length;
          if (rawLen < 200) {
            errors.push(`[${fileName} -> ${qLabel}] qcVerified is true but nlmResponse #${rIdx + 1} rawResponse length is ${rawLen} (< 200 chars).`);
          }
          if (resp.error) {
            errors.push(`[${fileName} -> ${qLabel}] qcVerified is true but nlmResponse #${rIdx + 1} contains RPC/connection error: "${resp.error}".`);
          }
          if (!resp.selectedOption || typeof resp.selectedOption !== 'string' || !resp.selectedOption.trim()) {
            errors.push(`[${fileName} -> ${qLabel}] qcVerified is true but nlmResponse #${rIdx + 1} selectedOption is null/empty.`);
          }

          // Check for Synthetic / Faked NLM Responses (copy of sourceExplanation)
          const cleanExpl = (q.sourceExplanation || '').trim();
          if (cleanExpl.length > 50 && resp.rawResponse && resp.rawResponse.includes(cleanExpl)) {
            errors.push(`[${fileName} -> ${qLabel}] FAKED NLM RESPONSE DETECTED! nlmResponse #${rIdx + 1} rawResponse contains verbatim copy of sourceExplanation.`);
          }
        });

        // Check NLM discrepancy reconciliation & Anti-Fake Identical Response Check
        if (q.nlmResponses.length === 2) {
          const resp1 = (q.nlmResponses[0].rawResponse || '').trim();
          const resp2 = (q.nlmResponses[1].rawResponse || '').trim();
          if (resp1.length > 50 && resp1 === resp2) {
            errors.push(`[${fileName} -> ${qLabel}] FAKED NLM RESPONSE DETECTED! Account 1 and Account 2 rawResponse are 100% identical verbatim strings.`);
          }

          const sel1 = q.nlmResponses[0].selectedOption;
          const sel2 = q.nlmResponses[1].selectedOption;
          if (sel1 && sel2 && sel1 !== sel2) {
            if (!q.reconciliationStatus || !q.qcNotes) {
              errors.push(`[${fileName} -> ${qLabel}] qcVerified is true but NLM #1 (${sel1}) and NLM #2 (${sel2}) disagree without explicit reconciliationStatus/qcNotes.`);
            }
          }
        }
      }
    }

    // Check 8: Pure English Medical Terms & Anti-Bilingual Brackets Gate
    const FORBIDDEN_ZH_MED_TERMS = [
      '高草酸尿症', '近曲小管', '足細胞', '軟水器', '雙折射', '腎切片', '前列腺',
      '滲透壓', '高血鈉', '低血鈉', '高血鉀', '低血鉀', '血管收縮', '利尿劑', '尿崩症'
    ];
    const BILINGUAL_BRACKET_REGEX = /([\u4e00-\u9fa5]{2,}\s*\([A-Za-z\s\/]{2,}\)|[A-Za-z]{2,}\s*\([\u4e00-\u9fa5]{2,}\))/g;

    const explanationTexts = [String(q.sourceExplanation || ''), String(q.codexExplanation || '')];
    explanationTexts.forEach((text, tIdx) => {
      if (!text || typeof text !== 'string') return;
      FORBIDDEN_ZH_MED_TERMS.forEach(term => {
        if (text.includes(term)) {
          errors.push(`[${fileName} -> ${qLabel}] Chinese medical term "${term}" detected in explanation #${tIdx + 1}. Must be pure English.`);
        }
      });

      BILINGUAL_BRACKET_REGEX.lastIndex = 0;
      let bMatch;
      while ((bMatch = BILINGUAL_BRACKET_REGEX.exec(text)) !== null) {
        errors.push(`[${fileName} -> ${qLabel}] Prohibited bilingual bracket "${bMatch[0]}" detected in explanation #${tIdx + 1}. Must use pure English term.`);
      }
    });
  });

  return { errors, warnings };
}

function lintManifestFile() {
  const manifestPath = path.join(SERVER_DATA_DIR, 'exams_manifest.json');
  if (!fs.existsSync(manifestPath)) {
    return [`exams_manifest.json not found in ${SERVER_DATA_DIR}`];
  }

  const errors = [];
  let manifest;
  try {
    manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  } catch (err) {
    return [`Failed to parse exams_manifest.json: ${err.message}`];
  }

  if (!Array.isArray(manifest)) {
    return ['exams_manifest.json content must be an array of ExamManifestItem objects.'];
  }

  manifest.forEach((item, idx) => {
    const itemLabel = `Manifest Item #${idx + 1} (${item.id || item.paperId || 'no-id'})`;

    // Forbidden Key Aliases
    if (item.name && !item.title) {
      errors.push(`[${itemLabel}] Prohibited key "name" used instead of "title".`);
    }
    if (item.totalQuestions !== undefined && item.questionCount === undefined) {
      errors.push(`[${itemLabel}] Prohibited key "totalQuestions" used instead of "questionCount".`);
    }

    // Required Field Schema Checks
    if (!item.id) {
      errors.push(`[${itemLabel}] Missing required field "id".`);
    }
    if (!item.title) {
      errors.push(`[${itemLabel}] Missing required field "title".`);
    }
    if (!item.sourceCategory) {
      errors.push(`[${itemLabel}] Missing required field "sourceCategory".`);
    }
    if (item.questionCount === undefined || typeof item.questionCount !== 'number') {
      errors.push(`[${itemLabel}] Missing or invalid numeric field "questionCount".`);
    }

    // Disk File Resolution Check
    const filename = item.filename || `${item.id}.json`;
    const targetPath = filename.startsWith('/') ? path.join(__dirname, '../../../public', filename) : path.join(SERVER_DATA_DIR, filename);
    const fallbackPath = path.join(SERVER_DATA_DIR, `${item.id}.json`);
    if (!fs.existsSync(targetPath) && !fs.existsSync(fallbackPath)) {
      errors.push(`[${itemLabel}] Targeted JSON file does not exist: ${filename}`);
    }
  });

  return errors;
}

function runLinter() {
  console.log('🔍 Running Exam JSON Static Linter (Checking Schema Keys, Synthetic Headers & Broken Sentences)...');

  if (!fs.existsSync(SERVER_DATA_DIR)) {
    console.error(`❌ Error: Directory not found: ${SERVER_DATA_DIR}`);
    process.exit(1);
  }

  let totalErrors = [];
  const manifestErrors = lintManifestFile();
  if (manifestErrors.length > 0) {
    totalErrors.push(...manifestErrors);
  }

  const files = fs.readdirSync(SERVER_DATA_DIR);
  let totalFilesChecked = 0;

  files.forEach(f => {
    const fullPath = path.join(SERVER_DATA_DIR, f);
    if (fs.statSync(fullPath).isFile() && f.endsWith('.json') && f !== 'exams_manifest.json' && f !== 'image_index.json') {
      totalFilesChecked++;
      const { errors } = lintExamFile(fullPath);
      if (errors.length > 0) {
        totalErrors.push(...errors);
      }
    }
  });

  console.log(`📊 Checked exams_manifest.json (${manifestErrors.length === 0 ? 'SCHEMA VALID' : 'SCHEMA ERRORS'}) and ${totalFilesChecked} exam database JSON files.`);

  if (totalErrors.length > 0) {
    console.error(`❌ Exam JSON Lint Failed with ${totalErrors.length} error(s):\n`);
    totalErrors.forEach(err => console.error(`  - ${err}`));
    console.error('\n🚫 Build aborted due to exam data governance violations.');
    process.exit(1);
  } else {
    console.log('✅ Exam JSON Lint Passed! All manifest schemas and exam files are clean (0 synthetic headers, 0 broken sentences, 0 schema key violations).');
    process.exit(0);
  }
}

export { lintExamFile, runLinter };

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  runLinter();
}


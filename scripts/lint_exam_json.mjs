import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SERVER_DATA_DIR = path.resolve(__dirname, '../public/server-data');

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
  });

  return { errors, warnings };
}

function runLinter() {
  console.log('🔍 Running Exam JSON Static Linter (Checking Synthetic Headers & Broken Sentences)...');

  if (!fs.existsSync(SERVER_DATA_DIR)) {
    console.error(`❌ Error: Directory not found: ${SERVER_DATA_DIR}`);
    process.exit(1);
  }

  const files = fs.readdirSync(SERVER_DATA_DIR);
  let totalFilesChecked = 0;
  let totalErrors = [];

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

  console.log(`📊 Checked ${totalFilesChecked} exam database JSON files.`);

  if (totalErrors.length > 0) {
    console.error(`❌ Exam JSON Lint Failed with ${totalErrors.length} error(s):\n`);
    totalErrors.forEach(err => console.error(`  - ${err}`));
    console.error('\n🚫 Build aborted due to exam data governance violations.');
    process.exit(1);
  } else {
    console.log('✅ Exam JSON Lint Passed! All exam files are clean (0 synthetic headers, 0 broken sentences).');
    process.exit(0);
  }
}

export { lintExamFile, runLinter };

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  runLinter();
}


import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PUBLIC_DIR = path.resolve(__dirname, '../../../public');
const TUTORIALS_DIR = path.resolve(PUBLIC_DIR, 'server-data/tutorials');

function lintTutorialFile(filePath) {
  const relFile = path.relative(PUBLIC_DIR, filePath);
  const raw = fs.readFileSync(filePath, 'utf-8');
  let data;
  try {
    data = JSON.parse(raw);
  } catch (err) {
    return [`[${relFile}] Invalid JSON syntax: ${err.message}`];
  }

  const errors = [];
  const sections = data.sections || [];
  const rootDiagrams = data.diagrams || [];

  if (rootDiagrams && Array.isArray(rootDiagrams)) {
    rootDiagrams.forEach((diag, idx) => {
      if (typeof diag === 'object' && diag !== null) {
        if (diag.url && !diag.imagePath) {
          errors.push(`[${relFile}] Root diagram[${idx}] uses deprecated property 'url' instead of 'imagePath'`);
        }
        if (diag.relPath && !diag.imagePath) {
          errors.push(`[${relFile}] Root diagram[${idx}] uses deprecated property 'relPath' instead of 'imagePath'`);
        }
        if (diag.title && !diag.caption) {
          errors.push(`[${relFile}] Root diagram[${idx}] uses deprecated property 'title' instead of 'caption'`);
        }
        if (diag.imagePath) {
          const cleanPath = diag.imagePath.replace(/^\//, '');
          const absPath = path.join(PUBLIC_DIR, cleanPath);
          if (!fs.existsSync(absPath)) {
            errors.push(`[${relFile}] Root diagram[${idx}] imagePath file missing on disk: "${diag.imagePath}"`);
          }
        }
      }
    });
  }

  sections.forEach((sec, sIdx) => {
    const secTitle = sec.title || `Section-${sIdx + 1}`;
    let secDiagrams = sec.diagrams || [];
    if (!secDiagrams.length && sec.diagram) {
      secDiagrams = [sec.diagram];
    }

    if (!secDiagrams.length) {
      errors.push(`[${relFile}] Section[${sIdx}] ("${secTitle}") has NO diagrams attached`);
    }

    secDiagrams.forEach((diag, dIdx) => {
      if (typeof diag === 'object' && diag !== null) {
        if (diag.url && !diag.imagePath) {
          errors.push(`[${relFile}] Section[${sIdx}] diagram[${dIdx}] uses deprecated property 'url' instead of 'imagePath'`);
        }
        if (diag.relPath && !diag.imagePath) {
          errors.push(`[${relFile}] Section[${sIdx}] diagram[${dIdx}] uses deprecated property 'relPath' instead of 'imagePath'`);
        }
        if (diag.title && !diag.caption) {
          errors.push(`[${relFile}] Section[${sIdx}] diagram[${dIdx}] uses deprecated property 'title' instead of 'caption'`);
        }
        if (diag.imagePath) {
          const cleanPath = diag.imagePath.replace(/^\//, '');
          const absPath = path.join(PUBLIC_DIR, cleanPath);
          if (!fs.existsSync(absPath)) {
            errors.push(`[${relFile}] Section[${sIdx}] diagram[${dIdx}] imagePath file missing on disk: "${diag.imagePath}"`);
          }
        }
      }
    });
    // Check language contract in tutorial content
    const FORBIDDEN_ZH_MED_TERMS = [
      '高草酸尿症', '近曲小管', '足細胞', '軟水器', '雙折射', '腎切片', '前列腺',
      '滲透壓', '高血鈉', '低血鈉', '高血鉀', '低血鉀', '血管收縮', '利尿劑', '尿崩症'
    ];
    const BILINGUAL_BRACKET_REGEX = /([\u4e00-\u9fa5]{2,}\s*\([A-Za-z\s\/]{2,}\)|[A-Za-z]{2,}\s*\([\u4e00-\u9fa5]{2,}\))/g;

    const content = sec.content || '';
    FORBIDDEN_ZH_MED_TERMS.forEach(term => {
      if (content.includes(term)) {
        errors.push(`[${relFile}] Section[${sIdx}] ("${secTitle}") contains Chinese medical term "${term}". Must be pure English.`);
      }
    });

    BILINGUAL_BRACKET_REGEX.lastIndex = 0;
    let bMatch;
    while ((bMatch = BILINGUAL_BRACKET_REGEX.exec(content)) !== null) {
      errors.push(`[${relFile}] Section[${sIdx}] ("${secTitle}") contains prohibited bilingual bracket "${bMatch[0]}". Must use pure English term.`);
    }
  });

  return errors;
}

function runTutorialLinter() {
  console.log('📘 Running Tutorial JSON Diagram & Schema Linter...');

  if (!fs.existsSync(TUTORIALS_DIR)) {
    console.error(`❌ Error: Directory not found: ${TUTORIALS_DIR}`);
    process.exit(1);
  }

  const files = fs.readdirSync(TUTORIALS_DIR).filter(f => f.endsWith('.json'));
  let totalErrors = [];

  files.forEach(file => {
    const fullPath = path.join(TUTORIALS_DIR, file);
    const errors = lintTutorialFile(fullPath);
    if (errors.length > 0) {
      totalErrors.push(...errors);
    }
  });

  console.log(`📊 Scanned ${files.length} tutorial JSON files in server-data/tutorials.`);

  if (totalErrors.length > 0) {
    console.error(`❌ Tutorial Linter Failed with ${totalErrors.length} error(s):\n`);
    totalErrors.forEach(err => console.error(`  - ${err}`));
    console.error('\n🚫 Build/Lint aborted due to tutorial schema anomalies.');
    process.exit(1);
  } else {
    console.log('✅ Tutorial Linter Passed! All tutorial diagram schemas and image paths are valid.');
    process.exit(0);
  }
}

runTutorialLinter();

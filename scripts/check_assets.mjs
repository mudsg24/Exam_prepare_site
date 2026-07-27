import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PUBLIC_DIR = path.resolve(__dirname, '../public');
const SERVER_DATA_DIR = path.resolve(PUBLIC_DIR, 'server-data');

function scanDirectory(dir) {
  let files = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files = files.concat(scanDirectory(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.json') && entry.name !== 'exams_manifest.json' && entry.name !== 'image_index.json') {
      files.push(fullPath);
    }
  }
  return files;
}

function checkAssetPathsInFile(filePath) {
  const relFile = path.relative(PUBLIC_DIR, filePath);
  const raw = fs.readFileSync(filePath, 'utf-8');
  let data;
  try {
    data = JSON.parse(raw);
  } catch (err) {
    return [`[${relFile}] Invalid JSON syntax: ${err.message}`];
  }

  const missingAssets = [];
  // Regex matching any path starting with /server-data/assets/ or server-data/assets/
  const assetRegex = /"?(\/server-data\/assets\/[^"\s]+)"?/g;
  let match;

  while ((match = assetRegex.exec(raw)) !== null) {
    const imageRelPath = match[1];
    // Strip query strings or trailing punctuation if any
    const cleanRelPath = imageRelPath.split('?')[0].replace(/[,\s]+$/, '');
    const absoluteImagePath = path.join(PUBLIC_DIR, cleanRelPath);

    if (!fs.existsSync(absoluteImagePath)) {
      missingAssets.push(`[${relFile}] Missing image asset: "${cleanRelPath}" (Absolute: ${absoluteImagePath})`);
    }
  }

  return missingAssets;
}

function runAssetChecker() {
  console.log('🖼️  Running Server Data Asset Integrity Checker...');

  if (!fs.existsSync(SERVER_DATA_DIR)) {
    console.error(`❌ Error: Directory not found: ${SERVER_DATA_DIR}`);
    process.exit(1);
  }

  const jsonFiles = scanDirectory(SERVER_DATA_DIR);
  let totalErrors = [];

  jsonFiles.forEach(file => {
    const errors = checkAssetPathsInFile(file);
    if (errors.length > 0) {
      totalErrors.push(...errors);
    }
  });

  console.log(`📊 Scanned ${jsonFiles.length} JSON database files across server-data.`);

  if (totalErrors.length > 0) {
    console.error(`❌ Asset Verification Failed with ${totalErrors.length} missing asset(s):\n`);
    totalErrors.forEach(err => console.error(`  - ${err}`));
    console.error('\n🚫 Build/Lint aborted due to missing image assets.');
    process.exit(1);
  } else {
    console.log('✅ Asset Verification Passed! All referenced image assets exist on disk.');
    process.exit(0);
  }
}

export { checkAssetPathsInFile, runAssetChecker };

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  runAssetChecker();
}

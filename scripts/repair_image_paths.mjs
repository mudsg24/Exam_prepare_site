import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PUBLIC_DIR = path.resolve(__dirname, '../public');
const SERVER_DATA_DIR = path.resolve(PUBLIC_DIR, 'server-data');
const REFERENCE_IMAGES_DIR = path.resolve(PUBLIC_DIR, 'reference-images');
const ASSETS_DIR = path.resolve(SERVER_DATA_DIR, 'assets');

// Load image_index.json for fast lookup if available
let imageIndexMap = new Map();
const imageIndexPath = path.resolve(SERVER_DATA_DIR, 'image_index.json');
if (fs.existsSync(imageIndexPath)) {
  try {
    const raw = fs.readFileSync(imageIndexPath, 'utf-8');
    const items = JSON.parse(raw);
    items.forEach((item) => {
      if (item.filename && item.relPath) {
        imageIndexMap.set(item.filename, item.relPath);
      }
      if (item.id && item.relPath) {
        imageIndexMap.set(item.id, item.relPath);
      }
    });
  } catch (err) {
    console.warn('Could not parse image_index.json:', err.message);
  }
}

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

function findActualFileInPublic(relativePathCandidate) {
  if (!relativePathCandidate || typeof relativePathCandidate !== 'string') return null;

  let clean = relativePathCandidate.trim().replace(/^[/\\]+/, '');
  let fullPath = path.join(PUBLIC_DIR, clean);

  if (fs.existsSync(fullPath)) {
    return '/' + clean;
  }

  // Candidates 1: Prepend reference-images
  let refCandidate = path.join(PUBLIC_DIR, 'reference-images', clean);
  if (fs.existsSync(refCandidate)) {
    return '/reference-images/' + clean;
  }

  // Candidate 2: Prepend server-data/assets
  let assetCandidate = path.join(PUBLIC_DIR, 'server-data/assets', clean);
  if (fs.existsSync(assetCandidate)) {
    return '/server-data/assets/' + clean;
  }

  // Candidate 3: Check imageIndexMap by filename
  const filename = path.basename(clean);
  if (imageIndexMap.has(filename)) {
    const targetRel = imageIndexMap.get(filename);
    if (fs.existsSync(path.join(PUBLIC_DIR, targetRel.replace(/^\//, '')))) {
      return targetRel;
    }
  }

  return null;
}

function repairImageObject(imgObj) {
  if (typeof imgObj !== 'object' || imgObj === null) return false;

  let modified = false;

  // Fix 1: Key alias (imagePath -> relPath)
  if (!imgObj.relPath && imgObj.imagePath) {
    imgObj.relPath = imgObj.imagePath;
    modified = true;
  }

  const currentPath = imgObj.relPath || imgObj.path || '';
  if (!currentPath) return modified;

  const validPath = findActualFileInPublic(currentPath);
  if (validPath && validPath !== imgObj.relPath) {
    imgObj.relPath = validPath;
    modified = true;
  }

  return modified;
}

function repairFile(filePath) {
  const relFile = path.relative(PUBLIC_DIR, filePath);
  let raw = fs.readFileSync(filePath, 'utf-8');
  let data;
  try {
    data = JSON.parse(raw);
  } catch (err) {
    console.error(`❌ Could not parse JSON file ${relFile}:`, err.message);
    return 0;
  }

  let repairsCount = 0;

  if (data.questions && Array.isArray(data.questions)) {
    data.questions.forEach((q) => {
      if (q.resolvedImages && Array.isArray(q.resolvedImages)) {
        q.resolvedImages.forEach((img) => {
          if (repairImageObject(img)) repairsCount++;
        });
      }
      if (q.stemImages && Array.isArray(q.stemImages)) {
        q.stemImages.forEach((img) => {
          if (repairImageObject(img)) repairsCount++;
        });
      }
    });
  }

  if (data.sections && Array.isArray(data.sections)) {
    data.sections.forEach((sec) => {
      if (sec.images && Array.isArray(sec.images)) {
        sec.images.forEach((img) => {
          if (typeof img === 'object') {
            if (repairImageObject(img)) repairsCount++;
          }
        });
      }
    });
  }

  if (repairsCount > 0) {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
    console.log(`🔧 Repaired ${repairsCount} image path(s) in [${relFile}]`);
  }

  return repairsCount;
}

function runRepair() {
  console.log('🛠️  Running Image Path Database Repair...');
  const jsonFiles = scanDirectory(SERVER_DATA_DIR);
  let totalRepairs = 0;

  jsonFiles.forEach((file) => {
    totalRepairs += repairFile(file);
  });

  console.log(`\n🎉 Repair process completed across ${jsonFiles.length} JSON database files.`);
  console.log(`✅ Total image references repaired: ${totalRepairs}`);
}

runRepair();

import fs from 'fs';
import path from 'path';

const KDIGO_DIR = '/Users/yuan/Projects/PDF/Outputs/KDIGO';
const BRENNER_DIR = '/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e';
const OUTPUT_FILE = path.join(process.cwd(), 'public', 'server-data', 'image_index.json');

function scanDir(dirPath, sourceName) {
  const results = [];
  if (!fs.existsSync(dirPath)) {
    console.warn(`[WARN] Directory does not exist: ${dirPath}`);
    return results;
  }

  function walk(currentDir) {
    const files = fs.readdirSync(currentDir, { withFileTypes: true });
    for (const f of files) {
      const fullPath = path.join(currentDir, f.name);
      if (f.isDirectory()) {
        walk(fullPath);
      } else if (/\.(png|jpe?g|webp|gif|svg)$/i.test(f.name)) {
        const relPath = path.relative(process.cwd(), fullPath);
        results.push({
          id: `${sourceName}_${f.name}`,
          title: f.name.replace(/\.[^/.]+$/, ''),
          bookSource: sourceName,
          relPath: `/${relPath}`,
          absPath: fullPath,
          filename: f.name,
        });
      }
    }
  }

  walk(dirPath);
  return results;
}

export function buildImageIndex() {
  console.log('Indexing KDIGO & Brenner 11e images...');
  const kdigoImages = scanDir(KDIGO_DIR, 'KDIGO');
  const brennerImages = scanDir(BRENNER_DIR, 'Brenner 11e');
  const allImages = [...kdigoImages, ...brennerImages];

  const dir = path.dirname(OUTPUT_FILE);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(allImages, null, 2), 'utf-8');
  console.log(`[SUCCESS] Indexed ${allImages.length} images to ${OUTPUT_FILE}`);
  return allImages;
}

buildImageIndex();

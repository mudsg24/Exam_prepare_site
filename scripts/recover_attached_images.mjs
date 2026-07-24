import fs from 'fs';
import path from 'path';

const PROCESSED_BASE_DIR = '/Users/yuan/Projects/Exam/Exam_prepare_database/Processed';
const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');
const EXAM_IMAGES_PUBLIC_DIR = path.join(process.cwd(), 'public', 'exam-images');

if (!fs.existsSync(EXAM_IMAGES_PUBLIC_DIR)) {
  fs.mkdirSync(EXAM_IMAGES_PUBLIC_DIR, { recursive: true });
}

// Recursively find all folders under PROCESSED_BASE_DIR that contain an `images` subfolder
function findProcessedPaperFolders(dir, results = []) {
  if (!fs.existsSync(dir)) return results;
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  let hasImagesSubdir = false;
  for (const entry of entries) {
    if (entry.isDirectory() && entry.name === 'images') {
      hasImagesSubdir = true;
      break;
    }
  }

  if (hasImagesSubdir) {
    results.push(dir);
  }

  for (const entry of entries) {
    if (entry.isDirectory() && entry.name !== 'images') {
      findProcessedPaperFolders(path.join(dir, entry.name), results);
    }
  }
  return results;
}

// Clean paper title to match paperId
function cleanPaperTitle(rawName) {
  return rawName.replace(/\s*-\s*原檔$/i, '').trim();
}

function makePaperId(title) {
  return title.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5]/g, '_');
}

// Main Recovery Runner
export async function runRecovery() {
  console.log('=== Starting Question Image Recovery ===');
  const paperFolders = findProcessedPaperFolders(PROCESSED_BASE_DIR);
  console.log(`Found ${paperFolders.length} folders with images in Processed database.`);

  // Load all JSON datasets in server-data
  const serverJsonFiles = fs.readdirSync(SERVER_DATA_DIR).filter(f => f.endsWith('.json') && f !== 'exams_manifest.json' && f !== 'image_index.json');
  
  let totalCopiedImages = 0;
  let totalUpdatedQuestions = 0;
  let updatedPapersCount = 0;

  for (const jsonFile of serverJsonFiles) {
    const jsonPath = path.join(SERVER_DATA_DIR, jsonFile);
    let paperData;
    try {
      paperData = JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));
    } catch (e) {
      console.warn(`[WARN] Could not parse ${jsonFile}`);
      continue;
    }

    const paperId = paperData.id || paperData.paperId || jsonFile.replace('.json', '');
    const paperTitle = paperData.title || cleanPaperTitle(paperData.rawTitle || paperId);

    // Find matching folder in paperFolders
    const matchedFolders = paperFolders.filter(folderPath => {
      const baseName = path.basename(folderPath); // e.g. "office" or "hybrid_auto"
      const parentName = path.basename(path.dirname(folderPath)); // e.g. "2025 彰基重點 - 原檔"
      const cleanParent = cleanPaperTitle(parentName);
      const cleanBase = cleanPaperTitle(baseName);
      
      const parentId = makePaperId(cleanParent);
      const baseId = makePaperId(cleanBase);

      return parentId === paperId || baseId === paperId || paperId.includes(parentId) || parentId.includes(paperId);
    });

    if (matchedFolders.length === 0) {
      continue;
    }

    let paperImagesAttached = 0;

    for (const matchedFolder of matchedFolders) {
      const imagesDir = path.join(matchedFolder, 'images');
      if (!fs.existsSync(imagesDir)) continue;

      // Find .md file in matchedFolder or parent folder
      let mdFile = fs.readdirSync(matchedFolder).find(f => f.endsWith('.md'));
      let mdPath = mdFile ? path.join(matchedFolder, mdFile) : null;
      if (!mdPath) {
        const parentDir = path.dirname(matchedFolder);
        mdFile = fs.readdirSync(parentDir).find(f => f.endsWith('.md'));
        if (mdFile) mdPath = path.join(parentDir, mdFile);
      }

      if (!mdPath || !fs.existsSync(mdPath)) {
        continue;
      }

      const mdContent = fs.readFileSync(mdPath, 'utf-8');
      const mdLines = mdContent.split('\n');

      // Parse image references and map them to question numbers
      const questionImageMap = {}; // qNum -> array of image filenames
      let currentQNum = 1;

      for (let i = 0; i < mdLines.length; i++) {
        const line = mdLines[i].trim();
        if (!line) continue;

        // Check for question header like "1. ", "2. ", "Question 3", "題號: 4"
        const qMatch = line.match(/^(?:Question\s+([0-9]+)|#([0-9]+)\b|題號\s*[:：]\s*([0-9]+)|([0-9]+)\.\s+)/i);
        if (qMatch) {
          const numStr = qMatch[1] || qMatch[2] || qMatch[3] || qMatch[4];
          if (numStr) {
            currentQNum = parseInt(numStr, 10);
          }
        }

        // Check for Markdown image tag: ![](images/filename.ext) or ![](filename.ext) or <img src="...">
        const imgMatch = line.match(/!\[.*?\]\((?:images\/)?([^\)]+)\)/i) || line.match(/<img[^>]+src=["'](?:images\/)?([^"']+)["']/i);
        if (imgMatch) {
          const imgFileName = path.basename(imgMatch[1]);
          if (!questionImageMap[currentQNum]) {
            questionImageMap[currentQNum] = [];
          }
          if (!questionImageMap[currentQNum].includes(imgFileName)) {
            questionImageMap[currentQNum].push(imgFileName);
          }
        }
      }

      // Destination dir for this paper's public images
      const targetPublicImgDir = path.join(EXAM_IMAGES_PUBLIC_DIR, paperId);
      if (!fs.existsSync(targetPublicImgDir)) {
        fs.mkdirSync(targetPublicImgDir, { recursive: true });
      }

      const questions = paperData.questions || [];

      for (const q of questions) {
        const qNum = q.number;
        const mappedImgFiles = questionImageMap[qNum] || [];

        if (mappedImgFiles.length > 0) {
          q.attachedImages = q.attachedImages || [];

          for (let idx = 0; idx < mappedImgFiles.length; idx++) {
            const fileName = mappedImgFiles[idx];
            const srcImgPath = path.join(imagesDir, fileName);

            if (fs.existsSync(srcImgPath)) {
              const destImgPath = path.join(targetPublicImgDir, fileName);
              fs.copyFileSync(srcImgPath, destImgPath);

              const relPath = `/exam-images/${paperId}/${fileName}`;
              const imgObj = {
                id: `img_${paperId}_q${qNum}_${idx + 1}`,
                fileName: fileName,
                relPath: relPath,
                caption: `圖 ${qNum}-${idx + 1}`
              };

              if (!q.attachedImages.some(existing => existing.relPath === relPath)) {
                q.attachedImages.push(imgObj);
                paperImagesAttached++;
                totalCopiedImages++;
              }
            }
          }
          totalUpdatedQuestions++;
        }
      }
    }

    if (paperImagesAttached > 0) {
      fs.writeFileSync(jsonPath, JSON.stringify(paperData, null, 2), 'utf-8');
      console.log(`[SUCCESS] Restored ${paperImagesAttached} attached images for "${paperTitle}" (${paperId})`);
      updatedPapersCount++;
    }
  }

  console.log(`\n=== Recovery Finished ===`);
  console.log(`Updated Papers: ${updatedPapersCount}`);
  console.log(`Updated Questions: ${totalUpdatedQuestions}`);
  console.log(`Total Restored Images: ${totalCopiedImages}`);
}

runRecovery();

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');

const SOURCE_DIR = '/Users/yuan/Projects/ChatGPT Work/TSN Exam 2026/outputs/2026/question-bank';
const TARGET_DIR = path.join(projectRoot, 'public', 'server-data');

// Read 2026-A provenance
const provenanceA = JSON.parse(fs.readFileSync(path.join(SOURCE_DIR, 'assets/image-provenance.json'), 'utf-8'));
const imagesAMap = {};
for (const asset of provenanceA.assets || []) {
  const filename = path.basename(asset.output_path);
  imagesAMap[asset.asset_id] = {
    id: asset.asset_id,
    fileName: filename,
    relPath: `/server-data/assets/2026-A/${filename}`,
    caption: asset.alt_zh || ''
  };
}

// Read 2026-B provenance
const provenanceB = JSON.parse(fs.readFileSync(path.join(SOURCE_DIR, 'assets/2026-B-image-provenance.json'), 'utf-8'));
const imagesBMap = {};
for (const asset of provenanceB.assets || []) {
  const filename = path.basename(asset.output_path);
  imagesBMap[asset.question_id] = {
    id: asset.asset_id,
    fileName: filename,
    relPath: `/server-data/assets/2026-B/${filename}`,
    caption: asset.alt_zh || ''
  };
}

function processStem(rawStem) {
  if (!rawStem) return '';
  // Anti-strikethrough: escape standalone tildes unless already escaped
  let cleaned = rawStem.replace(/(?<!\\)~(?!~)/g, '\\~');
  return cleaned;
}

function convertPaper(sourceFile, paperId, paperTitle, imagesMap) {
  const rawData = JSON.parse(fs.readFileSync(path.join(SOURCE_DIR, sourceFile), 'utf-8'));
  const questions = (rawData.questions || []).map((q, index) => {
    const qNum = index + 1;
    const attachedImages = [];
    if (imagesMap[q.id]) {
      attachedImages.push(imagesMap[q.id]);
    }

    const fullStem = q.case_stem ? `${q.case_stem}\n\n${q.stem}` : q.stem;
    return {
      id: `${paperId}_q${qNum}`,
      number: qNum,
      stem: processStem(fullStem),
      options: (q.options || []).map(opt => ({
        id: opt.id,
        text: opt.text
      })),
      sourceAnswerStatus: 'provided',
      sourceProvidedAnswer: q.correct_option || null,
      codexExplanation: {
        explanationZh: q.explanation_zh || '',
        optionAnalysisZh: q.option_analysis_zh || {},
        authorityEvidence: q.authority_evidence || [],
        sourceNotesZh: q.source_notes_zh || ''
      },
      nlmResponses: [],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '',
      resolvedImages: [],
      attachedImages
    };
  });

  const paperObj = {
    id: paperId,
    title: paperTitle,
    rawTitle: `${paperTitle} - 腎專模擬考試`,
    sourceCategory: '2026 年模擬試題',
    year: 2026,
    questionCount: questions.length,
    highConfidenceCount: questions.length,
    disputedCount: 0,
    createdAt: new Date().toISOString(),
    questions
  };

  fs.writeFileSync(path.join(TARGET_DIR, `${paperId}.json`), JSON.stringify(paperObj, null, 2), 'utf-8');
  console.log(`Successfully generated ${paperId}.json with ${questions.length} questions.`);
  return {
    id: paperId,
    title: paperTitle,
    sourceCategory: '2026 年模擬試題',
    questionCount: questions.length,
    year: 2026
  };
}

const manifestItemA = convertPaper('2026-A.json', '2026_A', '2026 腎臟專科模擬考 A 卷', imagesAMap);
const manifestItemB = convertPaper('2026-B.json', '2026_B', '2026 腎臟專科模擬考 B 卷', imagesBMap);

// Update exams_manifest.json
const manifestPath = path.join(TARGET_DIR, 'exams_manifest.json');
let manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));

// Filter out old entries for 2026_A and 2026_B if exist, then prepend
manifest = manifest.filter(item => item.id !== '2026_A' && item.id !== '2026_B');
manifest.unshift(manifestItemB);
manifest.unshift(manifestItemA);

fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf-8');
console.log('Successfully updated exams_manifest.json.');

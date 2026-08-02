## Forensic Audit Report

**Work Product**: Phase 2 Script Modularization (`scripts/pipeline/`, tests, `AGENTS.md`, `package.json`)
**Profile**: General Project
**Verdict**: CLEAN

### Executive Summary

A comprehensive forensic integrity audit was conducted on Phase 2 script modularization in `Exam_prepare_site`. All 12 target scripts were relocated into modular subdirectories under `scripts/pipeline/{lint,ingest,qc,nlm,utils}/`. Path resolutions across `package.json`, unit tests, helper scripts, and relocated linters were verified. The ESM export fix in `build_image_index.mjs` was confirmed. AGENTS.md Rule 1 Red Zone vs Green Zone governance boundaries were validated. All 4 verification commands executed cleanly with 100% test pass rates and zero warnings or errors. No integrity violations, hardcoded test results, facade implementations, or faked outputs were detected.

---

### Phase Results

| Check # | Phase | Description | Result | Details |
|---|---|---|---|---|
| 1 | Phase 1 (Source) | Script Relocations | PASS | 12 core scripts correctly moved into `scripts/pipeline/{ingest,lint,nlm,qc,utils}/` |
| 2 | Phase 1 (Source) | Path Resolution Fixes | PASS | `package.json`, `vitest.config.ts`, unit tests, and helper scripts updated to relative paths |
| 3 | Phase 1 (Source) | ESM Export Fix | PASS | `build_image_index.mjs` exports `scanDir` & `buildImageIndex` with `import.meta.url` CLI execution guard |
| 4 | Phase 1 (Source) | Governance Clarification | PASS | `AGENTS.md` Rule 1 explicitly defines Red Zone (prohibited regex on stems/options) vs Green Zone (permitted linters in `scripts/pipeline/`) |
| 5 | Phase 1 (Source) | Zero Faked/Hardcoded Results | PASS | Verified no dummy returns, hardcoded expected strings, or facade logic exist |
| 6 | Phase 2 (Behavioral) | `npm run build:images` | PASS | Exit 0, 2,762 images indexed into `public/server-data/image_index.json` |
| 7 | Phase 2 (Behavioral) | `npm run lint:exams` | PASS | Exit 0, all 3 linters (`lint_exam_json`, `lint_tutorial_json`, `check_assets`) passed cleanly |
| 8 | Phase 2 (Behavioral) | `npm run test` | PASS | Exit 0, 14 test files passed (98 tests total) |
| 9 | Phase 2 (Behavioral) | `npm run test:py` | PASS | Exit 0, 2 python unit tests passed |

---

### Detailed Findings & Evidence

#### 1. Script Relocation Audit
The following 12 scripts were moved from `scripts/` to `scripts/pipeline/`:
- `scripts/pipeline/ingest/`: `extract_and_attach_images.py`, `ingest_exam.mjs`
- `scripts/pipeline/lint/`: `check_assets.mjs`, `lint_exam_json.mjs`, `lint_tutorial_json.mjs`
- `scripts/pipeline/nlm/`: `ask_nlm_for_2026.mjs`, `ask_nlm_for_renal_transplant.mjs`, `process_nlm_results.py`
- `scripts/pipeline/qc/`: `apply_qc_updates.py`, `exam_qc.mjs`, `merge_qc_results.mjs`
- `scripts/pipeline/utils/`: `build_image_index.mjs`

#### 2. Path Resolution Verification
- `package.json` script entry points updated:
  - `"lint:exams": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs"`
  - `"check:assets": "node scripts/pipeline/lint/check_assets.mjs"`
  - `"build": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs && tsc && vite build"`
  - `"build:images": "node scripts/pipeline/utils/build_image_index.mjs"`
- Unit test import paths updated:
  - `scripts/__tests__/build_image_index.test.mjs`: `import { scanDir, buildImageIndex } from '../pipeline/utils/build_image_index.mjs';`
  - `scripts/__tests__/lint_exam_json.test.mjs`: `import { lintExamFile, runLinter } from '../pipeline/lint/lint_exam_json.mjs';`
  - `scripts/__tests__/test_extract_and_attach_images.py`: `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'ingest')))`
- Relocated Linters Path Resolution:
  - `check_assets.mjs`: `const PUBLIC_DIR = path.resolve(__dirname, '../../../public');`
  - `lint_exam_json.mjs`: `const SERVER_DATA_DIR = path.resolve(__dirname, '../../../public/server-data');`
  - `lint_tutorial_json.mjs`: `const PUBLIC_DIR = path.resolve(__dirname, '../../../public');`

#### 3. ESM Export & Guard Verification
In `scripts/pipeline/utils/build_image_index.mjs`:
```javascript
export { scanDir };
export function buildImageIndex() { ... }

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  buildImageIndex();
}
```
This enables Vitest to import `scanDir` and `buildImageIndex` without triggering side-effects upon file import.

#### 4. AGENTS.md Governance Clarification
Lines 22–24 of `AGENTS.md`:
```markdown
- **Red Zone vs. Green Zone 治理邊界**:
  - **Red Zone (絕對禁區)**: 對考題內文 (`stem`)、選項 (`options`)、解說 (`sourceExplanation`) 等文字內容進行 Regex 抓取、段落切分、換行插入或機械取代為嚴格禁止之紅線。
  - **Green Zone (合規系統工具)**: 置於 `scripts/pipeline/` 下的 JSON schema linters (`scripts/pipeline/lint/lint_exam_json.mjs`)、靜態資產檢查器 (`scripts/pipeline/lint/check_assets.mjs`) 與管道狀態腳本為合法且合規之系統工具，不屬於 Red Zone 切分改寫行為。
```

---

### Command Output Log Evidence

#### `npm run build:images`
```text
> exam-prepare-site@1.0.0 build:images
> node scripts/pipeline/utils/build_image_index.mjs

Indexing and copying KDIGO & Brenner 11e images...
[SUCCESS] Indexed and copied 2762 images to /Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/image_index.json
```

#### `npm run lint:exams`
```text
> exam-prepare-site@1.0.0 lint:exams
> node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs

🔍 Running Exam JSON Static Linter (Checking Schema Keys, Synthetic Headers & Broken Sentences)...
📊 Checked exams_manifest.json (SCHEMA VALID) and 103 exam database JSON files.
✅ Exam JSON Lint Passed! All manifest schemas and exam files are clean (0 synthetic headers, 0 broken sentences, 0 schema key violations).
📘 Running Tutorial JSON Diagram & Schema Linter...
📊 Scanned 77 tutorial JSON files in server-data/tutorials.
✅ Tutorial Linter Passed! All tutorial diagram schemas and image paths are valid.
🖼️  Running Server Data Asset Integrity Checker...
📊 Scanned 180 JSON database files across server-data.
✅ Asset Verification Passed! All referenced image assets exist on disk.
```

#### `npm run test`
```text
 Test Files  14 passed (14)
      Tests  98 passed (98)
   Start at  22:18:09
   Duration  1.57s
```

#### `npm run test:py`
```text
scripts/__tests__/test_extract_and_attach_images.py ..                   [100%]
============================== 2 passed in 0.10s ===============================
```

---

### Final Verdict

**CLEAN**: All checks passed with 100% integrity compliance. Phase 2 Script Modularization is fully verified and ready for completion.

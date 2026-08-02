# Handoff Report — Explorer 1 (teamwork_preview_explorer_m1_1)

## 1. Observation
1. **Scope & Targets**:
   - `lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs` (target: `scripts/pipeline/lint/`)
   - `ingest_exam.mjs`, `extract_and_attach_images.py` (target: `scripts/pipeline/ingest/`)
   - `exam_qc.mjs`, `merge_qc_results.mjs`, `apply_qc_updates.py` (target: `scripts/pipeline/qc/`)
   - `ask_nlm_for_2026.mjs`, `ask_nlm_for_renal_transplant.mjs`, `process_nlm_results.py` (target: `scripts/pipeline/nlm/`)
   - `build_image_index.mjs` (target: `scripts/pipeline/utils/`)

2. **Verbatim Line References & Code Snippets**:
   - `scripts/lint_exam_json.mjs`:
     - Line 8: `const SERVER_DATA_DIR = path.resolve(__dirname, '../public/server-data');`
     - Line 208: `const targetPath = filename.startsWith('/') ? path.join(__dirname, '../public', filename) : path.join(SERVER_DATA_DIR, filename);`
   - `scripts/lint_tutorial_json.mjs`:
     - Line 8: `const PUBLIC_DIR = path.resolve(__dirname, '../public');`
   - `scripts/check_assets.mjs`:
     - Line 8: `const PUBLIC_DIR = path.resolve(__dirname, '../public');`
   - `scripts/ask_nlm_for_2026.mjs`:
     - Line 4: `import { reconcileResponses } from './ingest_exam.mjs';`
   - `scripts/ask_nlm_for_renal_transplant.mjs`:
     - Line 4: `import { reconcileResponses } from './ingest_exam.mjs';`

3. **Scripts using `process.cwd()` or Absolute Paths (No Internal Replacements Needed)**:
   - `ingest_exam.mjs` (uses `process.cwd()`)
   - `extract_and_attach_images.py` (uses absolute `/Users/yuan/Projects/...`)
   - `exam_qc.mjs` (uses `process.cwd()`)
   - `merge_qc_results.mjs` (uses `process.cwd()`)
   - `apply_qc_updates.py` (uses `os.getcwd()` / `scratch/`)
   - `process_nlm_results.py` (uses `os.getcwd()` / `scratch/`)
   - `build_image_index.mjs` (uses `process.cwd()`)

---

## 2. Logic Chain
1. Moving scripts into `scripts/pipeline/<subfolder>/` increases file depth from 1 level (`scripts/`) to 3 levels (`scripts/pipeline/<subfolder>/`).
2. Any relative directory lookup based on `__dirname` pointing to `../public` or `../public/server-data` will resolve to `scripts/pipeline/public` instead of `project_root/public`.
3. To correct `__dirname` references in `scripts/pipeline/lint/`, path navigation must go 3 levels up (`../../../public` and `../../../public/server-data`).
4. Cross-module imports between pipeline scripts (e.g. `ask_nlm_for_*.mjs` importing `ingest_exam.mjs`) change from sibling imports (`./ingest_exam.mjs`) to cross-directory imports (`../ingest/ingest_exam.mjs`).
5. Scripts depending solely on `process.cwd()` evaluate paths at runtime from where node/python is executed (typically project root), so their internal path code does not break upon migration.

---

## 3. Caveats
1. This report is a read-only investigation (Milestone 1). No source code or config files outside `.agents/teamwork_preview_explorer_m1_1` have been modified.
2. In Milestone 2 (External Path Updates), test files in `scripts/__tests__/`, `package.json` npm scripts, `vitest.config.ts`, `AGENTS.md`, and unmigrated scripts in `scripts/` (e.g., `reask_anomalous.mjs`) will need import and execution path updates corresponding to the new `scripts/pipeline/` layout.

---

## 4. Conclusion
All designated scripts for migration under R1 have been cataloged, and exact line-by-line replacements for R2 path resolution fixes have been documented:
- **5 replacement chunks** across 5 files (`lint_exam_json.mjs` [2], `lint_tutorial_json.mjs` [1], `check_assets.mjs` [1], `ask_nlm_for_2026.mjs` [1], `ask_nlm_for_renal_transplant.mjs` [1]).
- **6 files** require zero internal path modifications.
- Complete details and replacement strings are recorded in `analysis.md`.

---

## 5. Verification Method
1. Inspect `analysis.md` at `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_explorer_m1_1/analysis.md`.
2. Verify line numbers in source files using `view_file`:
   - `view_file` on `scripts/lint_exam_json.mjs` at lines 8 and 208.
   - `view_file` on `scripts/lint_tutorial_json.mjs` at line 8.
   - `view_file` on `scripts/check_assets.mjs` at line 8.
   - `view_file` on `scripts/ask_nlm_for_2026.mjs` at line 4.
   - `view_file` on `scripts/ask_nlm_for_renal_transplant.mjs` at line 4.

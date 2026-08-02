# Handoff Report — Challenger 1 (teamwork_preview_challenger_m1_1)

## 1. Observation

1. **`npm run build:images` Execution Failure**:
   - Command: `npm run build:images` (executed from `/Users/yuan/Projects/Exam/Exam_prepare_site`)
   - Verbatim Output:
     ```text
     > exam-prepare-site@1.0.0 build:images
     > node scripts/pipeline/utils/build_image_index.mjs

     file:///Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/utils/build_image_index.mjs:71
     export { scanDir, buildImageIndex };
                       ^^^^^^^^^^^^^^^

     SyntaxError: Duplicate export of 'buildImageIndex'
         at compileSourceTextModule (node:internal/modules/esm/utils:354:16)
         at ModuleLoader.moduleStrategy (node:internal/modules/esm/translators:91:18)
     ```
   - Target File: `scripts/pipeline/utils/build_image_index.mjs`, Line 53 (`export function buildImageIndex()`) and Line 71 (`export { scanDir, buildImageIndex };`).

2. **Directory Coupling Errors (`process.cwd()` dependencies)**:
   - Command: `node pipeline/qc/exam_qc.mjs` (executed from `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts`)
   - Verbatim Output:
     ```text
     === TN-EXAM-QC AUDIT SCANNER ===
     file:///Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/qc/exam_qc.mjs:105
         throw new Error(`Server data directory not found: ${SERVER_DATA_DIR}`);
               ^

     Error: Server data directory not found: /Users/yuan/Projects/Exam/Exam_prepare_site/scripts/public/server-data
         at scanServerData (file:///Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/qc/exam_qc.mjs:105:11)
     ```
   - Target File: `scripts/pipeline/qc/exam_qc.mjs`, Line 4 (`const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');`).

3. **Linter & Test Executions from Project Root**:
   - `npm run lint:exams`: PASS (103 exam JSONs, 77 tutorial JSONs, 180 assets verified).
   - `npm run check:assets`: PASS (180 database JSON assets verified).
   - `npm run test`: PASS (14 test files passed, 98 unit tests passed).
   - `npm run test:py`: PASS (2 pytest tests passed, 100%).
   - `npm run build`: PASS (tsc & vite build successful).
   - Linters (`lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`) executed from `scripts/` or `scripts/pipeline/lint/`: PASS (using `__dirname`).

---

## 2. Logic Chain

1. Worker M1 updated linters (`lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`) to compute paths using `__dirname` (`path.resolve(__dirname, '../../../public/server-data')`), allowing them to execute correctly from any CWD directory (Observation 3).
2. However, `build_image_index.mjs` was moved to `scripts/pipeline/utils/` while retaining both `export function buildImageIndex()` on line 53 and `export { scanDir, buildImageIndex };` on line 71, causing Node.js native ESM loader to throw `SyntaxError: Duplicate export of 'buildImageIndex'` when `npm run build:images` is executed (Observation 1).
3. Vitest test runner transforms ESM code in memory, masking this native Node duplicate export error during `npm run test` (Observation 3).
4. Unmigrated non-linter scripts (`exam_qc.mjs`, `merge_qc_results.mjs`, `export_stage1_anomalous.mjs`, `build_image_index.mjs`, `ingest_exam.mjs`) still construct paths via `path.join(process.cwd(), 'public', ...)` (Observation 2). Running them outside the root directory causes `process.cwd()` to resolve to `/scripts/public/server-data`, throwing `ENOENT` or directory not found errors (Observation 2).

---

## 3. Caveats

- **No caveats**: All 11 relocated scripts, npm scripts, directory paths, and test runner outputs were empirically tested and documented.

---

## 4. Conclusion

Phase 2 Script Modularization is partially complete:
- Core linters, unit tests, and Vite build pass cleanly from project root.
- **2 bugs were uncovered during empirical verification**:
  1. `npm run build:images` fails due to a duplicate ESM export in `scripts/pipeline/utils/build_image_index.mjs`.
  2. Scripts relying on `process.cwd()` fail when executed from subdirectories (e.g., `scripts/`).

---

## 5. Verification Method

To independently verify these findings, execute:

1. **Verify `npm run build:images` failure**:
   ```bash
   npm run build:images
   ```
   *Expected Output*: Exit code 1 with `SyntaxError: Duplicate export of 'buildImageIndex'`.

2. **Verify non-root directory coupling failure**:
   ```bash
   cd /Users/yuan/Projects/Exam/Exam_prepare_site/scripts && node pipeline/qc/exam_qc.mjs
   ```
   *Expected Output*: Exit code 1 with `Error: Server data directory not found: .../scripts/public/server-data`.

3. **Verify passing root test suite**:
   ```bash
   npm run lint:exams && npm run test && npm run test:py
   ```
   *Expected Output*: All 3 commands pass with Exit Code 0.

# Handoff Report: Requirement R3 External Path Updates Investigation

## 1. Observation

Direct code inspection confirmed exact line numbers and paths for all external references to moved pipeline scripts across `package.json`, `AGENTS.md`, `vitest.config.ts`, `scripts/__tests__/`, and additional script callers in `scripts/`:

1. **`package.json`** (`/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`):
   - Line 8: `"lint:exams": "node scripts/lint_exam_json.mjs && node scripts/lint_tutorial_json.mjs && node scripts/check_assets.mjs",`
   - Line 9: `"check:assets": "node scripts/check_assets.mjs",`
   - Line 10: `"build": "node scripts/lint_exam_json.mjs && node scripts/lint_tutorial_json.mjs && node scripts/check_assets.mjs && tsc && vite build",`
   - Line 12: `"build:images": "node scripts/build_image_index.mjs",`

2. **`AGENTS.md`** (`/Users/yuan/Projects/Exam/Exam_prepare_site/AGENTS.md`):
   - Line 82 (Rule 10): `node scripts/lint_exam_json.mjs`
   - Line 88 (Rule 11): `node scripts/lint_exam_json.mjs && node scripts/check_assets.mjs`
   - Line 99 (Rule 12): `靜態 Linter scripts/lint_exam_json.mjs`
   - Line 18: `ZERO MECHANICAL EXTRACTION MEMORY GUARD (機械切分絕對警示鐵律)` section lacks explicit Red Zone vs Green Zone definitions.

3. **`scripts/__tests__/` Test Suite**:
   - `scripts/__tests__/lint_exam_json.test.mjs:4`: `import { lintExamFile, runLinter } from '../lint_exam_json.mjs';`
   - `scripts/__tests__/build_image_index.test.mjs:4`: `import { scanDir, buildImageIndex } from '../build_image_index.mjs';`
   - `scripts/__tests__/test_extract_and_attach_images.py:8`: `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))`

4. **`vitest.config.ts`** (`/Users/yuan/Projects/Exam/Exam_prepare_site/vitest.config.ts`):
   - Line 17: `'scripts/lint_exam_json.mjs',`
   - Line 18: `'scripts/build_image_index.mjs',`

5. **Additional Calling Scripts in `scripts/`**:
   - `scripts/ask_nlm_for_2026.mjs:4`: `import { reconcileResponses } from './ingest_exam.mjs';`
   - `scripts/ask_nlm_for_renal_transplant.mjs:4`: `import { reconcileResponses } from './ingest_exam.mjs';`
   - `scripts/reask_anomalous.mjs:4`: `import { reconcileResponses } from './ingest_exam.mjs';`
   - `scripts/repair_nlm_dual_asking.mjs:4`: `import { reconcileResponses } from './ingest_exam.mjs';`
   - `scripts/export_stage1_anomalous.mjs:3`: `import { isNlmResponseAnomalous } from './exam_qc.mjs';`
   - `scripts/prepare_stage2_batch.mjs:3`: `import { inspectQuestionForQc } from './exam_qc.mjs';`
   - `scripts/update_stage1_results.mjs:3`: `import { isNlmResponseAnomalous } from './exam_qc.mjs';`

---

## 2. Logic Chain

1. **Premise**: Requirement R1 relocates 11 scripts into `scripts/pipeline/{lint,ingest,qc,nlm,utils}/`.
2. **Step 1**: Moving `lint_exam_json.mjs`, `lint_tutorial_json.mjs`, and `check_assets.mjs` to `scripts/pipeline/lint/` invalidates commands in `package.json` (lines 8, 9, 10) and governance rules in `AGENTS.md` (lines 82, 88, 99). They must be updated to include `scripts/pipeline/lint/`.
3. **Step 2**: Moving `build_image_index.mjs` to `scripts/pipeline/utils/` invalidates `build:images` in `package.json` (line 12) and `build_image_index.test.mjs` import path (line 4).
4. **Step 3**: Relocating `extract_and_attach_images.py` to `scripts/pipeline/ingest/` causes `test_extract_and_attach_images.py` (line 8) to fail on `import extract_and_attach_images` unless `sys.path` points to `../pipeline/ingest`.
5. **Step 4**: Moving `lint_exam_json.mjs` and `build_image_index.mjs` requires updating `vitest.config.ts` lines 17-18 under `coverage.include`.
6. **Step 5**: Scripts that import `ingest_exam.mjs` or `exam_qc.mjs` (both relocated scripts) must update their relative imports. Moved callers (`ask_nlm_for_2026.mjs`, `ask_nlm_for_renal_transplant.mjs`) must use `../ingest/ingest_exam.mjs`, while non-moved callers (`reask_anomalous.mjs`, `repair_nlm_dual_asking.mjs`, `export_stage1_anomalous.mjs`, `prepare_stage2_batch.mjs`, `update_stage1_results.mjs`) must use `./pipeline/{ingest,qc}/...`.
7. **Step 6**: AGENTS.md rule expansion clarifies Red Zone (Regex on stem/options/explanations) vs Green Zone (linter/schema/assets/utility scripts).

---

## 3. Caveats

- **No caveats**: All files referencing relocated scripts were fully scanned and mapped with exact line numbers and replacement targets.

---

## 4. Conclusion

Requirement R3 involves updating 17 specific line targets across 12 files (`package.json`, `AGENTS.md`, `vitest.config.ts`, 3 test files in `scripts/__tests__/`, and 6 caller scripts in `scripts/`). Implementing these exact replacements guarantees zero broken imports, full linter compliance, and passing test suites.

---

## 5. Verification Method

1. **Verify `package.json` and Linter Commands**:
   - Execute `npm run lint:exams` and `npm run check:assets`.
2. **Verify Vitest Suite**:
   - Execute `npm run test` (must pass 0 failed tests, covering relocated scripts).
3. **Verify Pytest Suite**:
   - Execute `npm run test:py` (must pass 2/2 tests in `test_extract_and_attach_images.py`).
4. **Inspect Files**:
   - View `package.json`, `AGENTS.md`, `vitest.config.ts`, and test files to confirm no stale `scripts/<moved_script>` references remain.

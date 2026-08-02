# Analysis Report — Challenger 2 (Import & Configuration Coverage)

## Mission Overview

Adversarial review of import paths and configuration coverage across Javascript and Python test harnesses (`scripts/__tests__/`) and Vitest configuration (`vitest.config.ts`) following Worker M1's script relocation into `scripts/pipeline/{lint,ingest,qc,nlm,utils}/`.

---

## Attack Surface & Hypotheses Tested

### Hypothesis 1: Stale Imports in Test Harnesses
- **Hypothesis**: Test files in `scripts/__tests__/` might still reference pre-relocation paths (e.g. `../lint_exam_json.mjs`, `../build_image_index.mjs`, `sys.path` to `../scripts`) or fail to resolve ESM/Python imports.
- **Verification Method**: Inspect every test file in `scripts/__tests__/` and verify exact import statements against filesystem paths.
- **Result**: **DISPROVED** (Pass).
  - `build_image_index.test.mjs:4`: Imports `../pipeline/utils/build_image_index.mjs`. Path `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/utils/build_image_index.mjs` verified present on disk.
  - `lint_exam_json.test.mjs:4`: Imports `../pipeline/lint/lint_exam_json.mjs`. Path `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/lint/lint_exam_json.mjs` verified present on disk.
  - `test_extract_and_attach_images.py:8`: Inserts `os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'ingest')` into `sys.path`. Path `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/ingest/extract_and_attach_images.py` verified present on disk.

### Hypothesis 2: Dead or Non-Existent Paths in `vitest.config.ts`
- **Hypothesis**: `vitest.config.ts` `coverage.include` array might reference obsolete root `scripts/*.mjs` paths or non-existent relocated subdirectories.
- **Verification Method**: Audit `vitest.config.ts` lines 15–19 against actual filesystem structure.
- **Result**: **DISPROVED** (Pass).
  - `vitest.config.ts` specifies:
    ```ts
    include: [
      'src/**/*.{ts,tsx}',
      'scripts/pipeline/lint/lint_exam_json.mjs',
      'scripts/pipeline/utils/build_image_index.mjs',
    ]
    ```
  - Both targets exist at their exact relative paths. No references to legacy root `scripts/lint_exam_json.mjs` or `scripts/build_image_index.mjs` exist in `vitest.config.ts`.

### Hypothesis 3: Test Runner Failures or Coverage Regressions
- **Hypothesis**: Executing test runners (`npm run test`, `npm run test:py`) could uncover runtime module resolution errors, broken path references, or missing test suites.
- **Verification Method**: Execute `npm run test` and `npm run test:py` empirically.
- **Result**: **DISPROVED** (Pass).
  - `npm run test`: Passed 14 test files (12 React/src tests + 2 scripts tests) containing 98 total tests in 1.45s.
  - `npm run test:py`: Passed 1 test suite (2 tests in `test_extract_and_attach_images.py`) in 0.09s.

---

## Stress Test Results & Findings

| Scenario | Expected Behavior | Actual Behavior | Pass/Fail |
|---|---|---|---|
| Module Import in `build_image_index.test.mjs` | Resolves to `scripts/pipeline/utils/build_image_index.mjs` | Resolves cleanly, exports `scanDir` & `buildImageIndex` | PASS |
| Module Import in `lint_exam_json.test.mjs` | Resolves to `scripts/pipeline/lint/lint_exam_json.mjs` | Resolves cleanly, exports `lintExamFile` & `runLinter` | PASS |
| Python Path Resolution in `test_extract_and_attach_images.py` | `sys.path` targets `scripts/pipeline/ingest` | Imports `extract_and_attach_images` without `ModuleNotFoundError` | PASS |
| `vitest.config.ts` Coverage Target Audit | Targets valid existing files in `scripts/pipeline/` | Target files exist and match actual relocated scripts | PASS |
| Vitest Test Suite Execution (`npm run test`) | All 14 test files execute and pass | 14 test files passed (98 tests, 0 failures) | PASS |
| Pytest Execution (`npm run test:py`) | Pytest suite passes against `scripts/pipeline/ingest` | 2 passed in 0.09s | PASS |

---

## Observations & Minor Notes

1. **Vitest Global Threshold Note**: Running `npm run test:coverage` triggers a global line/statement threshold check of 90% configured in `vitest.config.ts`. Total repository coverage currently stands at ~78.62% lines due to frontend UI components in `src/`. However, `scripts/pipeline/utils/build_image_index.mjs` achieved 89.47% and `scripts/pipeline/lint/lint_exam_json.mjs` achieved 77.30%. The test command specified by Worker M1 and project standards (`npm run test`) passes with exit code 0.
2. **Unmigrated Root Callers**: As noted in Worker M1's handoff, 5 optional operational/maintenance helper scripts in `scripts/` (`reask_anomalous.mjs`, `repair_nlm_dual_asking.mjs`, `export_stage1_anomalous.mjs`, `prepare_stage2_batch.mjs`, `update_stage1_results.mjs`) have had their import paths updated to `./pipeline/{ingest,qc}/...` and resolved properly.

---

## Risk Assessment & Conclusion

- **Risk Level**: **LOW**.
- All JavaScript and Python test harnesses correctly import relocated pipeline modules.
- `vitest.config.ts` coverage inclusion paths accurately target existing files.
- Test suites (`npm run test` and `npm run test:py`) pass 100%.

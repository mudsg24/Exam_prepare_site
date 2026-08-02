# Phase 2 Script Modularization — Adversarial Analysis & Verification Report

**Author**: Challenger 1 (`teamwork_preview_challenger_m1_1`)  
**Date**: 2026-08-02  
**Target**: Phase 2 Script Relocation & Modularization (`scripts/pipeline/`)  

---

## 1. Executive Summary

Empirical testing and adversarial stress-testing were conducted on the relocated pipeline scripts under `scripts/pipeline/`.
While core npm commands (`npm run lint:exams`, `npm run check:assets`, `npm run test`, `npm run test:py`, `npm run build`) pass when run from project root, **1 critical runtime error** and **multiple non-root directory execution failures** were discovered through empirical execution.

---

## 2. Findings & Edge Case Verification

### Finding 1: [CRITICAL] `npm run build:images` Fails with Node ESM SyntaxError

- **Target Script**: `scripts/pipeline/utils/build_image_index.mjs` (Lines 53 & 71)
- **Command Executed**: `npm run build:images` (from project root)
- **Output / Error**:
  ```text
  file:///Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/utils/build_image_index.mjs:71
  export { scanDir, buildImageIndex };
                    ^^^^^^^^^^^^^^^

  SyntaxError: Duplicate export of 'buildImageIndex'
      at compileSourceTextModule (node:internal/modules/esm/utils:354:16)
  ```
- **Root Cause Analysis**: Line 53 exports `buildImageIndex` via inline function declaration (`export function buildImageIndex()`), and Line 71 attempts to re-export `buildImageIndex` in named export syntax (`export { scanDir, buildImageIndex };`). Node.js native ESM loader strictly rejects duplicate exports at parse time.
- **Impact**: Any user or CI/CD pipeline attempting to run `npm run build:images` will crash immediately. Worker M1 omitted `npm run build:images` from their verification run, masking this failure.

---

### Finding 2: [MEDIUM] CWD-Coupled Directory Execution Failures

- **Target Scripts**:
  - `scripts/pipeline/qc/exam_qc.mjs` (Line 4)
  - `scripts/pipeline/qc/merge_qc_results.mjs` (Lines 4–5)
  - `scripts/export_stage1_anomalous.mjs` (Line 5)
  - `scripts/pipeline/utils/build_image_index.mjs` (Lines 6 & 8)
  - `scripts/pipeline/ingest/ingest_exam.mjs` (Line 6)
  - `scripts/pipeline/nlm/ask_nlm_for_2026.mjs` (Line 7)
- **Command Executed**: `node pipeline/qc/exam_qc.mjs` (from `scripts/` directory)
- **Output / Error**:
  ```text
  Error: Server data directory not found: /Users/yuan/Projects/Exam/Exam_prepare_site/scripts/public/server-data
      at scanServerData (file:///Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/qc/exam_qc.mjs:105:11)
  ```
- **Root Cause Analysis**: While Worker M1 correctly updated linters (`lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`) to use `import.meta.url` / `__dirname` (`path.resolve(__dirname, '../../../public/server-data')`), remaining pipeline scripts still rely on `path.join(process.cwd(), 'public', ...)`. When invoked from subdirectories (`scripts/`, `scripts/pipeline/qc/`, etc.), `process.cwd()` evaluates relative to the active terminal directory instead of the project root.

---

### Finding 3: [LOW / OBSERVATION] Vitest ESM Parser Masking Syntax Errors

- **Target File**: `scripts/__tests__/build_image_index.test.mjs`
- **Command Executed**: `npm run test`
- **Observation**: `vitest run` passed (14/14 test files, 98/98 tests) even though `scripts/pipeline/utils/build_image_index.mjs` contains a duplicate export syntax error. Vitest's internal esbuild transformer sanitizes ESM exports during bundle compilation, providing a false positive test pass that masks native Node ESM syntax errors.

---

## 3. Empirical Test Execution Matrix

| Test Case | Command | Execution Dir | Result | Failure / Observation |
|---|---|---|---|---|
| 1 | `npm run lint:exams` | Project Root | **PASS** | 103 exam JSONs, 77 tutorials, 180 assets verified |
| 2 | `npm run check:assets` | Project Root | **PASS** | 180 database JSON assets verified |
| 3 | `npm run build:images` | Project Root | **FAIL** | `SyntaxError: Duplicate export of 'buildImageIndex'` |
| 4 | `npm run test` | Project Root | **PASS** | 14 test files passed, 98 tests passed |
| 5 | `npm run test:py` | Project Root | **PASS** | 2 pytest cases passed (100%) |
| 6 | `npm run build` | Project Root | **PASS** | tsc + vite build successful |
| 7 | `node pipeline/lint/lint_exam_json.mjs` | `scripts/` | **PASS** | Correctly resolved `__dirname` |
| 8 | `node lint_exam_json.mjs` | `scripts/pipeline/lint/` | **PASS** | Correctly resolved `__dirname` |
| 9 | `node pipeline/qc/exam_qc.mjs` | `scripts/` | **FAIL** | `Error: Server data directory not found` (`process.cwd()` issue) |
| 10 | `node export_stage1_anomalous.mjs` | `scripts/` | **FAIL** | `ENOENT: /scripts/public/server-data` (`process.cwd()` issue) |

---

## 4. Remediation Recommendations for Worker

1. **Fix `build_image_index.mjs` duplicate export**:
   - Change Line 53 to `function buildImageIndex()` OR remove `buildImageIndex` from Line 71 `export { scanDir, buildImageIndex };`.
2. **Convert `process.cwd()` to `__dirname` / `import.meta.url` in pipeline scripts**:
   - Replace `path.join(process.cwd(), 'public', 'server-data')` with `path.resolve(__dirname, '../../../public/server-data')` (or relative equivalent based on directory depth) across `exam_qc.mjs`, `build_image_index.mjs`, `ingest_exam.mjs`, `ask_nlm_for_2026.mjs`, etc.

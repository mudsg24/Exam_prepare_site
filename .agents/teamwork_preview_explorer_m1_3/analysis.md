# Detailed Analysis: Testing Baseline & Acceptance Criteria Verification

## 1. Executive Summary

本報告為 `Exam_prepare_site` Phase 2 Script Modularization 之 **Testing Baseline & Acceptance Criteria Verification** 的完整調查分析。

本調查針對三個核心命令 (`npm run lint:exams`, `npm run test`, `npm run test:py`) 進行了深入盤點、執行機制解析、現有 Unit Tests 與 Test Fixtures 之引用關係梳理，並建立了 Pre-migration Baseline 狀態。同時，本報告詳細剖析了腳本移轉至 `scripts/pipeline/{lint,ingest,qc,nlm,utils}/` 後，可能導致測試與工具鏈斷裂的關鍵 Pitfalls，並提出完整的驗證防護措施。

---

## 2. Command Execution & Test Suite Setup

### 2.1 `npm run lint:exams`

- **Execution Command**:
  `node scripts/lint_exam_json.mjs && node scripts/lint_tutorial_json.mjs && node scripts/check_assets.mjs`
- **Execution Mechanism**:
  透過 Node.js CLI 依序串行執行 3 個靜態檢查腳本：
  1. `lint_exam_json.mjs`: 掃描 `public/server-data/` 下 103 個試題 JSON 及 `exams_manifest.json`，檢查 Schema Keys、Synthetic Headers (如 `**History & Clinical Presentation:**`)、Broken Sentences (`\n\n` between lowercase words)、Unescaped Tildes (`~`) 以及 Wall of Text。
  2. `lint_tutorial_json.mjs`: 掃描 `public/server-data/tutorials/` 下 77 個教學講堂 JSON，驗證 Diagram Schema、`imagePath` 與相對路徑結構。
  3. `check_assets.mjs`: 掃描 `public/server-data/` 所有 180 個 JSON 檔案，驗證所有被引用的圖片 Asset 檔案（如 `/reference-images/...` 或 `/server-data/assets/...`）在 `public/` 磁碟上皆真實存在。
- **Associated Pipeline Scripts**:
  - `scripts/lint_exam_json.mjs` -> 移至 `scripts/pipeline/lint/lint_exam_json.mjs`
  - `scripts/lint_tutorial_json.mjs` -> 移至 `scripts/pipeline/lint/lint_tutorial_json.mjs`
  - `scripts/check_assets.mjs` -> 移至 `scripts/pipeline/lint/check_assets.mjs`

### 2.2 `npm run test` (Vitest)

- **Execution Command**:
  `vitest run`
- **Configuration File**: `vitest.config.ts`
  - `test.globals`: `true`
  - `test.environment`: `'jsdom'`
  - `test.setupFiles`: `['./src/__tests__/setup.ts']`
  - `test.include`: `['src/**/*.{test,spec}.{ts,tsx}', 'scripts/__tests__/**/*.{test,spec}.mjs']`
  - `test.coverage.include`: `['src/**/*.{ts,tsx}', 'scripts/lint_exam_json.mjs', 'scripts/build_image_index.mjs']`
- **Existing Test Files Inventory**:
  1. `src/` UI / Utility Unit & Integration Tests (12 test files, 96 tests):
     - `src/__tests__/App.test.tsx` (9 tests)
     - `src/components/__tests__/DashboardView.test.tsx` (12 tests)
     - `src/components/__tests__/DisputeBadge.test.tsx`
     - `src/components/__tests__/ExplanationPanel.test.tsx` (11 tests)
     - `src/components/__tests__/Header.test.tsx` (10 tests)
     - `src/components/__tests__/ImageModal.test.tsx`
     - `src/components/__tests__/QuestionMatrix.test.tsx`
     - `src/components/__tests__/QuestionPanel.test.tsx` (9 tests)
     - `src/components/__tests__/TutorialReaderView.test.tsx`
     - `src/utils/__tests__/imageUtils.test.ts`
     - `src/utils/__tests__/katexRenderer.test.ts`
     - `src/utils/__tests__/markdownRenderer.test.ts`
  2. `scripts/__tests__/` JavaScript Script Unit Tests (2 test files, 2 suites):
     - `scripts/__tests__/lint_exam_json.test.mjs`:
       - Imports target module via relative path: `import { lintExamFile, runLinter } from '../lint_exam_json.mjs';`
       - Test cases: Ignore manifest/image_index/non-json, return error for malformed JSON, return empty if no questions, detect synthetic headers, detect broken sentences, detect unescaped tildes / wall of text warnings, detect empty stem / insufficient options, execute `runLinter()`.
       - Fixture management: Dynamic temp directory `path.resolve(__dirname, './tmp_lint_tests')` created in `beforeEach` and force-removed in `afterEach`.
     - `scripts/__tests__/build_image_index.test.mjs`:
       - Imports target module via relative path: `import { scanDir, buildImageIndex } from '../build_image_index.mjs';`
       - Test cases: Return empty array for non-existent dir, recursively scan directory and copy images, execute `buildImageIndex()`.
       - Fixture management: Dynamic temp directory `path.resolve(__dirname, './tmp_img_src')` created in `beforeEach` and force-removed in `afterEach`.

### 2.3 `npm run test:py` (Pytest)

- **Execution Command**:
  `pytest --cov=scripts scripts/__tests__/`
- **Execution Mechanism**:
  呼叫 `pytest` 對 `scripts/__tests__/` 目錄下所有以 `test_*.py` 命名的 Python 測試檔進行測試，並透過 `--cov=scripts` 收集 `scripts` 目錄下 Python 腳本的 Code Coverage。
- **Existing Test Files Inventory**:
  - `scripts/__tests__/test_extract_and_attach_images.py`:
    - `sys.path` Manipulation:
      `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))`
    - Imports target module: `import extract_and_attach_images`
    - Test cases:
      1. `test_extract_images_from_invalid_docx`: 建立無效 Zip 格式之 `.docx` 暫存檔，驗證 `extract_images_from_docx` 回傳 `[]` 且不會拋出致命 Exception。
      2. `test_process_all_papers_no_files`: 使用 `unittest.mock.patch` 模擬 `extract_and_attach_images.get_paper_mappings` 與 `extract_and_attach_images.find_source_docx_files` 回傳空清單，驗證 `process_all_papers()` 執行順暢且 Mock 方法被正確認用。

---

## 3. Pre-Migration Baseline Status

在未進行任何腳本搬移前的 Baseline 測試執行結果如下：

| Command | Status | Result Summary | Details |
|---|---|---|---|
| `npm run lint:exams` | **PASSED** | 0 errors, 0 warnings | Checked `exams_manifest.json` + 103 exam JSONs, 77 tutorial JSONs, 180 total JSON asset paths. All clean. |
| `npm run test` (vitest) | **PASSED** | 14 test files passed, 98 tests passed | Executed in 1.75s. All 98 UI & script unit tests passed. |
| `npm run test:py` (pytest) | **PASSED** | 2 passed in 0.09s | Executed `test_extract_and_attach_images.py` successfully. |

> **Note on Coverage**:
> 執行 `npm run test:coverage` 時，Vitest Coverage report 會因為 `src/` UI coverage 尚未達 90% threshold 而回傳 exit code 1。然而，Acceptance Criteria 所規定的 `npm run test` (Vitest) 執行結果為 100% 通過 (14 test files passed, 98 tests passed)。

---

## 4. Migration Pitfalls & Potential Breakages

當 Phase 2 執行腳本移轉至 `scripts/pipeline/{lint,ingest,qc,nlm,utils}/` 時，下列 5 大潛在連鎖破壞點必須同步修復：

### Pitfall 1: `scripts/__tests__/` JavaScript Test Import Path Breakage
- **Affected Files**:
  - `scripts/__tests__/lint_exam_json.test.mjs` (Line 4)
  - `scripts/__tests__/build_image_index.test.mjs` (Line 4)
- **Breakage Cause**:
  目前引用路徑為 `../lint_exam_json.mjs` 與 `../build_image_index.mjs`（相對於 `scripts/__tests__` 即指向 `scripts/`）。當腳本搬移至 `scripts/pipeline/lint/` 與 `scripts/pipeline/utils/` 後，直接執行 `npm run test` 將拋出 `ERR_MODULE_NOT_FOUND` 錯誤。
- **Remediation**:
  - `lint_exam_json.test.mjs`: 將 `../lint_exam_json.mjs` 改為 `../pipeline/lint/lint_exam_json.mjs`
  - `build_image_index.test.mjs`: 將 `../build_image_index.mjs` 改為 `../pipeline/utils/build_image_index.mjs`

### Pitfall 2: `scripts/__tests__/` Python `sys.path` & Module Import Breakage
- **Affected File**:
  - `scripts/__tests__/test_extract_and_attach_images.py` (Lines 8, 10, 20, 21)
- **Breakage Cause**:
  `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))` 僅將 `scripts/` 加入 Python 模組搜尋路徑。當 `extract_and_attach_images.py` 移至 `scripts/pipeline/ingest/` 後，`import extract_and_attach_images` 與 `@patch("extract_and_attach_images...")` 將拋出 `ModuleNotFoundError`。
- **Remediation**:
  將 `sys.path.insert` 改為包含 `../pipeline/ingest` 的絕對路徑：
  `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../pipeline/ingest')))`

### Pitfall 3: `vitest.config.ts` Coverage Include Path Mismatch
- **Affected File**:
  - `vitest.config.ts` (Lines 17-18)
- **Breakage Cause**:
  `coverage.include` 硬編碼為 `'scripts/lint_exam_json.mjs'` 與 `'scripts/build_image_index.mjs'`。若未同步更新，Vitest coverage 收集將無法配對已移轉之腳本。
- **Remediation**:
  更新為 `'scripts/pipeline/lint/lint_exam_json.mjs'` 與 `'scripts/pipeline/utils/build_image_index.mjs'`。

### Pitfall 4: `package.json` Script Command Path Breakage
- **Affected File**:
  - `package.json` (Lines 8, 9, 10, 12)
- **Breakage Cause**:
  `lint:exams`, `check:assets`, `build`, `build:images` 指向舊路徑 `node scripts/*.mjs`。執行 `npm run lint:exams` 或 `npm run build` 將拋出 `Cannot find module` 致命失敗。
- **Remediation**:
  更新 `package.json` 之 scripts 命令至 `node scripts/pipeline/{lint,utils}/*.mjs`。

### Pitfall 5: NLM Scripts Internal Cross-Module Import Breakage
- **Affected Files**:
  - `scripts/ask_nlm_for_2026.mjs` (Line 4)
  - `scripts/ask_nlm_for_renal_transplant.mjs` (Line 4)
- **Breakage Cause**:
  此二腳本目前使用 `import { reconcileResponses } from './ingest_exam.mjs';`。當移至 `scripts/pipeline/nlm/` 而 `ingest_exam.mjs` 移至 `scripts/pipeline/ingest/` 時，相對路徑 `./ingest_exam.mjs` 將失效。
- **Remediation**:
  更新引用為 `import { reconcileResponses } from '../ingest/ingest_exam.mjs';`。

---

## 5. Verification Matrix & Acceptance Checklists

在 Milestone 3 (Full Pipeline Verification & Integrity Audit) 階段，執行者應依據以下程序進行獨立驗證：

| Verification Phase | Command / Action | Expected Result | Acceptance Criteria Pass Condition |
|---|---|---|---|
| Linter Verification | `npm run lint:exams` | Exit code 0 | 0 schema errors, 0 synthetic headers, 0 broken sentences, all assets present |
| Vitest Unit Verification | `npm run test` | Exit code 0 | 14 test files passed, 98 tests passed (0 failed) |
| Pytest Unit Verification | `npm run test:py` | Exit code 0 | 2 tests passed in `test_extract_and_attach_images.py` |
| Asset Integrity Check | `npm run check:assets` | Exit code 0 | All referenced images exist in `public/` directory |
| Build Verification | `npm run build` | Exit code 0 | Vite build succeeds without missing script errors |


# Handoff Report: Testing Baseline & Acceptance Criteria Verification

## 1. Observation

1. **`package.json` Test & Lint Command Definitions**:
   - `package.json:8`: `"lint:exams": "node scripts/lint_exam_json.mjs && node scripts/lint_tutorial_json.mjs && node scripts/check_assets.mjs"`
   - `package.json:13`: `"test": "vitest run"`
   - `package.json:15`: `"test:py": "pytest --cov=scripts scripts/__tests__/"`

2. **Pre-Migration Baseline Test Outputs**:
   - Command `npm run lint:exams`:
     ```text
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
   - Command `npm run test` (vitest):
     ```text
     Test Files  14 passed (14)
          Tests  98 passed (98)
       Start at  22:09:25
       Duration  1.75s (transform 1.02s, setup 1.53s, import 5.02s, tests 1.38s, environment 8.43s)
     ```
   - Command `npm run test:py` (pytest):
     ```text
     scripts/__tests__/test_extract_and_attach_images.py ..                   [100%]
     ============================== 2 passed in 0.09s ===============================
     ```

3. **Existing Script Test File Imports & Setup**:
   - `scripts/__tests__/lint_exam_json.test.mjs:4`:
     `import { lintExamFile, runLinter } from '../lint_exam_json.mjs';`
   - `scripts/__tests__/build_image_index.test.mjs:4`:
     `import { scanDir, buildImageIndex } from '../build_image_index.mjs';`
   - `scripts/__tests__/test_extract_and_attach_images.py:8`:
     `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))`
   - `scripts/__tests__/test_extract_and_attach_images.py:10`:
     `import extract_and_attach_images`

4. **Configuration & Cross-Script Imports**:
   - `vitest.config.ts:17-18`:
     `include: ['src/**/*.{ts,tsx}', 'scripts/lint_exam_json.mjs', 'scripts/build_image_index.mjs']`
   - `scripts/ask_nlm_for_2026.mjs:4`:
     `import { reconcileResponses } from './ingest_exam.mjs';`
   - `scripts/ask_nlm_for_renal_transplant.mjs:4`:
     `import { reconcileResponses } from './ingest_exam.mjs';`

---

## 2. Logic Chain

1. **Establishing Pre-Migration Baseline (Observation 1 & 2)**:
   - 經實際執行 `npm run lint:exams`、`npm run test` 與 `npm run test:py`，目前所有命令皆以 exit code 0 成功執行。
   - `lint:exams` 掃描 103 個試題 JSON、77 個教學講堂 JSON 與 180 個 asset JSON，全部通過。
   - `vitest` 執行 14 個測試檔共 98 個測試，全數通過 (0 failed)。
   - `pytest` 執行 `test_extract_and_attach_images.py` 共 2 個測試，全數通過。
   - 此證明 pre-migration baseline 處於 100% 健康狀態，無預設失效之測試。

2. **Identifying Migration Breakage Points (Observation 3 & 4)**:
   - 當 11 個管道腳本移入 `scripts/pipeline/{lint,ingest,qc,nlm,utils}/` 之後：
     a) `scripts/__tests__/lint_exam_json.test.mjs` 與 `scripts/__tests__/build_image_index.test.mjs` 之相對 `import` 路徑若未改為 `../pipeline/lint/...` 及 `../pipeline/utils/...`，Vitest 將無法載入模組，導致 `npm run test` 失敗。
     b) `scripts/__tests__/test_extract_and_attach_images.py` 之 `sys.path.insert` 若未更新為 `../pipeline/ingest`，Pytest 將拋出 `ModuleNotFoundError`，導致 `npm run test:py` 失敗。
     c) `vitest.config.ts` 中的 `coverage.include` 若未更新路徑，Vitest coverage 配對將失效。
     d) `package.json` 中的 `lint:exams` 指令若未更新，執行 `npm run lint:exams` 將拋出 `Node.js ERR_MODULE_NOT_FOUND`。
     e) `ask_nlm_for_2026.mjs` 與 `ask_nlm_for_renal_transplant.mjs` 中的 `import { reconcileResponses } from './ingest_exam.mjs';` 若未改為 `../ingest/ingest_exam.mjs`，NLM 發問管道將會中斷。

3. **Deriving Acceptance Criteria Verification Strategy**:
   - 只要在 Milestone 2 針對上述相依路徑與設定檔進行精準更新，即可確保 Milestone 3 執行 3 大命令時能 100% 通過 Acceptance Criteria 驗證。

---

## 3. Caveats

- **Coverage Threshold Status**:
  `npm run test:coverage` 預設的 thresholds 為 `lines: 90, statements: 90`。目前因為 `src/` UI 元件的 coverage 為 ~78.6%，直接執行 `test:coverage` 會因 UI 覆蓋率未達標而告警。然而 Acceptance Criteria 要求的是 `npm run test` (Vitest run) 必須 0 failed，且 `npm run test` 本身確實 100% 通過 (98 tests passed)。
- **External NLM Infrastructure**:
  `ingest_exam.mjs` 與 `ask_nlm_for_*.mjs` 在執行 NLM Dual Asking 時會呼叫本機外部路徑 `/Users/yuan/Projects/Notebooklm/NLM_MCQs` 之 Python Gateway。測試環境中 Unit Tests 皆以 Mock 方法保護，不依賴網域/外部 API。

---

## 4. Conclusion

Pre-migration baseline 驗證已完整確認：`npm run lint:exams`、`npm run test` (Vitest 98 tests passed)、`npm run test:py` (Pytest 2 tests passed) 皆處於 100% 綠燈狀態。
搬移至 `scripts/pipeline/` 後的測試驗證關鍵在於同步修正 `scripts/__tests__/` JavaScript 與 Python 測試檔的相對引用路徑、`vitest.config.ts` 設定、`package.json` 指令以及 `ask_nlm_for_*.mjs` 的跨模組 import。修復後可無縫通過 Phase 2 的全套 Acceptance Criteria。

---

## 5. Verification Method

1. **Pre-migration Baseline Re-verification Command**:
   ```bash
   npm run lint:exams && npm run test && npm run test:py
   ```
   - Invalidation Condition: 任何命令傳回 exit code 非 0。

2. **Post-migration Verification Target Files**:
   - `package.json`
   - `vitest.config.ts`
   - `scripts/__tests__/lint_exam_json.test.mjs`
   - `scripts/__tests__/build_image_index.test.mjs`
   - `scripts/__tests__/test_extract_and_attach_images.py`
   - `scripts/pipeline/nlm/ask_nlm_for_2026.mjs`
   - `scripts/pipeline/nlm/ask_nlm_for_renal_transplant.mjs`

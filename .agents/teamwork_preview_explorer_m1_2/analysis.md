# External Path Resolution Analysis (Requirement R3)

## Summary
本報告為 Exam_prepare_site Phase 2 script modularization 之 Requirement R3 (External Path Updates) 進行全域唯讀盤點。當 11 個核心管線腳本從 `scripts/` 移轉至 `scripts/pipeline/{lint,ingest,qc,nlm,utils}/` 後，所有外部參照檔（包含 `package.json`, `AGENTS.md`, `vitest.config.ts`, `scripts/__tests__/` 以及 `scripts/` 底下其餘保留腳本）均須精準更新其相對與硬編碼路徑，以確保 npm scripts, pre-publish linter gates, Vitest, Pytest 與相依工作流程可正常運作。

---

## Detailed Findings & Replacement Mapping

### 1. `package.json`
- **File Path**: `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`
- **Impact Analysis**: npm script 指令呼叫已移轉至 `scripts/pipeline/lint/` 與 `scripts/pipeline/utils/` 之腳本。

| Script Key | Current Command (Line) | Target Command Replacement |
|------------|------------------------|----------------------------|
| `lint:exams` | `node scripts/lint_exam_json.mjs && node scripts/lint_tutorial_json.mjs && node scripts/check_assets.mjs` (Line 8) | `node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs` |
| `check:assets` | `node scripts/check_assets.mjs` (Line 9) | `node scripts/pipeline/lint/check_assets.mjs` |
| `build` | `node scripts/lint_exam_json.mjs && node scripts/lint_tutorial_json.mjs && node scripts/check_assets.mjs && tsc && vite build` (Line 10) | `node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs && tsc && vite build` |
| `build:images` | `node scripts/build_image_index.mjs` (Line 12) | `node scripts/pipeline/utils/build_image_index.mjs` |

---

### 2. `AGENTS.md`
- **File Path**: `/Users/yuan/Projects/Exam/Exam_prepare_site/AGENTS.md`
- **Impact Analysis**: 更新 Pre-Publish Linter Gate 指令路徑，並於 Mandatory Question Extraction Rules 中補充 Red Zone / Green Zone 之明確定義。

| Section / Rule | Current Text / Line | Target Replacement |
|----------------|---------------------|--------------------|
| Rule 10 (Line 82) | `execute node scripts/lint_exam_json.mjs` | `execute node scripts/pipeline/lint/lint_exam_json.mjs` |
| Rule 11 (Line 88) | `execute node scripts/lint_exam_json.mjs && node scripts/check_assets.mjs` | `execute node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/check_assets.mjs` |
| Rule 12 (Line 99) | `靜態 Linter scripts/lint_exam_json.mjs 會自動對所有 JSON 進行...` | `靜態 Linter scripts/pipeline/lint/lint_exam_json.mjs 會自動對所有 JSON 進行...` |
| Zero Mechanical Extraction Expansion (Line 18) | 原僅標註 `全管道絕對禁止使用 Regex 或機械腳本進行選答或選項擷取。` | 擴充 Red Zone 與 Green Zone 界線：<br>- **Red Zone (絕對禁令區)**：嚴禁全管道使用 Regex 或機械字串切分處理考題 `stem`、`options`、`sourceExplanation` 擷取與 NLM 答案剖析。<br>- **Green Zone (合規範圍區)**：JSON Schema 結構驗證、靜態 Linter (`scripts/pipeline/lint/*`)、檔案資產檢查 (`check_assets.mjs`)、圖表索引建置 (`build_image_index.mjs`) 及資料庫狀態修復/遷移管線腳本。 |

---

### 3. `scripts/__tests__/` (Test Files)
- **Impact Analysis**: Vitest 與 Pytest 單元測試檔導入模組之相對路徑需隨目標腳本層級搬移而調整。

| Test File Path | Line Number | Current Code | Target Replacement Code |
|----------------|-------------|--------------|-------------------------|
| `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/__tests__/lint_exam_json.test.mjs` | Line 4 | `import { lintExamFile, runLinter } from '../lint_exam_json.mjs';` | `import { lintExamFile, runLinter } from '../pipeline/lint/lint_exam_json.mjs';` |
| `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/__tests__/build_image_index.test.mjs` | Line 4 | `import { scanDir, buildImageIndex } from '../build_image_index.mjs';` | `import { scanDir, buildImageIndex } from '../pipeline/utils/build_image_index.mjs';` |
| `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/__tests__/test_extract_and_attach_images.py` | Line 8 | `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))` | `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'ingest')))` |

---

### 4. `vitest.config.ts`
- **File Path**: `/Users/yuan/Projects/Exam/Exam_prepare_site/vitest.config.ts`
- **Impact Analysis**: `coverage.include` 設定硬編碼之覆蓋率追蹤目標檔案需指向新路徑。

| Field / Location | Current Value (Line) | Target Replacement |
|------------------|----------------------|--------------------|
| `coverage.include[1]` | `'scripts/lint_exam_json.mjs',` (Line 17) | `'scripts/pipeline/lint/lint_exam_json.mjs',` |
| `coverage.include[2]` | `'scripts/build_image_index.mjs',` (Line 18) | `'scripts/pipeline/utils/build_image_index.mjs',` |

---

### 5. Additional Script Callers in `scripts/`
- **Impact Analysis**: 搬移及保留於 `scripts/` 底下的關聯腳本，跨模組引用路徑需同步更新。

| Caller Script File | Line | Current Import Statement | Target Replacement Import Statement | Note |
|--------------------|------|--------------------------|-------------------------------------|------|
| `scripts/ask_nlm_for_2026.mjs` | Line 4 | `import { reconcileResponses } from './ingest_exam.mjs';` | `import { reconcileResponses } from '../ingest/ingest_exam.mjs';` | Moved to `scripts/pipeline/nlm/` |
| `scripts/ask_nlm_for_renal_transplant.mjs` | Line 4 | `import { reconcileResponses } from './ingest_exam.mjs';` | `import { reconcileResponses } from '../ingest/ingest_exam.mjs';` | Moved to `scripts/pipeline/nlm/` |
| `scripts/reask_anomalous.mjs` | Line 4 | `import { reconcileResponses } from './ingest_exam.mjs';` | `import { reconcileResponses } from './pipeline/ingest/ingest_exam.mjs';` | Remains in `scripts/` |
| `scripts/repair_nlm_dual_asking.mjs` | Line 4 | `import { reconcileResponses } from './ingest_exam.mjs';` | `import { reconcileResponses } from './pipeline/ingest/ingest_exam.mjs';` | Remains in `scripts/` |
| `scripts/export_stage1_anomalous.mjs` | Line 3 | `import { isNlmResponseAnomalous } from './exam_qc.mjs';` | `import { isNlmResponseAnomalous } from './pipeline/qc/exam_qc.mjs';` | Remains in `scripts/` |
| `scripts/prepare_stage2_batch.mjs` | Line 3 | `import { inspectQuestionForQc } from './exam_qc.mjs';` | `import { inspectQuestionForQc } from './pipeline/qc/exam_qc.mjs';` | Remains in `scripts/` |
| `scripts/update_stage1_results.mjs` | Line 3 | `import { isNlmResponseAnomalous } from './exam_qc.mjs';` | `import { isNlmResponseAnomalous } from './pipeline/qc/exam_qc.mjs';` | Remains in `scripts/` |

---

## Verification Matrix
1. **`npm run lint:exams`**:
   - 驗證 `package.json` 指令執行成功，並能正確調用 `scripts/pipeline/lint/lint_exam_json.mjs`, `scripts/pipeline/lint/lint_tutorial_json.mjs` 及 `scripts/pipeline/lint/check_assets.mjs`。
2. **`npm run test` (Vitest)**:
   - 驗證 `scripts/__tests__/lint_exam_json.test.mjs` 與 `scripts/__tests__/build_image_index.test.mjs` 在 Vitest 載入時 `ERR_MODULE_NOT_FOUND` 不會發生，且測試 100% 通過。
3. **`npm run test:py` (Pytest)**:
   - 驗證 `scripts/__tests__/test_extract_and_attach_images.py` 可成功 `import extract_and_attach_images` 並通過 2 個單元測試。

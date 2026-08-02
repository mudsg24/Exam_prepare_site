# Phase 2 Script Modularization (R1, R2, R3) — Implementation Changes

## Summary of Changes

Phase 2 Script Modularization (R1, R2, R3) 已經成功實作與驗證完畢。所有 11 個管道腳本皆已搬移至 `scripts/pipeline/{lint,ingest,qc,nlm,utils}/` 目錄下，內部路徑解析與外部呼叫者、測試檔、設定檔與 `AGENTS.md` 治理規範皆已精準更新。

---

## Detailed File Modifications

### 1. R1 — Directory Setup & File Relocation
建立了 5 個子目錄，並使用 `git mv` 搬移以下 11 個腳本（核心邏輯維持 100% 原樣）：
- **`scripts/pipeline/lint/`**:
  - `lint_exam_json.mjs`
  - `lint_tutorial_json.mjs`
  - `check_assets.mjs`
- **`scripts/pipeline/ingest/`**:
  - `ingest_exam.mjs`
  - `extract_and_attach_images.py`
- **`scripts/pipeline/qc/`**:
  - `exam_qc.mjs`
  - `merge_qc_results.mjs`
  - `apply_qc_updates.py`
- **`scripts/pipeline/nlm/`**:
  - `ask_nlm_for_2026.mjs`
  - `ask_nlm_for_renal_transplant.mjs`
  - `process_nlm_results.py`
- **`scripts/pipeline/utils/`**:
  - `build_image_index.mjs`

---

### 2. R2 — Internal Path Resolution Fixes
更新搬移後腳本內部的相對路徑與 `import`：
- **`scripts/pipeline/lint/lint_exam_json.mjs`**:
  - Line 8: `SERVER_DATA_DIR` 改為 `path.resolve(__dirname, '../../../public/server-data')`
  - Line 208: `targetPath` 改為 `path.join(__dirname, '../../../public', filename)`
- **`scripts/pipeline/lint/lint_tutorial_json.mjs`**:
  - Line 8: `PUBLIC_DIR` 改為 `path.resolve(__dirname, '../../../public')`
- **`scripts/pipeline/lint/check_assets.mjs`**:
  - Line 8: `PUBLIC_DIR` 改為 `path.resolve(__dirname, '../../../public')`
- **`scripts/pipeline/nlm/ask_nlm_for_2026.mjs`**:
  - Line 4: `import { reconcileResponses } from '../ingest/ingest_exam.mjs';`
- **`scripts/pipeline/nlm/ask_nlm_for_renal_transplant.mjs`**:
  - Line 4: `import { reconcileResponses } from '../ingest/ingest_exam.mjs';`

---

### 3. R3 — External Path Updates & Governance
- **`package.json`**:
  - `lint:exams`: 指向 `scripts/pipeline/lint/lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`
  - `check:assets`: 指向 `scripts/pipeline/lint/check_assets.mjs`
  - `build`: 指向 `scripts/pipeline/lint/...`
  - `build:images`: 指向 `scripts/pipeline/utils/build_image_index.mjs`
- **`AGENTS.md`**:
  - 擴展 Rule 1 明確定義 **Red Zone** (絕對禁止對考題 `stem`/`options`/`sourceExplanation` 進行 Regex 切分與字串替換) vs **Green Zone** (`scripts/pipeline/` 下的 JSON schema linters, asset checkers, 管道腳本為合規系統工具)。
  - 更新 Rule 10, Rule 11, Rule 12 中的 linter 腳本引用路徑至 `scripts/pipeline/lint/...`
- **`vitest.config.ts`**:
  - 更新 `coverage.include` 陣列至 `scripts/pipeline/lint/lint_exam_json.mjs` 與 `scripts/pipeline/utils/build_image_index.mjs`
- **`scripts/__tests__/`**:
  - `lint_exam_json.test.mjs`: `import` 改為 `'../pipeline/lint/lint_exam_json.mjs'`
  - `build_image_index.test.mjs`: `import` 改為 `'../pipeline/utils/build_image_index.mjs'`
  - `test_extract_and_attach_images.py`: `sys.path.insert` 改為 `os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pipeline', 'ingest'))`
- **Unmigrated scripts in `scripts/`**:
  - `scripts/reask_anomalous.mjs`: `import` 改為 `'./pipeline/ingest/ingest_exam.mjs'`
  - `scripts/repair_nlm_dual_asking.mjs`: `import` 改為 `'./pipeline/ingest/ingest_exam.mjs'`
  - `scripts/export_stage1_anomalous.mjs`: `import` 改為 `'./pipeline/qc/exam_qc.mjs'`
  - `scripts/prepare_stage2_batch.mjs`: `import` 改為 `'./pipeline/qc/exam_qc.mjs'`
  - `scripts/update_stage1_results.mjs`: `import` 改為 `'./pipeline/qc/exam_qc.mjs'`

---

## Verification Results

1. **`npm run lint:exams`**:
   - `Exam JSON Static Linter`: Passed (Checked 103 exam JSONs).
   - `Tutorial JSON Linter`: Passed (Scanned 77 tutorial JSONs).
   - `Asset Integrity Checker`: Passed (Scanned 180 database JSONs).
2. **`npm run test` (Vitest)**:
   - 14 test files passed (98 tests passed).
3. **`npm run test:py` (Pytest)**:
   - 2 passed in 0.09s.

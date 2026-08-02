# Original User Request

## 2026-08-02T22:08:25Z

<USER_REQUEST>
# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Delegate to teamwork_preview to execute Phase 2

將 `Exam_prepare_site` 的龐雜 scripts 模組化，整併至 `scripts/pipeline/`，並同步修復內外部相依連鎖路徑。

Working directory: `/Users/yuan/Projects/Exam/Exam_prepare_site`
Integrity mode: development

## Requirements

### R1. Pipeline Module Migration
建立以下子目錄並移轉對應腳本 (不可修改腳本核心邏輯，僅做搬移)：
- `scripts/pipeline/lint/`: `lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`
- `scripts/pipeline/ingest/`: `ingest_exam.mjs`, `extract_and_attach_images.py`
- `scripts/pipeline/qc/`: `exam_qc.mjs`, `merge_qc_results.mjs`, `apply_qc_updates.py`
- `scripts/pipeline/nlm/`: `ask_nlm_for_*.mjs`, `process_nlm_results.py`
- `scripts/pipeline/utils/`: `build_image_index.mjs`

### R2. Internal Path Resolution Fix
- 徹底盤點並修改上述移轉腳本內的 `__dirname` 或 `os.path.dirname(__file__)` 相對路徑。因腳本移入深層目錄，必須將指向 `../public` 或根目錄的相對路徑修正（如改為 `../../public`），避免 Directory not found。

### R3. External Path Updates (Hardcoded)
同步修改以下檔案中的硬編碼路徑：
- `package.json`: 修改 `lint:exams`, `check:assets`, `build`, `build:images` 指向新的 `scripts/pipeline/lint/...`。
- `AGENTS.md`: 更新 Rule 10 與 Rule 11 的 `node scripts/lint_exam_json.mjs` 等路徑。並擴充 "ZERO MECHANICAL EXTRACTION" 條文，明定 Regex 處理題幹/選項為 "Red Zone" 絕對禁令，而 JSON/狀態管線腳本為 "Green Zone"。
- `scripts/__tests__/`: 更新測試檔的 imports 路徑。
- `vitest.config.ts`: 確保 `include` 涵蓋新路徑。

## Acceptance Criteria

### [Linter & E2E Verification]
- [ ] 執行 `npm run lint:exams` 必須成功，無語法或路徑錯誤。
- [ ] 執行 `npm run test` (vitest) 必須成功 (0 failed)。
- [ ] 執行 `npm run test:py` (pytest) 必須成功。

### [Code Quality]
- [ ] 腳本內的相對路徑 (`__dirname`, `os.path.dirname`) 必須能成功指向正確的根目錄與 `public/server-data` 實體檔案位置。
</USER_REQUEST>

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

## 2026-08-02T22:24:35Z

<USER_REQUEST>
# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Delegate to teamwork_preview to execute Phase 3

執行 `Exam_prepare_site` 的 Phase 3 重構：針對 7 個 `/tn-exam-*` Skills 進行 Atomic Transaction 改寫，落實單一職責與 Pipeline 呼叫對齊。

Working directory: `/Users/yuan/.gemini/config/skills/`
Integrity mode: development

## Requirements

### R1. Skill Boundary & Interface Contract (Group A: Ingestion & QC)
- **`tn-exam-prepare`**: 改寫為單純的 Ingestion 入口。專注發派 Subagents 進行 NLP 語意抽取。嚴格禁止內建繁雜的腳本邏輯，資料抽離完成後，一律改為觸發 `npm run pipeline:ingest`。
- **`tn-exam-qc`**: 改寫為權威的 Quality Gate。負責 NLM 完整度與語意審查，並統一呼叫 `npm run pipeline:qc` 來處理 retry loops 與狀態輪轉。清除所有與 prepare 重疊的 governance rules。

### R2. Skill Boundary & Interface Contract (Group B: Content Generation)
- **`tn-exam-expert`**: 降級為純粹的 Pre-processing 工具，專職負責文字牆 De-walling 與 LaTeX/Markdown 損毀修復。明文禁止呼叫 QC。
- **`tn-exam-producer`**: 專注於從 study notes 生成純英文 MCQs。
- **`tn-exam-tutor`**: 專注於從 study notes 生成 textbook-style lectures。
- **`tn-exam-lecture-and-practice`**: 改寫為純粹的 Orchestrator / Dispatcher。**本身禁止撰寫內容**，專職解析使用者需求後，透過 `invoke_subagent` 發派 `tn-exam-producer` 與 `tn-exam-tutor` 進行並行處理。清除其內部所有 duplicate 的 tutor/producer 治理條文。

### R3. General Skill Cleanup
- `tn-exam-query`: 確認維持 Semantic search/RAG 的角色，並移除任何已經作廢的相依。
- **全局清理**：移除上述 7 個 Skills 的重複治理條文 (Duplicate Governance Rules)，確保所有 `SKILL.md` 中對 Node.js / Python 的腳本呼叫，100% 取代為 `npm run pipeline:*` 的新架構呼叫，絕對不可殘留寫死的舊 `scripts/...` 實體路徑。

## Acceptance Criteria

### [Linter & Dependency Verification]
- [ ] 所有修改後的 `SKILL.md` 檔案必須能正常被平台解析 (YAML frontmatter 格式正確且不受損)。
- [ ] 使用 `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*` 必須找不到任何舊的直接腳本呼叫 (必須全部換成 `npm run pipeline:*`)。
- [ ] `tn-exam-lecture-and-practice/SKILL.md` 內容必須證實不再包含自己產生內容的 Prompt 邏輯，僅保留 `invoke_subagent` 派發邏輯。
</USER_REQUEST>

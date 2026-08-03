---
name: tn-exam-lecture-and-practice
description: "TSN 腎臟專科考點整合之純 Orchestrator / Dispatcher 門面 Skill。接收指定腎臟科考點/主題，解析用戶輸入並呼叫 invoke_subagent 分流派發 tn-exam-producer (產出純英文練習題庫) 與 tn-exam-tutor (產出主題式教學講堂)，經由 npm run pipeline:lint 與 npm run build 完成雙重產出與整合發佈。"
user-invocable: true
---

# /tn-exam-lecture-and-practice — Orchestrator & Dispatcher Gateway for Masterclass Lecture & Practice Test Bank

## Purpose

本 Skill 為 TSN 腎臟專科醫師甄試考點整合之**純 Orchestrator / Dispatcher 門面 (Pure Orchestrator / Dispatcher ONLY)**。
本 Skill **本身絕對不直接生成講堂或題庫內文**，其唯一職責為解析用戶輸入之主題與參數，並透過 `invoke_subagent` 分流派發給專責 Skill：
1. **`tn-exam-tutor`**：專責生成教科書等級之主題式教學講堂 (Masterclass Lecture)。
2. **`tn-exam-producer`**：專責生成純英文練習選擇題庫 (Practice Test Bank)。

經由 `npm run pipeline:lint` 與 `npm run build` 完成最終整合與構建驗證。

## Yuan Usage

- 斜線指令或口語觸發：
  - `/tn-exam-lecture-and-practice <topic_name>`
  - 「Tonks，幫我用 tn-exam-lecture-and-practice 準備 '<topic_name>' 的課程與練習題」

## Governance & Boundary

- **GOVERNANCE RULES ALIGNMENT**:
  - 全流程硬性遵循 `AGENTS.md` 之 12 大考題治理規範（包含 0% Regex 內文處理、0% 人造標題、專有名詞純英文及圖表 Schema 完整性等）。

- **PURE ORCHESTRATOR / DISPATCHER MANDATE (純調度與派發鐵律)**:
  - 本 Skill **絕對不得**在主 Session 內直接撰寫、生成或編輯講堂段落、題目內文、選項或 NLM 解析。
  - 所有內容生成任務**必須且只能**透過 `invoke_subagent` 委派給 `tn-exam-tutor` 與 `tn-exam-producer` 完成。

- **SUBAGENT DISPATCH CONTRACT (子精靈派發合約)**:
  - 派發 Subagent 時，必須傳入確切之 `topic_name` 與相關參數。
  - 講堂生成委派：呼叫 `invoke_subagent` 並遵循 `tn-exam-tutor` 規範之工作流處理。
  - 題庫生成委派：呼叫 `invoke_subagent` 並遵循 `tn-exam-producer` 規範之工作流處理。

- **PIPELINE & LINTER CLEARANCE (管道與靜態驗證關卡)**:
  - 完成分流派發與產出後，執行 `npm run pipeline:lint` 與 `npm run build` 完成最終整合與構建驗證。

## Execution Algorithm

### Step 1: Input Parsing & Dispatch Blueprint
1. 接收 Yuan 傳入之主題名稱 (`topic_name`) 與參數。
2. 提報調度計畫，確定將同時派發 `tn-exam-tutor` 與 `tn-exam-producer`。

### Step 2: Dispatch `tn-exam-tutor` Subagent
1. 呼叫 `invoke_subagent` 派發專責 Subagent（採用 `model_reasoning_effort: high`）：
   - 載入並遵循 `/Users/yuan/Projects/Exam/Exam_prepare_site/.gemini/skills/tn-exam-tutor/SKILL.md` 規範。
   - 針對 `topic_name` 產出教科書等級之主題式教學講堂 JSON 至 `public/server-data/tutorials/`。

### Step 3: Dispatch `tn-exam-producer` Subagent
1. 呼叫 `invoke_subagent` 派發專責 Subagent（採用 `model_reasoning_effort: high`）：
   - 載入並遵循 `/Users/yuan/Projects/Exam/Exam_prepare_site/.gemini/skills/tn-exam-producer/SKILL.md` 規範。
   - 針對 `topic_name` 產出純英文練習題庫 JSON 至 `public/server-data/`。

### Step 4: Pipeline Execution & Final Verification
1. 呼叫 `run_command` 執行 `npm run pipeline:lint` 與 `npm run build` 確認全站 Schema、圖片資產與 TypeScript 構建 100% 通過。

## Output Contract

- 匯報統一使用 **繁體中文敘述 + 英文專有名詞**（Headings 保持純 English）。
- 匯報結構：
  - **Dispatched Topic**: 指定主題名稱
  - **Orchestration Status**:
    - `tn-exam-tutor` 派發與講堂產出狀態
    - `tn-exam-producer` 派發與題庫產出狀態
  - **Deliverable Artifacts Summary**: 講堂檔與題庫檔路徑
  - **Build Verification**: `npm run pipeline:lint` 與 `npm run build` 構建驗證結果

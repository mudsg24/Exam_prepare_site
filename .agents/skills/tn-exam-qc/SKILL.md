---
name: tn-exam-qc
description: "專責 TSN 考題品質控制與解答爭議稽核 Skill。作為權威 Quality Gate，實施雙階段強制關卡：Stage 1 鎖定技術性失敗題目 (未達雙重對答、短回答<200字、連線 Error) 通過 npm run pipeline:qc 與 /tn-nlm-asking-mcqs 發起一次性重問；Stage 2 派發 Subagents 逐題重讀原始檔與 NLM 全文進行 100% 語意校對 (0% Regex)，持久化寫入 QC 結案標記。"
user-invocable: true
---

# /tn-exam-qc — Exam Quality Control & Reconciliation Gateway

## Purpose

本 Skill 為 TSN 腎臟專科醫師甄試考題之權威品質控制與爭議處理門面 (Authoritative Quality Gate)。負責維護全站考題 NLM 對答完整度與語意審查，實施雙階段強制關卡 (Two-Stage Strict Gated Pipeline)：

1. **Stage 1 Gate (技術性失敗與缺失優先消除關卡)**：調用 `npm run pipeline:qc -- --scan-only` 掃描全站 `public/server-data/*.json`，找出 `nlmResponses.length < 2`、`rawResponse.length < 200` 或帶有連線 Error 之題目，彙整單一 Payload 檔並經由 `/tn-nlm-asking-mcqs` 進行單一管道一次性重問。
2. **Stage 2 Gate (Subagent 原始檔與 NLM 全文雙重語意校對關卡)**：派發獨立 Subagent 重讀原始檔案驗證 `stem` 與 `options` 完整性，語意研讀 NLM `Answer Determination` 判定 `selectedOption` (`A`~`E`, `B, D`, `NONE`, `ALL`)，並調用 `npm run pipeline:qc` 腳本寫回 `qcVerified: true`、`qcStatus` 與 `qcNotes`。

## Yuan Usage

- 斜線指令或口語觸發：
  - `/tn-exam-qc` (掃描資料庫中所有未驗證或異常題目)
  - `/tn-exam-qc --paper <paper_id>` (針對特定試卷進行 QC 稽核)
  - `/tn-exam-qc --force` (強制對全資料庫所有試卷重新執行 QC 稽核)
  - `/tn-exam-qc --clean` (清理歷史無效或重複 NLM 對答紀錄)
  - 「Tonks，幫我用 tn-exam-qc 校對這張試卷：'2025_114出題表格_傳統題_中山吳勝文'」

## Boundary & Governance

- **GOVERNANCE RULES ALIGNMENT**:
  - 全流程遵循 `AGENTS.md` 之 12 大考題治理規範。本 Skill 為品質審查專責門面，不包含 Prepare 階段之檔案遞迴搜尋、MCQ 資格預檢或 Ingestion 清單呈報邏輯。

- **ABSOLUTE BAN ON AD-HOC RE-ASK SCRIPTS (全管道嚴禁自創/批次重問腳本鐵律)**:
  - 絕對禁止 Agent 於執行 QC 期間寫入或執行任何自創的批次迴圈腳本。
  - 所有 NLM 補問一律且只能走 `/tn-nlm-asking-mcqs` 標準門面。

- **SINGLE-PASS STAGE 1 RULE (單次執行一輪鐵律)**:
  - 單次呼叫 `/tn-exam-qc` 時，Stage 1 重問任務一律只執行 1 輪 (Single Pass)。結束後直接轉入 Stage 2，絕不循環重試。

- **CORE QUALITY GATE CHECKS (五大核心品質檢查)**:
  1. **Distractor Analysis Collision Guard (干擾項字母碰撞防線)**: 判定 `selectedOption` 時錨定 `Answer Determination`，禁止從干擾項分析中誤抓字母。
  2. **INSUFFICIENT Header False-NONE Guard**: 開頭有 INSUFFICIENT 警語但內文有明確正解時，寫入該選項字母，禁止盲目寫入 `NONE`。
  3. **Zero-Null SelectedOption Guard**: 確認所有條目 `selectedOption` 均為非空字串。
  4. **Strict Dual Response Count & Length Guard**: 確認每題具備精確 2 筆獨立有效回應 (`nlmResponses.length === 2`) 且無連線 Error。
  5. **Reconciliation Status Alignment Guard**: 確認 `reconciliationStatus` 精確反映 NLM 共識與原始答案對比。

- **MANDATORY MAIN SESSION INTERVENTION FOR NLM `NONE` & DISCREPANCIES (主 Session 強制介入診斷與報告鐵律)**:
  - 遇 `NONE` 判定或 NLM 與原始答案不一致時，主 Session 必須親自介入診斷根本原因（提問 Payload 缺漏選項 / 題目瑕疵 / 文獻限制），並於 Chat 中輸出正式 QC 結案報告。

- **STRICT LANGUAGE AUDIT GATE (專有名詞純英文硬性審查關卡)**:
  - QC Subagent 於 Stage 2 審查時，強制驗證 `sourceExplanation` 與 `reconciliationNotes`：敘述 100% 繁體中文，所有醫學與技術專有名詞 100% 純英文 (0% 中譯專有名詞、0% 雙語括號)。

- **PERSISTENT QC METADATA**:
  - 凡通過校對核銷之題目，必須寫入 `qcVerified: true`、`qcStatus` (`QC_PASSED` / `QC_DISPUTED_RESOLVED` / `QC_REASKED`) 與 `qcNotes`。

## Execution Algorithm

1. **Step 1: Scan & Categorize Target Questions (掃描資料庫與問題分類)**
   - 調用 `npm run pipeline:qc -- --scan-only` (或指定 `--paper <paper_id>` / `--force` / `--clean`) 掃描 `public/server-data/*.json`。
   - 彙整需要處置的題目：
     - **Category A (Stage 1 Technical Failures)**: `nlmResponses.length < 2` 或 `rawResponse.length < 200` 或帶有 `error`。
     - **Category B (Stage 2 Review Scope)**: 待 Subagent 雙重校對與語意審查之題目 (`qcVerified !== true` 或存在爭議)。

2. **Step 2: Execute Stage 1 Gate - Single-Payload NLM Re-ask (執行單一 Payload 重問)**
   - 將 Category A 題目統一彙整為單一 JSON Payload，調用 `/tn-nlm-asking-mcqs` 進行單一管道一次性提問。
   - 提問完成後更新伺服器 JSON 資料庫。

3. **Step 3: Execute Stage 2 Gate - Subagent Dual Semantic Verification (執行 Stage 2 Subagent 雙重校對)**
   - 針對 Category B 題目，按 5 題/批次切分，派發 Subagent (`invoke_subagent`, `model_reasoning_effort: high`)：
     - 重讀原始檔案 (`_origin.docx` 等) 核對題幹與選項。
     - 語意研讀 NLM 全文判定 `selectedOption`。
     - 比對原始答案與 NLM 共識，決定 `reconciliationStatus` 與 `qcNotes`。

4. **Step 4: Update JSON Database & Persist QC Flags (寫入資料庫與標記結案)**
   - 調用 `npm run pipeline:qc` Pipeline 將 Subagent 驗證結果寫回 `public/server-data/<paper_id>.json` 並更新 `exams_manifest.json`。
   - 執行 `npm run pipeline:lint` 與 `npm run build` 通過全站 Schema 與資產編譯驗證。

## Progress & Output Contract

- 過程中使用**繁體中文敘述 + 英文專有名詞**（Headings 為 English）。
- 匯報統計數據：
  - 已檢測題目總數
  - Stage 1 短回答/連線失敗經 /tn-nlm-asking-mcqs 成功補齊重問題數
  - Stage 2 經由 Subagent 雙重校對成功結案題數
  - 最終完成 QC 標記 (`qcVerified: true`) 題數

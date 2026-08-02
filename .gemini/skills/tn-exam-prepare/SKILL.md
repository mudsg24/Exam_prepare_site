---
name: tn-exam-prepare
description: "TSN 腎臟專科考題處理與匯入門面 Skill。遞迴遍歷指定資料夾、整理試卷名稱、執行 MCQ 資格預檢過濾非 MCQ 文件 (如 Clinical Cases, Topic Outlines)、自動比對資料庫並跳過已處理試卷（支援 --force）、提報 Yuan 確認、派發 Subagents 以原始檔優先進行純 NLP 語意題目與元資料抽離 (嚴禁 Regex & 拒絕 Mineru 二手污染)、派發專責 QC Subagent 執行 100% 題目品管、呼叫 /tn-nlm-asking-mcqs 執行雙重提問與 Subagent NLM 語意答案解析，並調用 npm run pipeline:ingest 進行網站資料庫寫入與資產建置。"
user-invocable: true
---

# /tn-exam-prepare — TSN Exam Preparation & Ingestion Gateway

## Purpose

本 Skill 為 TSN 腎臟專科醫師甄試與歷年交換考題之純 Ingestion 處理門面。專注於接收資料夾路徑後進行遞迴遍歷、MCQ 資格預檢、已處理試卷比對與 Yuan 二次確認，接著派發 Subagents 進行純 NLP 語意題目與解說抽離，經專責 QC Subagent 品管審查與 `/tn-nlm-asking-mcqs` 提問解析後，統一調用 `npm run pipeline:ingest` 腳本執行資料庫寫入與圖片資產串接。

## Yuan Usage

- 斜線指令或口語觸發：
  - `/tn-exam-prepare <path_to_dir_1> <path_to_dir_2> ...`
  - `/tn-exam-prepare --force <path_to_dir_1> ...` (強制重新處理已匯入試卷)
  - 「Tonks，幫我用 tn-exam-prepare 處理這些資料夾：'/Users/yuan/Projects/Exam/Exam_prepare_database/Processed/TSN 歷年交換題/2025 年交換題/2025 114出題表格_傳統題_中山吳勝文 - 原檔' ...」

## Governance & Boundary

- **GOVERNANCE RULES ALIGNMENT**:
  - 全流程硬性遵循 `AGENTS.md` 之 12 大考題治理規範（包含 0% Regex 內文處理、0% 人造標題、原始檔優先識別、專有名詞純英文、專責 QC 審查門閥、及圖表 Schema 完整性等）。

- **MCQ ONLY INGESTION RULE (僅處理 MCQ 選擇題試卷)**:
  - 本 Skill 僅處理具備選項 (A-E / A-D) 之 Multiple Choice Questions (MCQ) 選擇題試卷。
  - 凡不具備選項之非 MCQ 文件（例如臨床病例討論 Clinical Cases、出題範圍重點 Topic Outlines、問答題 Essay Questions 等），一律於預檢階段自動識別標註為非 MCQ 並排除。

- **PROCESSED PAPER SKIPPING RULE (自動跳過已處理試卷)**:
  - 預設自動比對 `public/server-data/exams_manifest.json` 與 `public/server-data/<paper_id>.json`。
  - 若試卷已存在，除非傳入 `--force` 標籤或在 Chat 中指示重新處理，否則一律自動跳過。

- **SUBAGENT NLP EXTRACTION & CONCURRENCY CONTROL (Subagent 純 NLP 語意抽離與批次控管)**:
  - 題目、選項、章節標籤與解說 (`sourceExplanation`) 抽離 100% 由 Subagents 閱讀原始檔進行語意解析，嚴禁機械切分。
  - 派發 Subagent 時按 5 題/批次 (Batch Size = 5) 進行分流，避免 Context 過大或語意混淆。

- **CONFIRMATION GATE (Yuan 雙重確認關卡)**:
  - 遍歷與預檢完畢後，必須先向 Yuan 呈報「預計處理、已跳過與非 MCQ 排除試卷清單」，並暫停執行，靜候 Yuan 於 Chat 中確認後方可續行。

- **NO GROUND TRUTH TO NLM**:
  - 呼叫 `/tn-nlm-asking-mcqs` 提問門面時僅傳遞題目與選項，絕對不洩漏原始解答。

## Execution Algorithm

1. **Step 1: Discover & Pre-screen (遞迴搜尋、原始檔定位與 MCQ 資格預檢)**
   - 遍歷傳入之資料夾與子目錄，優先定位原始檔案 (`_origin.docx`, `_origin.pdf` 等)。
   - 剝除名稱後綴 `- 原檔`。
   - 檢視檔案內容，過濾非 MCQ 文件。
   - 比對 `public/server-data/exams_manifest.json` 區分待處理 MCQ、已處理 skip 項目與非 MCQ 排除項目。

2. **Step 2: Propose & Confirm (呈報計畫與靜候確認)**
   - 在 Chat 中向 Yuan 匯報試卷處理計畫。
   - 暫停並靜候 Yuan 於 Chat 中回覆確認。

3. **Step 3: Subagent NLP Semantic Extraction (Subagent 原始檔語意題目與解說抽離)**
   - 派發 Subagents 直接讀取原始檔案，進行純 NLP 語意抽離：
     - 題目 `stem`
     - 選項 `options`
     - 章節標記 `chapter`
     - 解說 `sourceExplanation` (嚴格隔離於專屬欄位，不得混入 stem)
     - 原始答案 `sourceProvidedAnswer` (若缺失則執行原檔視覺/樣式重讀)

4. **Step 4: Dual NLM Dispatch & Subagent Parsing (雙重提問派發與 Subagent NLM 語意解析)**
   - 呼叫 `/tn-nlm-asking-mcqs` 門面發起 2 次獨立提問。
   - 派發 Subagent 閱讀 NLM 完整回答，語意解析 `selectedOption` (單選 `A`~`E`、複選 `B, D`、`NONE`、`ALL`)。

5. **Step 5: Dedicated QC Subagent Audit Gate (專責 QC Subagent 品質與解說隔離審查)**
   - 派發專責 QC Subagent 對抽離 JSON 與 NLM 解析結果進行 100% 品管與隔離驗證。
   - 通過驗證者核發 `QC_PASSED` 標籤。

6. **Step 6: Pipeline Ingestion Execution (執行管道腳本進行匯入與圖片串接)**
   - 調用 `npm run pipeline:ingest -- <dir1> <dir2> ...` (支援 `--force` / `--dry-run`) 執行資料庫寫入、考題圖片連結、Brenner/KDIGO 教科書圖片索引對應與 Manifest 更新。
   - 執行 `npm run pipeline:lint` 與 `npm run build` 強制驗證全站 Schema 與 TypeScript 構建。

## Progress & Output Contract

- 提報與進度轉播統一使用**繁體中文敘述 + 英文專有名詞**（Headings 為 English）。
- 題目與解說抽離、NLM 選項解析全程使用 Subagent 語言能力，嚴禁 Regex 切分。
- 匯入階段統一透過 `npm run pipeline:ingest` 腳本執行。
- 完成後匯報新新增試卷數、跳過試卷數、非 MCQ 排除數與總題目數統計。

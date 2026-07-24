# AGENTS.md — Workspace Guidance for Exam Prepare Site

## Workspace Identity

`Exam_prepare_site` is a local-running web application designed for practicing, reviewing, and analyzing medical specialization exam questions (TSN 腎臟專科醫師甄試與歷年交換題).

## Roles & Responsibilities

- **Lupin/Codex**: Primary workspace developer and repository structure maintainer.
- **Tonks/Antigravity**: Supportive partner and reviewer agent. Manages quality verification, review memos, and skill workflows.

## Mandatory Question Extraction Governance Rule

> [!CRITICAL]
> **STRICT QUESTION EXTRACTION & NLM PARSING GOVERNANCE RULES (考題抽離與 NLM 解析四大強制規範)**:
> 
> 1. **NO REGEX QUESTION PARSING RULE (嚴禁使用 Regex 抓取題目與資料)**:
>    - **絕對禁止**使用 Regex 正則表達式腳本進行考題內文、選項、解答或解說之抓取與切分。
>    - 所有的題目解析與結構化提取（包含題幹、選項、章節標籤 `Chapter`、原始解說 `Explanation`、頁碼出處），**一律必須派發 Subagents 透過 LLM 語言能力與語意理解進行判斷與抽離**。
>
> 2. **SOURCE-FILE PRIORITY RULE (原始檔優先，防二手資訊污染原則)**:
>    - 只要試卷資料夾中存在原始檔（如 `_origin.docx`、`_origin.pdf`、`_origin.pptx` 或圖片檔），Subagents **一律必須直接讀取原始檔內文與標註**。
>    - **絕不依賴 Mineru 轉出的 `.md` 或中間產物**，避免因 Mineru 轉檔遺漏選項、丟失格式或錯位而造成二手資訊污染。
>
> 3. **ABSOLUTE BAN ON REGEX NLM OPTION EXTRACTION (全管道嚴禁 Regex 擷取選項 & 100% Subagent 語意分析)**:
>    - **全管道（包含主 Session、腳本與 Subagents）絕對禁止**使用正則表達式 (Regex) 或字串比對去機械化擷取 NLM 回答中的選項字母 (A-E)。
>    - 正則表達式缺乏臨床語意理解，極易將內文提及之專有名詞 (如 `CaSR`、`EABV`)、誘答剖析中的非正解字母 (如 `選項 (B) 屬於相對禁忌...` 被誤抓為正解)、或是題目瑕疵宣告 (如 `Option A, B, C, D 無一正確`) 錯判為多選或單選答案。
>    - **100% Subagent 語意分析鐵律**：`selectedOption` **一律且只能由 Subagents 閱讀全文後以 LLM 語意能力進行邏輯研判**。正確選項為單選時輸出 `A`~`E`；複選題/多重解答時輸出 `B, D`；無解答/題目瑕疵時輸出 `NONE`；一律給分時輸出 `ALL`。腳本只接受 Subagent 語意判讀產出之 `selectedOption`，絕不進行機械化覆寫或猜測。
>
> 4. **DEDICATED QC SUBAGENT QUALITY GATE (專責 QC Subagent 驗證機制)**:
>    - 在 Subagent 完成初次題目抽離與 NLM 解析後，**必須派發專責的 `QC Subagent`** 對產出的 JSON 進行 100% 嚴格品質檢核：
>      - **選項完整度 (Options Integrity)**: 驗證每道題目是否皆具備完整的 A-E / A-D 選項，絕對不可遺漏選項。
>      - **解說與中元資料嚴格隔離 (Metadata & Explanation Isolation)**: 驗證題幹 (Stem) 中零混入 Explanation、Chapter 標籤或 Page 備註文字。原始解說必須隔離置於專屬欄位。
>      - **HTML 語法乾淨化 (Clean HTML)**: 驗證 `<em>`, `<strong>` 標籤已完整轉換為 Markdown 語法或淨化。
>      - **NLM 解答精準度 (NLM Option Precision)**: 驗證 `selectedOption` 與 NLM 內文 `Answer Determination` 標明之選項完全一致，無專有名詞誤判（如把 DDAVP 誤判為 D），且**複數選項（如 B, D）與無答案（NONE）無截斷或遺漏**。
>      - **解答精準對映 (Ground Truth Accuracy)**: 驗證原始答案與對照表已精準擷取。
>    - 只有通過 QC Subagent 標註為 `QC_PASSED` 的題目，方可獲准寫入網站資料庫。

## Single Source of Truth (SSOT) Data Sources

1. **Processed Exam Questions**:
   - Location: `/Users/yuan/Projects/Exam/Exam_prepare_database/Processed`
   - Description: Test papers and exchange questions. Paper folders ending in `- 原檔` must be stripped for display.

2. **Reference Image Outputs**:
   - KDIGO Guidelines: `/Users/yuan/Projects/PDF/Outputs/KDIGO`
   - Brenner 11e: `/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e`
   - Note: Other image folders in `PDF/Outputs` are not cited by NotebookLM and must be ignored.

3. **NotebookLM Dual Asking Gateway**:
   - Skill: `/tn-nlm-asking-mcqs`
   - Directory: `/Users/yuan/Projects/Notebooklm/NLM_MCQs`
   - Gateway Command: `uv run --directory /Users/yuan/Projects/Notebooklm/NLM_MCQs python -m MCQ_manufacturer.nlm_asking_gateway`
   - Architecture: 25-Worker pool across 5 accounts / 25 Notebooks.

## Web Application Architecture

- **Framework**: Vite + React + TypeScript + Vanilla CSS / Tailwind.
- **Data Location**: `public/server-data/`
  - `exams_manifest.json`: List of all imported test papers.
  - `<paper_id>.json`: Structured question bank for individual paper.
  - `image_index.json`: Citation mapping for KDIGO and Brenner 11e figures.
- **Modes**:
  - `Practice Mode` (正計時, no countdown, submit all to reveal answers).
  - `Dispute Analysis` (Highlights discrepancies between source provided answer and dual NotebookLM responses).

## Key Skills

- `/tn-exam-prepare`: Ingestion skill for scanning question directories, requesting Yuan confirmation, dispatching subagents for semantic question extraction directly from source files (No Regex! Source First!), executing dedicated QC Subagent verification, dispatching dual NLM asking via `/tn-nlm-asking-mcqs`, matching images, and updating the web database.
- `/tn-exam-qc`: Dedicated quality control skill for scanning anomalous NLM answers (< 200 chars or `INSUFFICIENT`), triggering NLM re-asking, dispatching subagents for source-first and full-text semantic option re-evaluation, and persisting QC verification flags (`qcVerified: true`, `qcStatus`) in the web database.

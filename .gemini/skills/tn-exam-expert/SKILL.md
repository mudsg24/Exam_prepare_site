---
name: tn-exam-expert
description: "考前專責試卷文字牆解牆 (De-Walling)、Markdown 刪除線修復 (Anti-Strikethrough) 與 LaTeX/Markdown 語法極化預處理工具。專注於練習特定試卷前之純排版與語法預處理。"
user-invocable: true
---

# /tn-exam-expert — Pre-Practice Exam Preparation & Pre-processing Expert Tool

## Purpose

本 Skill 為 TSN 腎臟專科醫師甄試考題之**純預處理門面 (Pre-processing Tool)**。當 Yuan 準備開始練習某張特定試卷前，啟動此門面專注執行試卷內文之文字牆解牆 (De-Walling)、Markdown 刪除線修復 (Anti-Strikethrough) 與 LaTeX/Markdown 語法排版極化預處理：
1. **Stem De-Walling & Paragraph Breaking (題幹解牆與數據條列)**：直讀原始檔案解開文字牆，將病歷、理學檢查與抽血/尿液數據以 `\n\n` 與 `- ` 或 Markdown 表格清晰分離。
2. **Anti-Strikethrough & LaTeX/Markdown Fix (刪除線修復與語法校正)**：轉義所有範圍波浪號 (`\~`) 徹底消除 Markdown 刪除線渲染 Bug，並對齊隨附圖表。
3. **Pipeline Static Verification (管道靜態驗證)**：由 LLM Subagents 處理內容預處理後，呼叫 `npm run pipeline:lint` 完成靜態 Schema 與資產驗證。

**注意：本 Skill 為純 Pre-processing 工具，不進行任何 QC 品管、不呼叫 `/tn-exam-qc`、亦不處理 NLM 回答可讀性。**

## Yuan Usage

- 斜線指令或口語觸發：
  - `/tn-exam-expert 2025北醫題庫一`
  - `/tn-exam-expert <paper_id_or_json_name>`
  - 「Tonks，幫我在考前用 tn-exam-expert 整理 '2026北醫-練習題'」

## Governance & Boundary

- **GOVERNANCE RULES ALIGNMENT**:
  - 全流程硬性遵循 `AGENTS.md` 之 12 大考題治理規範（包含 0% Regex 內文處理、0% 人造標題、原始檔優先識別、專有名詞純英文及圖表 Schema 完整性等）。

- **MANDATORY STEM DE-WALLING & PARAGRAPH BREAKING (強制題幹解牆與數據條列鐵律)**:
  - 凡包含臨床病歷、理學檢查、抽血與尿液數據之長題幹，必須以自然雙換行 `\n\n` 切分段落，數據採用項目符號 (`- `) 條列或整理為整齊 Markdown 表格 (`| ... |`)，絕不允許留存單行文字牆。

- **ANTI-STRIKETHROUGH GFM PROTECTION (Markdown 範圍波浪號防刪除線保護鐵律)**:
  - 必須將文字中所有範圍波浪號 `~` 轉義為 `\~` (如 `(3.5\~5)`) 或置入 Markdown 表格，100% 消除 GFM 刪除線 (`<del>`) Rendering Bug。

- **NO QC & NO NLM WORKFLOW CALLS (絕不呼叫 QC 與 NLM 工作流)**:
  - 本 Skill 嚴禁呼叫 `/tn-exam-qc` 或執行任何 QC 品管步驟。

## Execution Algorithm

### Step 1: Resolve Target Paper & Locate Original Files
1. 依據輸入之 `paper_name`（如 `2025北醫題庫一`），在 `public/server-data/` 搜尋對應 JSON 檔（如 `public/server-data/2025_北醫題庫一.json` 或 `2025北醫題庫一.json`）。
2. 在 `/Users/yuan/Projects/Exam/Exam_prepare_database/Processed/` 搜尋該試卷之原始檔案資料夾（名稱通常為 `<paper_id> - 原檔/`），確認存在 `_origin.docx`、`_origin.pdf` 或 `_origin.pptx` 及圖片。

### Step 2: Pre-processing Execution & Stem De-Walling
1. 派發 Subagent (`invoke_subagent`, `model_reasoning_effort: high`) 執行純語意文字預處理與 De-Walling：
   - **開啟原檔**：開啟 `_origin.*` 原始檔與圖表。
   - **語意解開文字牆**：將 `stem` 中臨床病歷、理學檢查與抽血/尿液數據以自然雙換行 `\n\n`、條列 `- ` 或 Markdown 表格優化。
   - **修復刪除線與 LaTeX/Markdown**：將範圍波浪號轉義為 `\~` 或置入 Markdown 表格，100% 消除刪除線渲染 Bug，校正 LaTeX/Markdown 語法。
   - **零人造標題與零字詞變動**：嚴禁插入 `**History...**` 等人造標題，確保 0% 單字變動。
   - **對齊隨附圖片**：確認 `attachedImages` 列表中圖片與原檔/題目內文引用正確對應。
2. 寫回 JSON 檔。

### Step 3: Automated Static Linter Clearance
1. 主 Session 呼叫 `run_command`: `npm run pipeline:lint`。
2. 確認全試卷通關（0 人造標題、0 斷句瑕疵、0 未轉義波浪號刪除線、0 無換行文字牆），並可成功執行 `npm run build`。

## Progress & Output Contract

- 過程中使用**繁體中文敘述 + 英文專有名詞**（Headings 為 English）。
- 匯報預處理完成狀態與統計數據：
  - 目標試卷名稱與 JSON 路徑
  - 整理與驗證題數（驗證 0 人造標題、0 字詞竄改、0 刪除線 Bug、0 文字牆）
  - Static Linter 通過狀態 (`npm run pipeline:lint`)

---
name: tn-exam-producer
description: "TSN 腎臟專科考訊重點轉化與純英文練習選擇題 (MCQs) 生成門面 Skill。讀取非 MCQ 考訊重點檔案 (如大林、雙和考訊重點)，使用 Subagents 語意將每個重點項目轉化為 2-3 題高質感選擇題 (純英文 stem & options, 繁中+英文專有名詞 Tonks 深度解析 sourceExplanation)。自動搜尋 KDIGO / Brenner 11e 圖表庫關聯圖片，呼叫 /tn-nlm-asking-mcqs 執行雙重 NLM 盲測對答，並派發 100% 語意 Subagent (0% Regex) 進行三向答案交叉比對 (Triangulation Reconciliation) 與 QC 品管，經由 npm run pipeline:lint 驗證，最終匯入 Web App 資料庫 (public/server-data/) 於 '2026 年重點轉化' 分類下。"
user-invocable: true
---

# /tn-exam-producer — TSN Exam Key Points Pure English MCQ Producer Gateway

## Purpose

本 Skill 為 TSN 腎臟專科醫師甄試考訊重點轉化與純英文選擇題 (MCQs) 生成門面。接收一個考訊重點檔案 (.txt, .docx, .pdf, .md) 或資料夾路徑，自動讀取非 MCQ 考訊重點項目，使用 Subagents 將每個重點轉化為指定數量 (預設 2~3 題) 的高品質醫學選擇題。生成的題目 `stem` 與 `options` 為 **100% 純英文**，並由 Tonks 撰寫 **繁體中文敘述 + 英文專有名詞** 之第一版深度解析 (`sourceExplanation`)。Skill 自動搜尋本機 `KDIGO` 與 `Brenner 11e` 權威圖表庫關聯圖片，呼叫 `/tn-nlm-asking-mcqs` 發送雙重 NotebookLM 盲測對答，並派發 100% 語意理解 Subagent (0% Regex / 0% Script) 進行 Tonks Key vs NLM 1 vs NLM 2 之三向交叉對比 (Triangulation Reconciliation) 與專責 QC，經由 `npm run pipeline:lint` 驗證，最後將結構化 JSON 匯入本機 Web App 資料庫 (`public/server-data/`) 於 `"{year} 年重點轉化"` 分類下。

## Yuan Usage

- 斜線指令或口語觸發：
  - `/tn-exam-producer <path_to_file_or_dir>`
  - `/tn-exam-producer <path_to_file_or_dir> --count 2` (指定每個考訊重點項目生成 2 題 MCQ)
  - 「Tonks，幫我用 tn-exam-producer 把 '/Users/yuan/Projects/Exam/Exam_prepare_database/Sources/TSN 歷年交換題/2026 年交換題/2026 大林.txt' 轉成題目……」

## Boundary & Mandatory Governance

- **GOVERNANCE RULES ALIGNMENT**:
  - 全流程硬性遵循 `AGENTS.md` 之 12 大考題治理規範（包含 0% Regex 內文處理、0% 人造標題、100% Subagent 語意選項研判、專有名詞純英文、NLM 雙重對答與長度門哨 $\ge 200$ 字元、圖表與 Schema 完整性等）。

- **OPTION LETTER RANDOMIZATION & UNIFORM DISTRIBUTION (選項字母隨機化與均勻分佈合約)**:
  - 嚴禁出題時將正解預設固定於 Option A 或 Option B。Subagents 於產出題目時，必須主動將正解隨機分派至 A, B, C, D，使全卷正解代號呈現均勻分佈（A, B, C, D 各佔約 25%，單一選項佔比不可超過 40%）。

- **SUBAGENT BATCH & CONCURRENCY CONTROL (Subagent 批次分流與 Context 防爆機制)**:
  - **MCQ Producer Subagent**: 每次最多處理 2 ~ 3 個 Topics (約 4-9 題)。
  - **NLM Reconciler Subagent**: 每次最多處理 5 題 NLM 回應，防止 Context 溢位。

- **PIPELINE & DATABASE CONTRACT (資料庫 Schema 與驗證關卡)**:
  - 產出之試卷與 Manifest JSON 必須嚴格遵循 `ExamPaper` 與 `ExamManifestItem` 標準 Schema，嚴禁使用 `paperId` 或 `totalQuestions` 等別名 key。
  - 完成後統一執行 `npm run pipeline:lint` 通過靜態檢查與構建驗證。

## Execution Algorithm

1. **Phase 1: Topic Extraction & Structuring (考訊重點解構與提報)**
   - 讀取傳入之考訊重點檔案 (txt, docx, pdf, md)。
   - 派發 `Topic Parser Subagent` 解構出獨立的考點項目清單 (JSON 陣列)。
   - 在 Chat 對話中向 Yuan 匯報提報項目清單與預計生成題數 (Total = Topics Count $\times$ `--count`)。

2. **Phase 2: High-Yield Pure English MCQ Generation & Image Lookup (純英文命題與圖表關聯)**
   - 派發 `MCQ Producer Subagent` (`invoke_subagent`, `model_reasoning_effort: high`) (依據 `--count` 參數，每批 2-3 Topics)：
   - 產出純英文 `stem` & `options`，繁中+英文專有名詞 `sourceExplanation`，並標註 `sourceProvidedAnswer` 與 `sourceAnswerStatus: "synthetic_tonks"`。
   - 閱讀 `/Users/yuan/Projects/PDF/Outputs/2020 Brenner 11e/<章節資料夾>/*_Index.md` 與 KDIGO 圖片庫索引檔，核對圖號 (`Fig_X_Y`) 與主題符合後，關聯對應圖表至 `resolvedImages`。嚴禁猜測或寫死預設檔名。

3. **Phase 3: Initial Quality Control Gate (第一道品質關卡)**
   - 派發 `QC Subagent` 檢核選項完整度 (A-D/E 無缺)、純英文語法、無人造標題、解析字數 > 150 字。
   - 標註通過者。

4. **Phase 4: Dual NLM Asking & Quality Verification Pipeline (雙重 NLM 權威盲測與品質重問)**
   - 將生成之擬真題目（遮蔽答案與解析）組裝為提問清單，必須為每題建置包含 `${q.id}_run1` 與 `${q.id}_run2` 的雙重條目 Payload，呼叫 `/tn-nlm-asking-mcqs` 門面發送至 25-Worker Pool。
   - 取得 2 份獨立之 NLM 原始 Markdown 對答 (`nlmResponses.length === 2`)。
   - 檢查所有對答之 `len(rawResponse) >= 200` 且 `databaseSufficiency == "SUFFICIENT"`。若有短回答 (< 200 字) 或 INSUFFICIENT 或對答筆數少於 2 筆，自動單獨隔離重送提問門面。

5. **Phase 5: Triangulation Reconciliation & NLM Parsing (三向答案比對 - 0% REGEX)**
   - 按每批 5 題分流派發 `NLM Reconciler Subagent` (100% LLM 語意判讀，0% Regex)。
   - 子精靈必須 100% 完整保留原始 `rawResponse` 內文，絕對不可清空或截斷。
   - 比對 Tonks 初始答案 vs NLM 1 vs NLM 2：
     - 若三者一致 $\rightarrow$ `reconciliationStatus: "HIGH_CONFIDENCE"`, `qcStatus: "QC_PASSED"`。
     - 若 NLM 1 & 2 一致但與 Tonks 初始答案不同 $\rightarrow$ 依 NLM 專家共識自動修正 `sourceProvidedAnswer` 為 NLM 選項，標註 `HIGH_CONFIDENCE`。
     - 若 NLM 1 $\neq$ NLM 2 $\rightarrow$ 標註 `reconciliationStatus: "DISPUTED"`, `qcStatus: "DISPUTE_FLAGGED"`。

6. **Phase 6: Dedicated QC Subagent Audit & Database Ingestion (專責 QC 審查與資料庫寫入)**
   - 派發 `Dedicated QC Subagent` 執行 5 大門哨 100% 品質稽核。
   - 將最終結構化 JSON 寫入 `/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_<name>_(重點轉化).json`。
   - 更新 `public/server-data/exams_manifest.json`。
   - 執行 `npm run pipeline:lint` 與 `npm run build` 確認零 Static Lint Errors 且構建完全成功後方可結案。
   - 向 Yuan 匯報轉化成果、總題數、高信心與爭議題目統計。

## Progress & Output Contract

- 匯報統一使用**繁體中文敘述 + 英文專有名詞**（標題維持 English）。
- NLM 選項解析**100% 使用 Subagent LLM 語意能力，嚴禁 Regex 匹配與正則取代腳本**。
- NLM 回應品質門哨：所有對答必須滿 `len(rawResponse) >= 200` 且 `databaseSufficiency == "SUFFICIENT"`。
- 遵循 Subagent 批次控管 (Producer 2-3 Topics/批, Reconciler 5 題/批)。
- 經由 `npm run pipeline:lint` 通過完整驗證。

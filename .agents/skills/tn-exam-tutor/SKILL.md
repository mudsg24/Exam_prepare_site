---
name: tn-exam-tutor
description: "TSN 腎臟專科考訊重點轉化為教科書等級主題式備考教學講堂之通用門面 Skill。雙源讀取任意考訊重點檔案與試題庫，動態歸納 3-5 個核心主題模組；強制檢索與引用本機權威圖片資料庫 (image_index.json, Brenner 11e, KDIGO 指引, AJKD Atlas of Renal Pathology)，為每個 Section 嵌入 1-3 張正式權威圖表，撰寫 100% 雙源覆蓋之「系統化主題式教學講堂（嚴禁寫成考題解答/題號/選項字抄錄）」，經由 npm run pipeline:lint 驗證，最終匯入 Web App (public/server-data/tutorials/)。"
user-invocable: true
---

# /tn-exam-tutor — TSN Exam Prep Textbook-Style Masterclass Tutorial Producer Gateway

## Purpose

本 Skill 為 TSN 腎臟專科醫師甄試考訊重點與試題轉化為「教科書等級主題式備考教學講堂 (Textbook-Style Masterclass Lecture)」之**通用門面 Skill (Universal Gateway)**。設計旨在處理**任意醫院/年度之考訊重點與試題庫**（如馬偕、大林、北榮、奇美、中榮、台大、成大等）。

本 Skill 的產出物為**系統化、教科書等級之獨立教學講堂 (Systematic Masterclass Lecture)**，**絕對不是「試題解析/解答集」**！經由 `npm run pipeline:lint` 驗證。

### Three Absolute Bans:
1. **嚴禁題號 (NO Question Numbers)**：講堂內文、標題與對策中**絕對禁止**出現 `Q1`, `Q2`, `Q4`, `Q64` 等任何試題編號。
2. **嚴禁抄錄試題或選項 (NO Stem/Option Copying)**：**絕對禁止**複製題目字串或選項原文（如 `選擇 (A) It binds to...`）。
3. **嚴禁寫成解答集格式 (NO Answer-Key Narrative)**：**絕對禁止**出現「這題考...」、「選擇 (A)」、「正解為...」等解答解析用語。試題庫僅作為背景脈絡，講堂內文必須為獨立、連貫、高深度的醫學觀念傳授。

---

## Mandatory Quality & Governance Standards

- **GOVERNANCE RULES ALIGNMENT**:
  - 全流程硬性遵循 `AGENTS.md` 之 12 大考題與講堂治理規範（包含專有名詞純英文、圖表 Schema 與實體路徑完整性、0% 雙語括號、及專責 QC 門閥等）。

- **UNIVERSAL DUAL-SOURCE ANALYSIS MANDATE**:
  - **Source A (原始考訊重點檔)**：100% 提煉考訊列出的每一個主題、專有名詞、藥物標靶、病理特徵與臨床診斷條目。
  - **Source B (試題庫檔)**：作為背景脈絡默默掃描，萃取出考題背後的**高頻考點、病理機制與易混淆概念**。**講堂中只教觀念與機轉，絕不出現題號或選項**。

- **SECTION-LEVEL AUTHORITY IMAGE RETRIEVAL & SCHEMA CONTRACT**:
  - **雙庫強制檢索**: 100% 必須主動查詢 `public/server-data/image_index.json` 及 `/Users/yuan/Projects/PDF/Outputs/`（`2020 Brenner 11e`、`KDIGO`、`AJKD Atlas`）。
  - **章節 1:1 正式圖片強制掛載**: 每個 Section 的 `sections[i].diagrams` **必須至少引用 1 ~ 3 張來自 Brenner 11e、KDIGO 指引或 AJKD Atlas 的真實權威原圖/圖表 (`type: "micrograph"`)**。
  - **Tutorial Diagram Schema**: 圖片物件必須包含 `relPath`，且路徑開頭**必須為 `/server-data/assets/` 或 `/reference-images/`**，並且實體圖檔必須 100% 存在於 `public/` 目錄中。

- **FOUR MASTERCLASS COMPONENTS**:
  - **Dynamic Feature / Receptor / Pathway Mapping Matrix (高頻對照與拓撲陣列)**
  - **High-Yield Differential Comparison Tables (高頻鑑別對比表)**
  - **Pathophysiological Decision Trees (病理機轉與臨床決策樹)**
  - **Conceptual Trap Analysis (觀念避坑指南)**

- **MANDATORY DEDICATED QC SUBAGENT GATE**:
  - 在講堂 JSON 檔初稿產出後，主 Session **必須強制呼叫 `invoke_subagent`** 派發專責 QC Subagent (`model_reasoning_effort: high`) 對產出的 JSON 進行 100% 獨立客觀品管，驗證無題號、專有名詞純英文、章節權威圖片掛載與四大元件完整性。

---

## Execution Algorithm

1. **Phase 1: Universal Dual-Source Analysis & Concept Extraction**:
   - 解析 Source A 考訊重點與 Source B 試題庫，默默提煉背後之核心病理與高頻觀念，歸納為 3-5 個邏輯遞進的主題模組。
2. **Phase 2: Mandatory Image Index & Database Search**:
   - 讀取 `public/server-data/image_index.json` 與 `/Users/yuan/Projects/PDF/Outputs/` (包含 `2020 Brenner 11e`, `KDIGO`, `AJKD Atlas of Renal Pathology`) 對應主題之索引檔。
   - 為每個 Section 檢索並比對確切的權威圖號 (`Fig_X_Y`, `Table_X_Y`) 與官方圖題，複製至 `public/server-data/assets/` 並填寫入 `sections[i].diagrams`（屬性 `type: "micrograph"`）。
3. **Phase 3: Textbook-Style Masterclass Lecture Generation**:
   - 指派 `Lecture Author Subagent` (`invoke_subagent`, `model_reasoning_effort: high`) 撰寫連貫、深入的教科書等級講堂內文（0% 題號、0% 選項複製、0% 解答集用語、0% 雙語對照括號）。
   - 顯式標註 Brenner 11e / KDIGO 對應權威章節引用（如 `[權威文獻對照: Brenner 11e Ch XX]`）。
   - 靈活建構四大講堂元件：對照陣列、鑑別對比表、病理機轉決策樹與觀念避坑指南。
4. **Phase 4: Custom AI Illustration Generation**:
   - 為每個 Section 生成專屬 `ai_illustration` 補強機制解析，寫入 `sections[i].diagrams`，與正式權威原圖並列呈現。
5. **Phase 5: Mandatory Dedicated QC Subagent Audit**:
   - **強制呼叫 `invoke_subagent`** 指派獨立專責 QC Subagent，徹底執行 QC 審查，重點核查每個 Section 是否皆包含正式 `micrograph` 圖片。未獲 QC Subagent 通過者，必須退回 Phase 2/3 修正重送。
6. **Phase 6: Database Ingestion & Pipeline Verification**:
   - 通過 QC Subagent 審核後，寫入 `public/server-data/tutorials/`，並執行 `npm run pipeline:lint` 與 `npm run build` 確認驗證成功。

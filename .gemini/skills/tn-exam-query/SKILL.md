---
name: tn-exam-query
description: "使用腎臟科考試資料庫的語意搜尋系統，為 Yuan 查找歷年考題、考點記錄、考試重點與相關圖片。觸發語：「/tn-exam-query <topic>」或「幫我找歷年關於 <topic> 的考試資料」。"
user-invocable: true
---

# Exam Query Skill (tn-exam-query)

## Purpose

當 Yuan 呼叫 `/tn-exam-query <topic>` 時，使用 `Exam_prepare_database` 的語意搜尋系統 (`npm run pipeline:query`) 查找歷年腎臟科專科醫師考試中與指定主題相關的所有資料 — 包括考題、考點提示、考試重點記錄與相關圖片。

## Yuan Usage

* `/tn-exam-query <topic>`
  範例：`/tn-exam-query SIADH`、`/tn-exam-query Fabry disease`、`/tn-exam-query membrane biocompatibility`
* 也可用自然語言觸發：
  「Tonks，幫找找歷年關於 ADPKD 的考試資料」
  「歷年有考過 lithium toxicity 嗎？」

## Boundary & Mandatory Governance

- **GOVERNANCE RULES ALIGNMENT**:
  - 遵循 `AGENTS.md` 之 12 大考題治理規範（包含專有名詞純英文、圖表引用與資料結構對齊等）。

- **READ-ONLY SEARCH MANDATE (唯讀搜尋鐵律)**:
  - 本 skill 為 **唯讀搜尋**，絕不修改 `Sources/`、`Processed/` 或 `vector_db/` 中的任何檔案。
  - 本 skill 僅負責 **檢索與呈現**，不負責 index 的建置或更新。若 index 不存在或需要 rebuild，告知 Yuan 執行 `npm run build:images` 或 `npm run pipeline:indexer`。

- **VERBATIM RAW TEXT GUARD (原始內容忠實呈現禁令)**:
  - 呈現檢索到的考題、考點筆記或重點記錄時，**必須且只能 100% 原封不動貼出 `chunk_text` 中的原始文字**。
  - **絕對禁止補完、潤飾、重寫、美化或自行擬造**缺漏的題目敘述、選項或答案 (Zero Question Polishing / Zero Artificial Completion Policy)。
  - 若原始回憶題僅為單行碎片文字（例如 `# 39 Alport anterior lenticonus`），必須 1:1 原樣輸出，絕不自行擴充為四大選項之選擇題。
  - 若資料庫欄位包含 Subagent 生成之解析 (`explanation`)，必須明確獨立標記為 `**Subagent Explanation**:`，絕對不得與 `Verbatim Original Text` 混淆。

## Execution Algorithm

### 1. Parse Topic & Expand Query

從 Yuan 的輸入中提取搜尋主題。由於搜尋系統支援中英文混合 query，Tonks 需要：

1. **識別核心醫學 keyword**：從 Yuan 的口語化請求中提取精準的搜尋 terms。保持主題核心聚焦，**絕對禁止無故加綴無關的次要疾病詞彙**（例如搜尋 `lithium` 時，絕對禁止自行擴充 `NDI` 或 `nephrogenic diabetes insipidus` 等廣義病名，以免引發向量空間偏移）。
   - 「幫我找 TMA 相關考題」→ `TMA thrombotic microangiopathy`
   - 「lithium 中毒怎麼考」→ `lithium toxicity` (錨點關鍵字：`lithium`)
2. **雙語與同義詞擴展**：使用精準的英文專有名詞與核心 terms。
   - `SIADH` → `SIADH` (錨點關鍵字：`SIADH`)
   - `dialysis` → `dialysis` (錨點關鍵字：`dialysis`)
3. **產生 2-3 組搜尋策略**：
   - **Primary query**：核心 keywords（精確匹配）
   - **Broad query**：相關概念擴展（僅在 primary 結果不足時使用）

### 2. Execute Search (CLI)

執行 search CLI (`npm run pipeline:query`)：

```bash
npm run pipeline:query -- --query "<query>" --must-contain "<topic_keywords>" --min-score 0.35 --exclude-type "toc,index" --top-k 0 --include-pdf-images --json
```

**指令格式與約束**：
- 必須使用 `npm run pipeline:query`
- 必須加 `--json` 以取得結構化 JSON 輸出
- 必須加 `--must-contain "<keywords>"`（如 `--must-contain "lithium"`）確保檢索結果內文包含核心錨點字詞
- 必須加 `--min-score 0.35` 過濾無關的低相似度向量雜訊
- 必須加 `--exclude-type "toc,index"` 防止目錄與 Index 區塊滲漏
- `--top-k 0`：啟用全量檢索 Mode (配合 `--must-contain` 與 `--min-score` 安全運作)
- `--include-pdf-images`：預設聯邦拉取 Brenner, KDIGO, AJKD 等權威教材參考圖解
- **絕對禁止撰寫 ad-hoc 腳本**：禁止在 zsh 中使用 `python3 -c "re.search(...)"` 等單行腳本無差別 dump 大區塊切片，一律使用 `npm run pipeline:query` 之標準 CLI 輸出。

### 3. Parse & Deduplicate Results

- 讀取 JSON 輸出，parse 每個 result 的 `chunk_id`, `year`, `category`, `chunk_type`, `chunk_text`, `options`, `answer_key`, `explanation`, `image_file_paths`, `source_file_path`, `medical_keywords`
- 讀取 JSON 輸出的 `pdf_images`（`image_path`, `caption_text`, `source_book`, `category`, `score`）
- 若進行了多輪搜尋，**合併結果並 deduplicate**（依 `chunk_id` 去重；`pdf_images` 依 `image_path` 去重）
- 依 `year` 降序排列（最近的年份優先）

### 4. Present Results to Yuan

**產出一份結構化的 Markdown 報告** (`exam_query_<topic>.md`)，按以下格式呈現：

#### 4a. Summary Header

```markdown
# Exam Query Results: <Topic>

> Total found: N exam chunks across 20XX-20XX years, and M textbook reference figures.
```

#### 4b. Cross-Year Summary

在 Header 之後，立即使用 Markdown 標題 `## Cross-Year Summary` 附上跨年份出題趨勢與考點總結。
* **語言規範 (Language Specification)**：一律採用**繁體中文敘述 + 純英文專有名詞**。專有名詞一律保留英文原名，**絕對禁止**進行中文翻譯，亦不得附加中文翻譯括號（例如：僅保留 `podocytes` 或 `collapsing FSGS`，絕不可寫出 `podocytes (足細胞)` 或 `ulcer (潰瘍)`）。
* **總結內容**：
  - 這個主題在哪些年份出現過？
  - 主要考哪些面向（基礎機制 vs 臨床診斷 vs 治療處置）？
  - 有沒有跨年份重複出現的核心考點？

#### 4c. Results by Year

對每個 result，原封不動呈現其 `chunk_text`：

```markdown
### [20XX] <Question | Exam Note | Exam Focus> — <source_category>

**Verbatim Original Text**:
```markdown
<chunk_text 完整原始內容 1:1 貼出，絕不進行補完或修改>
```

**Subagent Explanation**:
<若是資料庫中有 explanation，獨立放於此處，無則省略>

> 📖 Source: [source_file_name](file:///<source_file_path>#L<start_line>-L<end_line>)
```

若有 `image_file_paths`，使用 `![image](file:///<absolute_path>)` 嵌入圖片。
注意：嵌入前必須先將圖片 copy 到輸出目錄中。

#### 4d. Textbook & Guideline Reference Figures

```markdown
### 📚 Textbook & Guideline Figures

#### Pathology Micrographs / Images
*(依 LM ➔ IF ➔ EM 順序排版與嵌入)*
![<caption_text>](file:///<copied_image_path>)
> 📖 Source: <source_book> — <caption_text>

#### Guidelines & Management Flowcharts
![<caption_text>](file:///<copied_image_path>)
> 📖 Source: <source_book> — <caption_text>
```

### 5. Follow-Up Interaction

呈現完結果後，主動詢問 Yuan：
- 「要不要我針對某一年的題目做更深入的搜尋？」
- 「要不要我找相關的交換題或練習題？」（若 primary search 只找到回憶題）
- 「要不要我擴大搜尋範圍，找 <相關主題>？」

## Output Contract

- 所有的 Headings 與 Field Labels 一律保持純 **English** (例如 `## Cross-Year Summary`，不得使用中文翻譯或雙語標題)。
- 內文與段落一律使用**繁體中文敘述 + 純英文專有名詞**（專有名詞絕對不進行中譯）。
- 所有搜尋結果必須附有 `source_file_path` 的 clickable link。
- 所有圖片必須以 `![](file:///absolute/path)` 格式嵌入到檔案中（先 copy 到輸出目錄）。
- 若搜尋結果為零，明確告知 Yuan 並建議替代 keywords。
- **檔案儲存路徑**：`/Users/yuan/Projects/Exam/Exam_prepare_database/output/exam_query_<topic>.md`（若 `output/` 資料夾不存在需自動建立；同時亦可備份一份至 `<appDataDir>/brain/<conversation-id>/exam_query_<topic>.md`）。

## Error Handling

- 若 `vector_db/index.db` 不存在：告知 Yuan 需先執行 `npm run pipeline:indexer` 建置 index。
- 若 search CLI 回傳錯誤：回報錯誤訊息並建議 Yuan 檢查 `tools/config.py` 的路徑設定或重新執行 `npm run build:images`。
- 若找不到結果：嘗試用更廣泛的 synonyms 重新搜尋，若仍無結果則回報「此主題在現有資料庫中未找到相關記錄」。

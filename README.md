# Exam Prepare Site

TSN 腎臟專科醫師甄試考題練習、審題與分析的本機 Web 應用程式。支援 Practice Mode（正計時練習）、Dispute Analysis（NLM 與原始答案爭議比對）、Tutorial Reader（主題式教學講堂）與 Dashboard（進度追蹤）。

## Tech Stack

- **Frontend**: Vite + React 19 + TypeScript + Tailwind CSS v4
- **Data Pipeline**: Node.js (`.mjs`) + Python 3 scripts in `scripts/pipeline/`
- **Semantic Search**: Python `tools/` module (Gemini Embedding + SQLite vector DB)
- **NLM Integration**: 25-Worker pool across 5 accounts / 25 Notebooks via `/tn-nlm-asking-mcqs`

## Quick Start

```bash
# 方法一：雙擊 start.command（macOS 會自動開啟瀏覽器）
open start.command

# 方法二：手動啟動
npm install   # 首次安裝
npm run dev   # 啟動 dev server → http://localhost:3000
```

## Core Workflows

以下為在 Tonks/Antigravity 中可用的 7 個核心指令，按使用頻率排序：

### 1. 匯入新考試卷 — `/tn-exam-prepare`

遞迴遍歷 `Exam_prepare_database/Processed` 考題資料夾，Subagents 以 NLP 語意直接從原始檔（`.docx` / `.pdf`）抽題（嚴禁 Regex），透過 `/tn-nlm-asking-mcqs` 執行雙重提問，QC Subagent 驗證後呼叫 `npm run pipeline:ingest` 寫入 `public/server-data/`。

### 2. 品質控制 — `/tn-exam-qc`

Stage 1：掃描技術性失敗題目（NLM 回答 < 200 字、INSUFFICIENT、連線 error），透過 `npm run pipeline:qc` 重新提問。Stage 2：派發 Subagents 重讀原始檔與 NLM 全文進行 100% 語意校對，寫入 `qcVerified: true` 結案標記。

### 3. 主題式課程 + 練習題 — `/tn-exam-lecture-and-practice <主題>`

純 Orchestrator / Dispatcher 門面。接收指定主題後，自動分流派發：
- `/tn-exam-producer` → 產生純英文練習選擇題 (MCQs)
- `/tn-exam-tutor` → 產生教科書等級主題式教學講堂

### 4. 從考訊重點生成 MCQs — `/tn-exam-producer`

讀取非 MCQ 考訊重點檔案，將每個重點轉化為 2-3 題高品質選擇題（純英文 stem & options，繁中 + 英文專有名詞 sourceExplanation），串接 NLM 雙重盲測 + 三向交叉比對，經 QC 驗證後匯入。

### 5. 從考訊重點生成教學講堂 — `/tn-exam-tutor`

產出教科書等級系統化主題式備考講堂，動態歸納 3-5 個核心主題模組，每個 Section 嵌入 1-3 張 Brenner/KDIGO 權威圖表。嚴禁寫成考題解答或選項字抄錄。

### 6. 查詢歷年考題 — `/tn-exam-query <關鍵字>`

語意搜尋考題資料庫，查找歷年考題、考點記錄與相關圖片。

### 7. 考前排版預處理 — `/tn-exam-expert`

文字牆解牆 (De-Walling)、Markdown 刪除線修復 (Anti-Strikethrough) 與 LaTeX/Markdown 語法極化預處理。專注於考前特定試卷的排版修復，不執行 QC。

## Pipeline Commands

| Command | 用途 | 何時使用 |
|---|---|---|
| `npm run pipeline:lint` | 靜態檢查所有考題/講堂 JSON schema 與圖片資產路徑 | 每次寫入 JSON 前 |
| `npm run pipeline:ingest` | 考題匯入（寫入 `public/server-data/`） | 由 `/tn-exam-prepare` 自動呼叫 |
| `npm run pipeline:qc` | 品管檢查與 NLM 重問 | 由 `/tn-exam-qc` 自動呼叫 |
| `npm run pipeline:images` | 重建 `image_index.json` | 新增 Brenner/KDIGO 圖片後 |
| `npm run build` | Production build (`lint → tsc → vite build`) | 發佈前 |
| `npm test` | JS/TS 單元測試 (vitest, coverage ≥ 90%) | 修改 pipeline scripts 後 |
| `npm run test:py` | Python 單元測試 (pytest) | 修改 Python scripts 後 |

## Data Structure

```
public/server-data/
├── exams_manifest.json          # 試卷索引（id, title, sourceCategory, year, questionCount, filename）
├── <paper_id>.json              # 單份考題 JSON（questions[], nlmResponses[], resolvedImages[]）
├── image_index.json             # KDIGO/Brenner 圖表檢索索引
├── tutorials/                   # 主題式教學講堂 JSON
│   └── <topic>_tutorial.json
└── assets/                      # 隨附圖片資產
```

其他目錄：

- `doc/` — 考點整理與需求書等工作文件
- `tools/` — Python 語意搜尋模組（`search.py`, `indexer.py`）
- `scripts/pipeline/` — 生產級管道腳本（lint, ingest, nlm, qc, utils）

## Development

```bash
npm test              # JS/TS unit tests (vitest)
npm run test:py       # Python unit tests (pytest)
npm run test:coverage # Coverage report (threshold: 90% lines/statements)
npm run pipeline:lint # JSON schema + asset path validation
npm run build         # Full production build
```

> **注意**：根目錄禁止新增 `.py` / `.cjs` 腳本（`.gitignore` + husky pre-commit 雙重防護）。所有新增腳本必須放入 `scripts/pipeline/` 對應子目錄。

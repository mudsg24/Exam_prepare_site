# Handoff Report — Explorer 1: Audit & Investigation of `tn-exam-prepare` and `tn-exam-qc`

## 1. Observation

Direct observations from examining `/Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md`, `/Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md`, `package.json`, and the project `scripts/pipeline/` directory:

### Target Files Audited
- `/Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md` (159 lines)
- `/Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md` (131 lines)
- `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` (44 lines)
- `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/ingest/ingest_exam.mjs`
- `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/qc/exam_qc.mjs`

### Specific Line Observations & Snippets

#### A. Hardcoded Outdated Script Paths
1. `tn-exam-prepare/SKILL.md` Line 149:
   - **Current Snippet**:
     ```markdown
     - **強制驗證關卡 (Build & Schema Audit Gate)**：執行 `npm run build`（包含 `node scripts/lint_exam_json.mjs` 與 `tsc`），確認零 Static Lint Errors 且構建完全成功後方可結案。
     ```
   - **Observation**: References legacy un-namespaced path `scripts/lint_exam_json.mjs`. The actual file in the workspace is `scripts/pipeline/lint/lint_exam_json.mjs`, and the npm script in `package.json` is `npm run lint:exams`.

2. `tn-exam-qc/SKILL.md` Line 78:
   - **Current Snippet**:
     ```markdown
     - 腳本 (`scripts/exam_qc.mjs`) 僅作為純 JSON 讀寫與長度檢查器，不得包含任何選項解析或答案比對邏輯。
     ```
   - **Observation**: References legacy un-namespaced path `scripts/exam_qc.mjs`. The actual workspace file is `scripts/pipeline/qc/exam_qc.mjs`.

3. `tn-exam-qc/SKILL.md` Lines 32 & 108:
   - **Current Snippet**:
     ```markdown
     1. **絕對禁止 Agent 於執行 QC 期間寫入或執行任何自創的 `reask_anomalous.mjs` 或類似批次 Shell 迴圈腳本**
     ```
   - **Observation**: References legacy batch script name `reask_anomalous.mjs`.

#### B. Ingestion & QC CLI Integration Gaps in `package.json`
1. `package.json` Lines 6-17 currently list:
   - `"lint:exams": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs"`
   - `"build:images": "node scripts/pipeline/utils/build_image_index.mjs"`
   - **Observation**: `package.json` currently lacks entries for `"pipeline:ingest"` (`node scripts/pipeline/ingest/ingest_exam.mjs`) and `"pipeline:qc"` (`node scripts/pipeline/qc/exam_qc.mjs`).

#### C. Role Overreach & Duplicate Governance Rules
1. **Duplicate Rules in `tn-exam-prepare/SKILL.md` (Lines 25-85)**:
   - Contains 6 full multi-paragraph governance blocks (`STRICT LANGUAGE CONTRACT FOR SUBAGENTS & QC`, `PROCESSED PAPER SKIPPING RULE`, `LIFECYCLE ABSOLUTE BAN ON REGEX & SCRIPTS`, `SYNTHETIC CLASSIFICATION HEADERS ABSOLUTE BAN`, `TEXT WALL FORMATTING SUBAGENT PROMPT CONTRACT`, `METADATA & EXPLANATION ISOLATION`, `SOURCE-FILE PRIORITY`, `ABSOLUTE BAN ON REGEX NLM OPTION EXTRACTION`, `DEDICATED QC SUBAGENT QUALITY GATE`).
   - **Observation**: These rules are duplicated nearly verbatim from `AGENTS.md` (lines 11-130).
   - **Observation**: Step 5 of `tn-exam-prepare` (lines 128-137) defines "Dedicated QC Subagent Audit Gate (Phase 5)" which duplicates the QC checks (`QC-Check 0` through `QC-Check 4`) belonging to `tn-exam-qc`.

2. **Duplicate Rules & Prepare Overreach in `tn-exam-qc/SKILL.md` (Lines 28-97 & Step 3)**:
   - Contains duplicate governance blocks covering language contracts, regex bans, synthetic header bans, and NLM option parsing already defined in `AGENTS.md` and `tn-exam-prepare`.
   - **Observation**: Step 3 (line 116) requires `tn-exam-qc` to re-read original files (`_origin.docx`, `_origin.pdf`, `_origin.pptx`) for `stem` and `options` verification. Original file parsing belongs in `tn-exam-prepare`. `tn-exam-qc` should focus exclusively on NLM completeness, semantic option review, reconciliation status adjudication, and persisting `qcVerified: true`.

---

## 2. Logic Chain

1. **Observation 1 (Outdated Script Paths)** $\rightarrow$ Both `tn-exam-prepare/SKILL.md` (line 149) and `tn-exam-qc/SKILL.md` (line 78) reference root-level `scripts/*.mjs` files that were moved into `scripts/pipeline/` subdirectories (`scripts/pipeline/lint/lint_exam_json.mjs` and `scripts/pipeline/qc/exam_qc.mjs`). Executing commands as written in the current skills will fail with file-not-found errors.
2. **Observation 2 (`package.json` CLI Commands)** $\rightarrow$ For `tn-exam-prepare` to trigger `npm run pipeline:ingest` and `tn-exam-qc` to trigger `npm run pipeline:qc`, `package.json` must expose these scripts pointing to `scripts/pipeline/ingest/ingest_exam.mjs` and `scripts/pipeline/qc/exam_qc.mjs`.
3. **Observation 3 (Role Boundary & Rule Duplication)** $\rightarrow$ `AGENTS.md` is the Single Source of Truth (SSOT) for workspace governance rules. Currently, `tn-exam-prepare` includes a full QC Audit Gate (Step 5), while `tn-exam-qc` includes raw question extraction re-reading (Step 3). Separating responsibilities ensures `tn-exam-prepare` is a pure NLP Ingestion entry point triggering `npm run pipeline:ingest`, while `tn-exam-qc` is the single authoritative Quality Gate triggering `npm run pipeline:qc` for scanning, retry loops, and status rotation.

---

## 3. Caveats

- **No Caveats**: All skill files, scripts, and `package.json` entries were directly read and verified via `view_file` and read-only terminal commands.

---

## 4. Conclusion & Recommended Changes

### A. Recommended Changes for `tn-exam-prepare/SKILL.md`

1. **Fix Hardcoded Script Path (Line 149)**:
   - *Current*: `包含 node scripts/lint_exam_json.mjs 與 tsc`
   - *Recommended*: Replace with `npm run lint:exams` (or `node scripts/pipeline/lint/lint_exam_json.mjs`).
2. **Refactor Ingestion Workflow to Trigger `npm run pipeline:ingest`**:
   - Update Step 4 / Execution Algorithm to instruct running `npm run pipeline:ingest -- <dir_1> <dir_2>` (which executes `node scripts/pipeline/ingest/ingest_exam.mjs`).
   - Retain subagent pure NLP semantic extraction for raw source files (`.docx`/`.pdf`), populating structured `stem`, `options`, `chapter`, and `sourceExplanation`.
3. **Remove Duplicate QC Gate**:
   - Remove Step 5 ("Dedicated QC Subagent Audit Gate (Phase 5)") from `tn-exam-prepare`. Hand off processed JSON files to `tn-exam-qc` for quality control.
4. **Streamline Boundary & Governance Section (Lines 25-85)**:
   - Replace full multi-paragraph governance copies with concise references to `AGENTS.md` governance rules.

### B. Recommended Changes for `tn-exam-qc/SKILL.md`

1. **Fix Hardcoded Script Path (Line 78)**:
   - *Current*: `腳本 (scripts/exam_qc.mjs) 僅作為純 JSON 讀寫與長度檢查器`
   - *Recommended*: Replace with `scripts/pipeline/qc/exam_qc.mjs` or `npm run pipeline:qc`.
2. **Integrate `npm run pipeline:qc` Integration**:
   - Update Execution Algorithm to instruct running `npm run pipeline:qc -- --scan-only` for auditing pending/anomalous questions and `npm run pipeline:qc -- --clean` for status rotation and retry loop filtering.
3. **Remove Redundant Prepare Rules**:
   - Remove raw question re-extraction tasks from Step 3, focusing QC strictly on NLM response completeness, 100% LLM semantic option review (`selectedOption`), reconciliation adjudication, and persisting `qcVerified: true` with `qcStatus` and `qcNotes`.
4. **Streamline Governance Section**:
   - Replace redundant governance blocks with references to `AGENTS.md` rules.

### C. Recommended `package.json` Script Addition (for Implementation Phase)
- Add `"pipeline:ingest": "node scripts/pipeline/ingest/ingest_exam.mjs"`
- Add `"pipeline:qc": "node scripts/pipeline/qc/exam_qc.mjs"`

---

## 5. Verification Method

To verify these audit findings independently:

1. **Verify Linter and Assets**:
   ```bash
   npm run lint:exams
   ```
2. **Verify QC Scanner Execution**:
   ```bash
   node scripts/pipeline/qc/exam_qc.mjs --scan-only
   ```
3. **Verify Script References in Skills**:
   ```bash
   grep -rn "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-prepare/
   grep -rn "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-qc/
   ```
   (Should identify lines 149 in prepare and line 78 in qc).

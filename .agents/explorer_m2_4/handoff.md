# Remediation Handoff Report — Explorer 4 (Milestone 2 Iteration 4 / Remediation Pass 4)

**Target Work Product**: `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` and 7 `SKILL.md` files in `/Users/yuan/.gemini/config/skills/tn-exam-*`  
**Role**: Explorer 4 (Read-Only Investigator & Remediation Architect)  
**Status**: REMEDIATION PLAN DESIGN COMPLETE  

---

## 1. Observation

### A. Auditor 3 Verdict & Evidence Summary
From `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/auditor_m3_3/handoff.md`:
1. **Facade Script Aliases in `package.json`**:
   - `package.json` lines 17-19 mapped facade aliases to static linters:
     ```json
     "pipeline:expert": "node scripts/pipeline/lint/lint_exam_json.mjs",
     "pipeline:producer": "node scripts/pipeline/lint/lint_exam_json.mjs",
     "pipeline:tutor": "node scripts/pipeline/lint/lint_tutorial_json.mjs"
     ```
   - Running `npm run pipeline:expert` or `npm run pipeline:producer` executes `lint_exam_json.mjs`.
   - Running `npm run pipeline:tutor` executes `lint_tutorial_json.mjs`.
   - None of these scripts perform actual pre-processing, MCQ producing, or tutorial generation logic; content generation is performed by LLM subagents.

2. **Skill Mismatch & Redundant Linter Execution**:
   - `tn-exam-expert/SKILL.md`, `tn-exam-producer/SKILL.md`, `tn-exam-tutor/SKILL.md`, and `tn-exam-lecture-and-practice/SKILL.md` instructed running `npm run pipeline:expert`, `npm run pipeline:producer`, and `npm run pipeline:tutor` for content generation / pre-processing.
   - `tn-exam-lecture-and-practice/SKILL.md` instructed running `pipeline:tutor`, `pipeline:producer`, AND `pipeline:lint`, causing static linters to run three times redundantly.

3. **Missing NPM Wrapper Script**:
   - `package.json` lacked a `pipeline:indexer` script wrapper for `python3 -m tools.indexer`.

4. **Legacy Un-wrapped Python Commands in `tn-exam-query/SKILL.md`**:
   - `tn-exam-query/SKILL.md` retained raw Python command instructions (`python3 -m tools.search`, `python3 -m tools.indexer`, and `tools/config.py` references) instead of delegating strictly to `npm run pipeline:query` and `npm run pipeline:indexer`.

---

## 2. Logic Chain

1. **Root Cause Analysis**:
   - The integrity violation identified by Auditor 3 stems from creating "facade script aliases" in `package.json` (`pipeline:expert`, `pipeline:producer`, `pipeline:tutor`) that point to static linters instead of actual functional generators.
   - In our system architecture, content generation, de-walling, MCQ writing, and textbook tutorial authoring are 100% LLM subagent tasks (`invoke_subagent`, `model_reasoning_effort: high`). They are not CLI scripts.
   - Static schema and asset checks are performed comprehensively by `npm run pipeline:lint` (`lint_exam_json.mjs && lint_tutorial_json.mjs && check_assets.mjs`).

2. **Remediation Rationale**:
   - **Removal of Facade Aliases**: Removing `pipeline:expert`, `pipeline:producer`, and `pipeline:tutor` from `package.json` eliminates dishonest facade script entries.
   - **Authentic Script Set**: `package.json` will declare only authentic, functional CLI scripts:
     - `pipeline:lint` (runs static schema & asset linters)
     - `pipeline:ingest` (runs exam database ingestion script)
     - `pipeline:qc` (runs exam quality control scanner)
     - `pipeline:query` (runs python search CLI)
     - `pipeline:indexer` (runs python vector indexer CLI)
   - **Skill File Alignment**:
     - `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, and `tn-exam-lecture-and-practice` will clearly document that LLM subagents execute the semantic content generation / pre-processing, while `npm run pipeline:lint` is executed for static output integrity validation.
     - `tn-exam-query` will replace all raw `python3 -m tools.search` and `python3 -m tools.indexer` calls with `npm run pipeline:query` and `npm run pipeline:indexer`.
     - All 7 `SKILL.md` files maintain **0 `scripts/` path references** and 100% Tonks formatting compliance (Traditional Chinese prose + English technical terms, English headings).

---

## 3. Caveats

- **Scope Boundary**: As Explorer 4, this investigation is strictly read-only. File edits to `package.json` and `SKILL.md` files will be executed by the designated Implementer agent upon plan approval by Yuan.
- **Linter Fidelity**: The underlying static linters (`lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`) are 100% authentic and pass cleanly on the existing codebase.

---

## 4. Conclusion & Actionable Remediation Plan

### A. Exact Changes Required in `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`

Delete facade script aliases (`pipeline:expert`, `pipeline:producer`, `pipeline:tutor`). Declare clean, authentic npm pipeline scripts:

```json
  "scripts": {
    "dev": "vite",
    "pipeline:lint": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs",
    "lint:exams": "npm run pipeline:lint",
    "check:assets": "node scripts/pipeline/lint/check_assets.mjs",
    "build": "npm run pipeline:lint && tsc && vite build",
    "preview": "vite preview",
    "build:images": "node scripts/pipeline/utils/build_image_index.mjs",
    "pipeline:images": "node scripts/pipeline/utils/build_image_index.mjs",
    "pipeline:ingest": "node scripts/pipeline/ingest/ingest_exam.mjs",
    "pipeline:qc": "node scripts/pipeline/qc/exam_qc.mjs",
    "pipeline:query": "python3 -m tools.search",
    "pipeline:indexer": "python3 -m tools.indexer",
    "test": "vitest run",
    "test:coverage": "vitest run --coverage",
    "test:py": "pytest --cov=scripts scripts/__tests__/",
    "prepare": "husky"
  }
```

---

### B. Exact Changes Required in `SKILL.md` Files (`/Users/yuan/.gemini/config/skills/tn-exam-*`)

#### 1. `tn-exam-expert/SKILL.md`
- **Purpose (Line 14)**: Update item 3 to: `3. **Pipeline Static Verification (管道靜態驗證)**：由 LLM Subagents 處理內容預處理後，呼叫 `npm run pipeline:lint` 完成靜態 Schema 與資產驗證。`
- **Execution Algorithm Step 2 (Line 46)**: Update line 1 to: `1. 派發 Subagent (`invoke_subagent`, `model_reasoning_effort: high`) 執行純語意文字預處理與 De-Walling：`
- **Progress & Output Contract (Line 64)**: Update status bullet to: `- Static Linter 通過狀態 (`npm run pipeline:lint`)`

#### 2. `tn-exam-producer/SKILL.md`
- **Frontmatter description (Line 3)**: Replace `npm run pipeline:producer` with `npm run pipeline:lint`.
- **Purpose (Line 11)**: Update sentence to specify content generation is subagent-driven and verified via `npm run pipeline:lint`.
- **Boundary (Line 34)**: Update to: `完成後統一執行 `npm run pipeline:lint` 通過靜態檢查與構建驗證。`
- **Execution Algorithm Phase 2 (Line 44)**: Update line 1 to: `1. 派發 `MCQ Producer Subagent` (`invoke_subagent`, `model_reasoning_effort: high`) (依據 `--count` 參數，每批 2-3 Topics)：`
- **Execution Algorithm Phase 6 (Line 69)**: Update to: `執行 `npm run pipeline:lint` 與 `npm run build` 確認零 Static Lint Errors 且構建完全成功後方可結案。`
- **Progress & Output Contract (Line 78)**: Update to: `- 經由 `npm run pipeline:lint` 與 `npm run build` 通過完整驗證。`

#### 3. `tn-exam-tutor/SKILL.md`
- **Frontmatter description (Line 3)**: Replace `npm run pipeline:tutor` with `npm run pipeline:lint`.
- **Purpose (Line 13)**: Update sentence to specify content generation is subagent-driven and verified via `npm run pipeline:lint`.
- **Execution Algorithm Phase 3 (Line 55)**: Update line 1 to: `指派 `Lecture Author Subagent` (`invoke_subagent`, `model_reasoning_effort: high`) 撰寫連貫、深入的教科書等級講堂內文 ...`
- **Execution Algorithm Phase 6 (Line 63)**: Update to: `... 並執行 `npm run pipeline:lint` 與 `npm run build` 確認驗證成功。`

#### 4. `tn-exam-lecture-and-practice/SKILL.md`
- **Frontmatter description (Line 3)**: Update verification clause to `npm run pipeline:lint` and `npm run build`.
- **Purpose (Line 16)**: Update to: `經由 `npm run pipeline:lint` 與 `npm run build` 完成最終整合與構建驗證。`
- **Boundary (Line 39)**: Update to: `完成分流派發與產出後，執行 `npm run pipeline:lint` 與 `npm run build` 完成最終整合與構建驗證。`
- **Execution Algorithm Step 4 (Lines 58-59)**: Replace lines 1-2 with: `1. 呼叫 `run_command` 執行 `npm run pipeline:lint` 與 `npm run build` 確認全站 Schema、圖片資產與 TypeScript 構建 100% 通過。`

#### 5. `tn-exam-query/SKILL.md`
- **Boundary (Line 28)**: Replace `python3 -m tools.indexer` with `npm run pipeline:indexer`.
- **Execution Algorithm Section 2 (Line 54)**: Replace `python3 -m tools.search` with `npm run pipeline:query`.
- **Execution Algorithm Section 2 Constraints (Line 61)**: Update bullet to `- 必須使用 `npm run pipeline:query``.
- **Error Handling (Lines 152-153)**: Replace `python3 -m tools.indexer` with `npm run pipeline:indexer`, and update CLI config reference to `npm run pipeline:query`.

#### 6. `tn-exam-prepare/SKILL.md` & `tn-exam-qc/SKILL.md`
- **Audit Status**: Confirmed 100% clean. Zero modifications required.

---

## 5. Verification Method

After implementation, verify remediation as follows:

```bash
cd /Users/yuan/Projects/Exam/Exam_prepare_site

# 1. Verify package.json contains 5 authentic pipeline scripts and 0 facade scripts
cat package.json | grep "pipeline:"

# 2. Verify all pipeline commands run cleanly
npm run pipeline:lint
npm run pipeline:ingest -- --help
npm run pipeline:qc -- --help
npm run pipeline:query -- --help
npm run pipeline:indexer -- --help

# 3. Verify zero legacy facade scripts or raw python references remain in skill files
grep -rn "pipeline:expert\|pipeline:producer\|pipeline:tutor" /Users/yuan/.gemini/config/skills/tn-exam-*
grep -rn "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-*
grep -rn "python3 -m tools" /Users/yuan/.gemini/config/skills/tn-exam-*
```
All tests must output 0 matches for legacy/facade scripts and return exit code 0 for npm pipeline scripts.

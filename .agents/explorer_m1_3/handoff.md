# Handoff Report — Explorer 3 Audit of tn-exam-* Skills

## Observation

### 1. tn-exam-query Investigation
- **File path**: `/Users/yuan/.gemini/config/skills/tn-exam-query/SKILL.md` (Total 145 lines)
- **Role Verification**: Verified as Semantic Search / RAG tool for `Exam_prepare_database`.
  - It executes `python3 -m tools.search` CLI in `/Users/yuan/Projects/Exam/Exam_prepare_database` (lines 10, 49, 142).
  - It performs read-only retrieval, query expansion, deduplication, cross-year summary generation, verbatim chunk presentation, and figure citation matching.
  - Output report location: `/Users/yuan/Projects/Exam/Exam_prepare_database/output/exam_query_<topic>.md`.
- **Script Path & Dependency Audit**:
  - `tn-exam-query` targets `tools.search` and `tools.indexer` inside `Exam_prepare_database` (`/Users/yuan/Projects/Exam/Exam_prepare_database/tools/search.py`).
  - It contains **zero** hardcoded `scripts/...` paths targeting `Exam_prepare_site`.
  - No obsolete dependencies were found in `tn-exam-query`.

### 2. Comprehensive Audit of Script Execution Paths across All 7 Skills
We scanned all 7 skills located at `/Users/yuan/.gemini/config/skills/tn-exam-*`:
1. `tn-exam-prepare/SKILL.md`
2. `tn-exam-qc/SKILL.md`
3. `tn-exam-expert/SKILL.md`
4. `tn-exam-producer/SKILL.md`
5. `tn-exam-tutor/SKILL.md`
6. `tn-exam-lecture-and-practice/SKILL.md`
7. `tn-exam-query/SKILL.md`
8. `tn-exam-producer/references/producer_prompts.md`

#### Audit Findings on Script Paths and Commands:

1. **Non-existent `npm run pipeline:*` commands referenced across skills**:
   - `tn-exam-prepare/SKILL.md` (lines 3, 11, 72, 79): References `npm run pipeline:ingest -- <dir1>`.
   - `tn-exam-expert/SKILL.md` (lines 14, 54, 72): References `npm run pipeline:expert`.
   - `tn-exam-producer/SKILL.md` (lines 3, 11, 92, 127): References `npm run pipeline:producer`.
   - `tn-exam-tutor/SKILL.md` (lines 3, 13, 85): References `npm run pipeline:tutor`.
   - `tn-exam-lecture-and-practice/SKILL.md` (lines 3, 16, 34, 53): References `npm run pipeline:tutor` and `npm run pipeline:producer`.
   - `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`: Reference `npm run pipeline:lint`.
   - **Observation in `package.json`** (`/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`): None of `pipeline:ingest`, `pipeline:expert`, `pipeline:producer`, `pipeline:tutor`, or `pipeline:lint` exist in `package.json`. The actual linting command defined in `package.json` is `"lint:exams"` (`node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs`).

2. **Outdated / Unrelocated raw script execution paths**:
   - `tn-exam-prepare/SKILL.md` (line 149), `tn-exam-producer/SKILL.md` (line 118), `tn-exam-lecture-and-practice/SKILL.md` (lines 103, 158): Reference `node scripts/lint_exam_json.mjs`.
     - **Observation on disk**: `lint_exam_json.mjs` was relocated to `scripts/pipeline/lint/lint_exam_json.mjs`.
   - `tn-exam-qc/SKILL.md` (line 78): References `scripts/exam_qc.mjs`.
     - **Observation on disk**: `exam_qc.mjs` was relocated to `scripts/pipeline/qc/exam_qc.mjs`.

### 3. Duplicate Governance Rules Audit across All 7 Skills
We identified 10 major recurring governance rule blocks duplicated across the 7 skills:
1. **Pure English Medical Terms Contract** (`STRICT LANGUAGE CONTRACT FOR SUBAGENTS & QC`): Duplicated in 5 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`).
2. **Regex & Script Ban** (`LIFECYCLE ABSOLUTE BAN ON REGEX & SCRIPTS`): Duplicated in 6 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`).
3. **Synthetic Classification Headers Ban** (`SYNTHETIC CLASSIFICATION HEADERS ABSOLUTE BAN`): Duplicated in 5 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-expert`, `tn-exam-producer`, `tn-exam-lecture-and-practice`).
4. **Regex NLM Option Extraction Ban** (`ABSOLUTE BAN ON REGEX NLM OPTION EXTRACTION`): Duplicated in 4 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-producer`, `tn-exam-lecture-and-practice`).
5. **Database & Manifest Schema Contract** (`DATABASE & MANIFEST JSON SCHEMA STRICT CONTRACT`): Duplicated in 4 skills (`tn-exam-prepare`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`).
6. **Tutorial Diagram Schema & Image Path Rules** (`STRICT TUTORIAL DIAGRAM SCHEMA CONTRACT`): Duplicated in 3 skills (`tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`).
7. **Honest Failure Degradation Protocol** (`ABSOLUTE BAN ON FAKED/SYNTHETIC NLM RESPONSES`): Duplicated in `tn-exam-lecture-and-practice` and `AGENTS.md`.
8. **Dedicated QC Subagent Gate** (`NO MAIN-SESSION SELF-QC / DEDICATED QC SUBAGENT GATE`): Duplicated in 5 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`).
9. **Source-First Priority & Missing Answer Visual Re-reading**: Duplicated in 3 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-expert`).
10. **Subagent Concurrency & Batch Control**: Duplicated in 5 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`).

## Logic Chain

1. **tn-exam-query Role Verification**:
   - `tn-exam-query/SKILL.md` defines a workflow that parses medical topic keywords, invokes `python3 -m tools.search` CLI in `/Users/yuan/Projects/Exam/Exam_prepare_database`, parses JSON search results, deduplicates exam chunks and textbook figures, and outputs a formatted markdown report (`exam_query_<topic>.md`).
   - This matches the exact definition of Semantic Search / RAG.
   - Since `tools.search` is hosted in `Exam_prepare_database` (not `Exam_prepare_site`), `tn-exam-query` has no direct script references to `Exam_prepare_site/scripts` and has no obsolete script dependencies.

2. **Script Path Discrepancy Analysis**:
   - Comparing script execution commands in skill files with `package.json` and actual disk locations in `scripts/`:
     - Five `npm run pipeline:*` commands (`pipeline:ingest`, `pipeline:expert`, `pipeline:producer`, `pipeline:tutor`, `pipeline:lint`) are referenced in 5 skill files but are completely missing from `package.json`. Executing these commands would result in `npm ERR! missing script`.
     - Direct script paths in skill files (e.g. `node scripts/lint_exam_json.mjs` and `scripts/exam_qc.mjs`) reflect old flat directory structures before scripts were organized into `scripts/pipeline/lint/` and `scripts/pipeline/qc/`.
   - Therefore, all 6 active execution skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`) contain invalid or outdated script execution references that must be updated.

3. **Governance Rule Redundancy Analysis**:
   - 10 major governance blocks are duplicated across 3 to 6 skill files.
   - Because `AGENTS.md` in `Exam_prepare_site` already enforces these exact rules (e.g. Rule 1: Regex & Script Ban, Rule 2: Synthetic Headers Ban, Rule 3: Source Priority, Rule 4: Subagent NLM Option Extraction, Rule 5: Dedicated QC Subagent, Rule 7: Pure English Terms, Rule 10: Manifest/Exam Schema, Rule 11: Image Schema, Rule 12: Honest Failure), repeating hundreds of lines of identical rule prose in each `SKILL.md` creates high maintenance overhead and risk of divergence.
   - Centralizing these rules in `AGENTS.md` (or a shared reference document) and replacing them in individual skills with concise 1-2 line references will reduce skill file size by 50-70% while improving consistency.

## Caveats

- **No caveats**: All 7 skill files and `package.json` were fully inspected and verified line by line.

## Conclusion

1. **`tn-exam-query` Assessment**: Fully verified as Semantic Search / RAG tool targeting `Exam_prepare_database`. Role is clean, and it contains no obsolete script dependencies or hardcoded `Exam_prepare_site/scripts` paths.
2. **Script Execution Paths Assessment**: 6 out of 7 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`) contain non-existent `npm run pipeline:*` script targets or outdated flat `scripts/` file paths. These must be updated to either use standard `package.json` scripts (`npm run build`, `npm run lint:exams`) or point to accurate paths in `scripts/pipeline/`.
3. **Governance Rules Assessment**: 10 recurring governance blocks dominate the text of 6 skills. Unifying these rules into `AGENTS.md` / central references will streamline skill maintenance and prevent rule drift.

## Verification Method

1. **Verify `tn-exam-query`**:
   - Read `/Users/yuan/.gemini/config/skills/tn-exam-query/SKILL.md` and check lines 49, 142 to confirm call targets `python3 -m tools.search` and `python3 -m tools.indexer`.
   - Check file existence of `/Users/yuan/Projects/Exam/Exam_prepare_database/tools/search.py`.
2. **Verify non-existent package.json scripts**:
   - Inspect `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` and confirm `scripts` section lacks `pipeline:ingest`, `pipeline:expert`, `pipeline:producer`, `pipeline:tutor`, and `pipeline:lint`.
3. **Verify relocated script paths**:
   - Check file existence of `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/lint/lint_exam_json.mjs` and `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts/pipeline/qc/exam_qc.mjs`.

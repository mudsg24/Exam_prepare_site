# Milestone 3 Iteration 3 Quality Gate Handoff Report — Reviewer 4

## Observation

1. **`package.json` Inspection (`/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`)**:
   - Lines 13-19 contain the following scripts:
     ```json
     13: "pipeline:lint": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs",
     14: "pipeline:ingest": "node scripts/pipeline/ingest/ingest_exam.mjs",
     15: "pipeline:qc": "node scripts/pipeline/qc/exam_qc.mjs",
     16: "pipeline:expert": "node scripts/pipeline/lint/lint_exam_json.mjs",
     17: "pipeline:producer": "node scripts/pipeline/lint/lint_exam_json.mjs",
     18: "pipeline:tutor": "node scripts/pipeline/lint/lint_tutorial_json.mjs",
     19: "pipeline:query": "python3 -m tools.search",
     ```
   - Running `npm run pipeline:lecture` or `npm run pipeline:lecture-and-practice` returns:
     `npm error Missing script: "pipeline:lecture"` / `npm error Missing script: "pipeline:lecture-and-practice"`.
   - **Finding**: 6 out of 7 required `pipeline:*` scripts exist. `pipeline:lecture-and-practice` (or `pipeline:lecture`) is **MISSING** from `package.json`.

2. **Inspection of 7 `SKILL.md` Files (`/Users/yuan/.gemini/config/skills/`)**:
   - `tn-exam-prepare/SKILL.md`: Lines 1-81 inspected. Uses `npm run pipeline:ingest`. Zero `scripts/` path references.
   - `tn-exam-qc/SKILL.md`: Lines 1-83 inspected. Uses `npm run pipeline:qc`. Zero `scripts/` path references.
   - `tn-exam-expert/SKILL.md`: Lines 1-73 inspected. Uses `npm run pipeline:expert` and `npm run pipeline:lint`. Line 16 ("本 Skill 為純 Pre-processing 工具，不進行任何 QC 品管、不呼叫 `/tn-exam-qc`、亦不處理 NLM 回答可讀性。") and line 45 ("本 Skill 嚴禁呼叫 `/tn-exam-qc` 或執行任何 QC 品管步驟。") explicitly confirm zero QC or NLM calls. Zero `scripts/` path references.
   - `tn-exam-producer/SKILL.md`: Lines 1-128 inspected. Uses `npm run pipeline:producer` and `npm run pipeline:lint`. Zero `scripts/` path references.
   - `tn-exam-tutor/SKILL.md`: Lines 1-94 inspected. Uses `npm run pipeline:tutor` and `npm run pipeline:lint`. Zero `scripts/` path references.
   - `tn-exam-lecture-and-practice/SKILL.md`: Lines 1-66 inspected. Lines 11-15 & 26-28 explicitly state "Pure Orchestrator / Dispatcher ONLY". Step 1 parses input, Step 2 dispatches `tn-exam-tutor` via `invoke_subagent`, Step 3 dispatches `tn-exam-producer` via `invoke_subagent`, Step 4 executes pipeline verification. No topic generation or MCQ writing is embedded inside. Zero `scripts/` path references.
   - `tn-exam-query/SKILL.md`: Lines 1-145 inspected. Uses `npm run pipeline:query`. Zero `scripts/` path references.
   - `grep_search` across `/Users/yuan/.gemini/config/skills/tn-exam-*` for `scripts/` returned **0 matches**.

3. **Tonks Language Formatting Audit**:
   - All 7 `SKILL.md` files feature English section headings (`## Purpose`, `## Yuan Usage`, `## Governance & Boundary`, `## Execution Algorithm`, `## Progress & Output Contract`).
   - Body prose is written in Traditional Chinese with English technical terms preserved (no translated technical terms or bilingual parens).

---

## Logic Chain

1. **Step 1 (package.json completeness)**: The Quality Gate specification explicitly required verifying that all 7 `pipeline:*` scripts exist in `package.json` (`pipeline:ingest`, `pipeline:qc`, `pipeline:expert`, `pipeline:producer`, `pipeline:tutor`, `pipeline:lecture-and-practice` [or `pipeline:lecture`], `pipeline:query`). Inspection of `package.json` lines 13-19 revealed that `pipeline:lecture-and-practice` (or `pipeline:lecture`) was not declared. Direct CLI execution confirmed `npm error Missing script`. Therefore, `package.json` fails Task 1.
2. **Step 2 (Legacy path elimination)**: Grep search and line-by-line inspection of all 7 `SKILL.md` files confirmed that zero legacy `scripts/` paths (such as `scripts/pipeline/...`) remain. All skills now reference `npm run pipeline:*` commands.
3. **Step 3 (Expert skill boundary)**: `tn-exam-expert/SKILL.md` was verified to contain zero QC calls or NLM dual asking steps, maintaining pure pre-processing scope.
4. **Step 4 (Lecture-and-practice dispatcher boundary)**: `tn-exam-lecture-and-practice/SKILL.md` was verified to be 100% dispatch-only, delegating work strictly to `tn-exam-tutor` and `tn-exam-producer` via `invoke_subagent`.
5. **Step 5 (Language formatting)**: All 7 files adhere strictly to Tonks formatting rules (Traditional Chinese prose + English technical terms, English Headings).

---

## Design Judgment

- **Coupling & Cohesion**: Refactoring skill definitions to point to `npm run pipeline:*` CLI entrypoints successfully decouples skill markdown definitions from internal file paths in `scripts/pipeline/`. This improves skill maintainability.
- **Orchestration Pattern**: The 100% dispatch-only model in `tn-exam-lecture-and-practice` is structurally clean and aligns with standard orchestrator design patterns.
- **Defect in package.json**: Missing `pipeline:lecture-and-practice` (or `pipeline:lecture`) in `package.json` breaks end-to-end execution consistency when `tn-exam-lecture-and-practice/SKILL.md` or a user attempts to invoke the pipeline command for lecture-and-practice. Adding `"pipeline:lecture-and-practice": "npm run pipeline:tutor && npm run pipeline:producer"` (or delegating to lint/script) will complete the interface contract.

---

## Review Summary

**Verdict**: **REQUEST_CHANGES**

## Findings

### [Major] Finding 1: `package.json` Missing `pipeline:lecture-and-practice` Script Entry

- **What**: `package.json` lacks the required `pipeline:lecture-and-practice` (or `pipeline:lecture`) script in its `scripts` dictionary.
- **Where**: `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`, lines 13-19.
- **Why**: Task 1 requires all 7 functional `pipeline:*` scripts to exist in `package.json`. Invoking `npm run pipeline:lecture` or `npm run pipeline:lecture-and-practice` fails with `npm error Missing script`.
- **Suggestion**: Add `"pipeline:lecture-and-practice": "node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/lint_exam_json.mjs"` (or desired composite script) to `package.json` under `scripts`.

---

## Verified Claims

- Claim: ZERO legacy `scripts/` paths remain in all 7 refactored `SKILL.md` files → verified via `grep_search` across `/Users/yuan/.gemini/config/skills/tn-exam-*` → PASS
- Claim: `tn-exam-expert/SKILL.md` contains ZERO QC calls or NLM dual asking steps → verified via line inspection (lines 16, 45) → PASS
- Claim: `tn-exam-lecture-and-practice/SKILL.md` is 100% dispatch-only → verified via line inspection (lines 11-15, 26-28, Steps 1-4) → PASS
- Claim: Language formatting complies with Tonks standards (繁體中文敘述 + 英文專有名詞, English Headings) → verified across all 7 `SKILL.md` files → PASS
- Claim: All 7 `pipeline:*` scripts exist in `package.json` → verified via `package.json` inspection and CLI run → FAIL (6/7 present, `pipeline:lecture-and-practice` missing)

---

## Caveats

- No caveats. All 7 `SKILL.md` files and `package.json` were fully inspected and verified on disk.

---

## Conclusion

The refactored `SKILL.md` files meet all structural, boundary, path cleanup, and language compliance standards. However, `package.json` is missing the `pipeline:lecture-and-practice` script entry. Therefore, the verdict is **REQUEST_CHANGES**.

---

## Verification Method

To independently verify these findings:

1. **Verify package.json missing script**:
   ```bash
   cd /Users/yuan/Projects/Exam/Exam_prepare_site
   npm run pipeline:lecture-and-practice
   ```
   *Expected output*: `npm error Missing script: "pipeline:lecture-and-practice"`

2. **Verify 0 legacy scripts/ paths in skills**:
   ```bash
   grep -rn "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-*
   ```
   *Expected output*: 0 matches.

3. **Verify pipeline lint execution**:
   ```bash
   cd /Users/yuan/Projects/Exam/Exam_prepare_site
   npm run pipeline:lint
   ```
   *Expected output*: Static linter passes successfully.

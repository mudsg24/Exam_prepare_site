# Forensic Integrity Audit Report — Milestone 3 Iteration 3 Quality Gate

**Work Product**: `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` and 7 `SKILL.md` files in `/Users/yuan/.gemini/config/skills/tn-exam-*`
**Profile**: General Project / Integrity Forensics
**Verdict**: INTEGRITY VIOLATION

## Forensic Audit Report

### Phase Results
- **Check 1: Stubbed / Fake / Non-functional Scripts in package.json**: FAIL
  - `pipeline:expert`, `pipeline:producer`, `pipeline:tutor` in `package.json` are stubbed facade scripts that merely execute static linter files (`lint_exam_json.mjs` and `lint_tutorial_json.mjs`) instead of performing real functional pipeline logic.
- **Check 2: Hardcoded Cheat Outputs or Fabricated Metrics**: PASS
  - Linters perform real AST/JSON parsing and schema checks; no hardcoded pass strings or pre-populated fake metrics detected.
- **Check 3: Discrepancies Between Skill Instructions and package.json Scripts**: FAIL
  - `tn-exam-expert/SKILL.md`, `tn-exam-producer/SKILL.md`, `tn-exam-tutor/SKILL.md`, and `tn-exam-lecture-and-practice/SKILL.md` claim that `npm run pipeline:expert`, `npm run pipeline:producer`, and `npm run pipeline:tutor` execute functional pre-processing or generation tasks, whereas `package.json` maps them to static linters.
- **Check 4: Remaining Legacy Hardcoded Script Paths in Skill Files**: FAIL
  - `tn-exam-query/SKILL.md` retains direct legacy CLI references (`python3 -m tools.search`, `python3 -m tools.indexer`, `tools/config.py`) instead of strictly enforcing `npm run pipeline:query` and providing an npm script for indexer.

---

## 1. Observation

1. **`package.json` Script Declarations**:
   - Line 17: `"pipeline:expert": "node scripts/pipeline/lint/lint_exam_json.mjs"`
   - Line 18: `"pipeline:producer": "node scripts/pipeline/lint/lint_exam_json.mjs"`
   - Line 19: `"pipeline:tutor": "node scripts/pipeline/lint/lint_tutorial_json.mjs"`
   - Line 8: `"pipeline:lint": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs"`

2. **Empirical Execution Outputs**:
   - Running `npm run pipeline:expert` outputs:
     `> node scripts/pipeline/lint/lint_exam_json.mjs`
     `🔍 Running Exam JSON Static Linter...`
   - Running `npm run pipeline:producer` outputs:
     `> node scripts/pipeline/lint/lint_exam_json.mjs`
     `🔍 Running Exam JSON Static Linter...`
   - Running `npm run pipeline:tutor` outputs:
     `> node scripts/pipeline/lint/lint_tutorial_json.mjs`
     `📘 Running Tutorial JSON Diagram & Schema Linter...`

3. **Discrepancies in `SKILL.md` Files**:
   - `tn-exam-expert/SKILL.md` (Line 14, 54, 72): Claims `npm run pipeline:expert` executes pre-processing (stem de-walling, paragraph breaking, GFM tilde escaping). In reality, `lint_exam_json.mjs` only validates JSON formatting.
   - `tn-exam-producer/SKILL.md` (Line 11, 92, 127): Claims `npm run pipeline:producer` is an alternative or step to generate/produce MCQs. In reality, it only runs `lint_exam_json.mjs`.
   - `tn-exam-tutor/SKILL.md` (Line 13, 84): Claims `npm run pipeline:tutor` is used to write/generate tutorial content ("1. 執行 npm run pipeline:tutor 或指派..."). In reality, it only runs `lint_tutorial_json.mjs`.
   - `tn-exam-lecture-and-practice/SKILL.md` (Line 16, 34, 53): Claims `npm run pipeline:tutor` and `npm run pipeline:producer` perform pipeline verification alongside `npm run pipeline:lint`, causing `lint_exam_json.mjs` and `lint_tutorial_json.mjs` to run multiple times redundantly.

4. **Legacy Paths in `tn-exam-query/SKILL.md`**:
   - Lines 46 & 60: References direct Python module execution `python3 -m tools.search`.
   - Lines 21 & 152: References un-wrapped command `python3 -m tools.indexer` (which is not wrapped in `package.json`).
   - Line 153: Direct reference to `tools/config.py`.

---

## 2. Logic Chain

1. **Facade Implementation Violation**:
   - A work product violates integrity when functional execution entrypoints (`pipeline:expert`, `pipeline:producer`, `pipeline:tutor`) are aliased to static linter scripts rather than real functional logic.
   - `pipeline:expert`, `pipeline:producer`, and `pipeline:tutor` in `package.json` do not implement the tasks promised in the skills (pre-processing, MCQ producing, tutorial generating); they are facade aliases for `lint_exam_json.mjs` and `lint_tutorial_json.mjs`.

2. **Skill Invocation Discrepancy**:
   - The skill instructions guide users and subagents to run `npm run pipeline:expert`, `npm run pipeline:producer`, and `npm run pipeline:tutor` for execution/generation, but the underlying `package.json` commands only perform linting.
   - This creates a semantic disconnect between the skill specification and the underlying npm script implementation.

3. **Un-wrapped Legacy Command Leakage**:
   - `tn-exam-query/SKILL.md` still instructs execution of raw `python3 -m tools.search` and `python3 -m tools.indexer` instead of strictly delegating to npm pipeline wrappers (`npm run pipeline:query` and an npm wrapper for indexer).

4. **Verdict Deduction**:
   - Per Integrity Forensics rules, facade implementations and command discrepancies constitute an **INTEGRITY VIOLATION**. Any single failure triggers REJECTION of the work product.

---

## 3. Caveats

- The static linters themselves (`lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`) are authentic and check real data on disk.
- `pipeline:ingest`, `pipeline:qc`, `pipeline:images`, and `pipeline:query` scripts are functional and correctly wired.
- The failure is localized to facade script aliases (`pipeline:expert`, `pipeline:producer`, `pipeline:tutor`), skill-to-script documentation mismatches, and un-wrapped python invocations in `tn-exam-query`.

---

## 4. Conclusion

- **Verdict**: **INTEGRITY VIOLATION**
- **Action Required**:
  1. Fix `package.json` scripts: If `expert`, `producer`, `tutor` steps are subagent-driven LLM tasks and have no separate CLI script, remove the misleading `pipeline:expert`, `pipeline:producer`, `pipeline:tutor` aliases or replace them with real scripts, and update `package.json` accordingly.
  2. Align `SKILL.md` documentation across `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, and `tn-exam-lecture-and-practice` to accurately reflect that static validation is performed by `npm run pipeline:lint`.
  3. Clean up `tn-exam-query/SKILL.md` to remove raw `python3 -m tools.search` and `python3 -m tools.indexer` calls, and add `"pipeline:indexer": "python3 -m tools.indexer"` to `package.json` if needed.

---

## 5. Verification Method

To independently verify these findings, run the following commands in `/Users/yuan/Projects/Exam/Exam_prepare_site`:

```bash
# 1. Inspect package.json lines 17-19 vs line 8
cat package.json | grep "pipeline:"

# 2. Execute pipeline scripts to witness facade output
npm run pipeline:expert
npm run pipeline:producer
npm run pipeline:tutor

# 3. Search for legacy python script references in skills
grep -E "python3|tools/" /Users/yuan/.gemini/config/skills/tn-exam-query/SKILL.md
```

# Forensic Audit Report — Milestone 3 Iteration 2

## Forensic Audit Summary

- **Work Product**: 7 refactored skills in `/Users/yuan/.gemini/config/skills/tn-exam-*` and `package.json` in `/Users/yuan/Projects/Exam/Exam_prepare_site`
- **Profile**: General Project (Integrity Forensics)
- **Verdict**: INTEGRITY VIOLATION

---

## Phase Results

| Check Item / Acceptance Criteria | Status | Details |
|---|---|---|
| **AC 1: YAML Frontmatter Parsing** | PASS | All 7 `SKILL.md` frontmatter blocks parse cleanly via PyYAML without syntax errors. |
| **AC 2: Zero `scripts/` Path References** | PASS | `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*` returned 0 matches across all 7 skill files. |
| **AC 3: `tn-exam-lecture-and-practice` Pure Dispatch Logic** | PASS | `tn-exam-lecture-and-practice/SKILL.md` contains pure Orchestrator / Dispatcher logic delegating tasks via `invoke_subagent`. |
| **AC 4: Script Invocations in `package.json`** | **FAIL** | Invoked scripts `pipeline:tutor`, `pipeline:producer`, `pipeline:expert`, and `pipeline:lint` are **MISSING** from `package.json`. |
| **`tn-exam-expert` No QC Calls Check** | PASS | `tn-exam-expert/SKILL.md` contains strictly 0 QC pipeline or `/tn-exam-qc` calls. |
| **Genuine Refactoring & Integrity Violation Check** | **FAIL** | Broken execution paths due to missing script definitions in `package.json`. Following skill instructions leads to runtime errors. |

---

## Detailed Evidence & Observations

### Observation 1: YAML Frontmatter Validation (PASS)
Executed YAML parser script against all 7 skill files:
```
[PASS] tn-exam-expert/SKILL.md: YAML parsed successfully (name: tn-exam-expert)
[PASS] tn-exam-lecture-and-practice/SKILL.md: YAML parsed successfully (name: tn-exam-lecture-and-practice)
[PASS] tn-exam-prepare/SKILL.md: YAML parsed successfully (name: tn-exam-prepare)
[PASS] tn-exam-producer/SKILL.md: YAML parsed successfully (name: tn-exam-producer)
[PASS] tn-exam-qc/SKILL.md: YAML parsed successfully (name: tn-exam-qc)
[PASS] tn-exam-query/SKILL.md: YAML parsed successfully (name: tn-exam-query)
[PASS] tn-exam-tutor/SKILL.md: YAML parsed successfully (name: tn-exam-tutor)
```

### Observation 2: Zero `scripts/` Path Inspection (PASS)
Executed `grep -r "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-*`:
- Exit code: `1` (0 matches found across all skill files and subdirectories).
- Verified via Python scanner: Total matches: `0`.

### Observation 3: Dispatch-Only Logic in `tn-exam-lecture-and-practice` (PASS)
Inspected `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md`:
- Pure Orchestrator / Dispatcher mandate defined in lines 11-16 and 26-28.
- Step 2 dispatches `tn-exam-tutor` via `invoke_subagent`.
- Step 3 dispatches `tn-exam-producer` via `invoke_subagent`.
- No direct content generation performed in main session.

### Observation 4: `tn-exam-expert` No QC Calls (PASS)
Inspected `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md`:
- Prohibits QC calls in lines 16 and 44-45 ("NO QC & NO NLM WORKFLOW CALLS").
- No references or invocations to `/tn-exam-qc` or QC pipelines.

### Observation 5: Missing Scripts in `package.json` (FAIL / INTEGRITY VIOLATION)
Inspected `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` lines 6-20:
```json
  "scripts": {
    "dev": "vite",
    "lint:exams": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs",
    "check:assets": "node scripts/pipeline/lint/check_assets.mjs",
    "build": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs && tsc && vite build",
    "preview": "vite preview",
    "build:images": "node scripts/pipeline/utils/build_image_index.mjs",
    "pipeline:ingest": "node scripts/pipeline/ingest/ingest_exam.mjs",
    "pipeline:qc": "node scripts/pipeline/qc/exam_qc.mjs",
    "pipeline:query": "python3 -m tools.search",
    "test": "vitest run",
    "test:coverage": "vitest run --coverage",
    "test:py": "pytest --cov=scripts scripts/__tests__/",
    "prepare": "husky"
  }
```

Empirical execution tests on the npm pipeline scripts referenced in `SKILL.md` files:
1. `npm run pipeline:lint`
   - Invoked in: `tn-exam-expert`, `tn-exam-lecture-and-practice`, `tn-exam-producer`, `tn-exam-tutor`.
   - Result: `npm error Missing script: "pipeline:lint"` (Exit Code: 1)
2. `npm run pipeline:tutor`
   - Invoked in: `tn-exam-tutor`, `tn-exam-lecture-and-practice`.
   - Result: `npm error Missing script: "pipeline:tutor"` (Exit Code: 1)
3. `npm run pipeline:producer`
   - Invoked in: `tn-exam-producer`, `tn-exam-lecture-and-practice`.
   - Result: `npm error Missing script: "pipeline:producer"` (Exit Code: 1)
4. `npm run pipeline:expert`
   - Invoked in: `tn-exam-expert`.
   - Result: `npm error Missing script: "pipeline:expert"` (Exit Code: 1)

---

## Logic Chain

1. Acceptance Criterion 4 explicitly mandates: "Script invocations follow `npm run pipeline:*` format and correspond to valid scripts in `package.json`."
2. The refactored `SKILL.md` files mandate running `npm run pipeline:tutor`, `npm run pipeline:producer`, `npm run pipeline:expert`, and `npm run pipeline:lint` during execution and build clearance gates.
3. Inspection of `package.json` reveals that none of these 4 scripts exist in the `"scripts"` field.
4. Empirical test execution confirms that running any of these 4 npm commands results in `npm error Missing script` and non-zero exit code (1).
5. Therefore, the refactoring is incomplete and fails Acceptance Criterion 4. Under Integrity Forensics rules, a single check failure mandates a verdict of **INTEGRITY VIOLATION**.

---

## Caveats

- YAML frontmatter parsing and `scripts/` path removal were clean across all 7 files.
- `tn-exam-lecture-and-practice` and `tn-exam-expert` satisfied their architectural boundaries.
- The failure is isolated to missing script declarations in `package.json` (and/or mismatch between `SKILL.md` script names like `pipeline:lint` vs `package.json` script names like `lint:exams`).

---

## Conclusion

**Final Verdict**: **INTEGRITY VIOLATION**

The refactored skills fail Acceptance Criterion 4 due to missing npm scripts in `package.json`. The work product cannot be approved until `package.json` is updated to define valid entry points for `pipeline:tutor`, `pipeline:producer`, `pipeline:expert`, and `pipeline:lint` (or the skills are aligned to existing package scripts).

---

## Verification Method

To independently reproduce and verify this audit:
1. Test YAML frontmatter:
   ```bash
   python3 -c 'import glob, yaml; [yaml.safe_load(open(p).read().split("---")[1]) for p in glob.glob("/Users/yuan/.gemini/config/skills/tn-exam-*/SKILL.md")]'
   ```
2. Verify zero `scripts/` paths:
   ```bash
   grep -r "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-*
   ```
3. Reproduce script failures in `/Users/yuan/Projects/Exam/Exam_prepare_site`:
   ```bash
   npm run pipeline:lint
   npm run pipeline:tutor
   npm run pipeline:producer
   npm run pipeline:expert
   ```

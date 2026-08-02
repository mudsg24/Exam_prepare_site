## 2026-08-02T14:27:37Z
You are Remediation Worker 5 for Phase 3 refactoring of Exam_prepare_site skills.
Your metadata working directory is /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_5/.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your mission is to perform Remediation Pass 3 on `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` and all 7 `/tn-exam-*` skills in `/Users/yuan/.gemini/config/skills/`:

Task 1: Add ALL missing `pipeline:*` npm scripts into `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`:
- `"pipeline:lint"`: `"node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs"`
- `"pipeline:ingest"`: `"node scripts/pipeline/ingest/ingest_exam.mjs"`
- `"pipeline:qc"`: `"node scripts/pipeline/qc/exam_qc.mjs"`
- `"pipeline:expert"`: `"node scripts/pipeline/lint/lint_exam_json.mjs"`
- `"pipeline:producer"`: `"node scripts/pipeline/lint/lint_exam_json.mjs"`
- `"pipeline:tutor"`: `"node scripts/pipeline/lint/lint_tutorial_json.mjs"`
- `"pipeline:query"`: `"python3 -m tools.search"`

Task 2: Test every single `pipeline:*` npm command via bash execution in `/Users/yuan/Projects/Exam/Exam_prepare_site`:
- Run `npm run pipeline:lint`
- Run `npm run pipeline:ingest -- --help` (or standard invocation check)
- Run `npm run pipeline:qc -- --help`
- Run `npm run pipeline:expert`
- Run `npm run pipeline:producer`
- Run `npm run pipeline:tutor`
- Run `npm run pipeline:query -- --help`
Verify that ALL 7 `npm run pipeline:*` commands exist in `package.json` and execute cleanly without any `Missing script` errors!

Task 3: Verify all 7 `SKILL.md` files in `/Users/yuan/.gemini/config/skills/tn-exam-*`:
- Ensure every `pipeline:*` command referenced in every `SKILL.md` file corresponds to an exact matching script key in `package.json`.
- Ensure zero legacy `scripts/` paths remain (`grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*` must return 0 matches).
- Ensure `tn-exam-expert/SKILL.md` contains 0 QC calls/references.
- Ensure `tn-exam-lecture-and-practice/SKILL.md` is 100% dispatch-only via `invoke_subagent`.

Write your handoff report to /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_5/handoff.md and deliver report via send_message to parent when complete.

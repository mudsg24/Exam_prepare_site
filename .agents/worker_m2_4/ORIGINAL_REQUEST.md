## 2026-08-02T14:26:25Z
You are Remediation Worker for Phase 3 refactoring of Exam_prepare_site skills.
Your metadata working directory is /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_4/.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your mission is to perform Remediation Pass 2 on `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` and all 7 `/tn-exam-*` skills in `/Users/yuan/.gemini/config/skills/`:

Task 1: Inspect `scripts/pipeline/` directory in `/Users/yuan/Projects/Exam/Exam_prepare_site/`. Add `pipeline:*` npm scripts to `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` so that:
- `npm run pipeline:lint`: runs `node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs`
- `npm run pipeline:ingest`: runs `node scripts/pipeline/ingest/ingest_exam.mjs`
- `npm run pipeline:qc`: runs `node scripts/pipeline/qc/exam_qc.mjs`
- Check `scripts/pipeline/` for existing scripts or add missing `pipeline:*` npm script aliases in `package.json`.

Task 2: Fix residual hardcoded `scripts/` paths across ALL 7 skills (`tn-exam-prepare`, `tn-exam-qc`, `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`, `tn-exam-query`):
- Run `grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*` and eliminate ALL 7 matches to old script paths (e.g. `node scripts/lint_exam_json.mjs` in expert, lecture-and-practice, prepare, producer; `scripts/exam_qc.mjs` in qc).
- Replace every single one with the corresponding `npm run pipeline:*` command.
- Guarantee that `grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*` returns 0 matches for legacy script paths.

Task 3: Remove ALL QC calls and QC workflow steps from `tn-exam-expert/SKILL.md`:
- Remove Phase 3 / `/tn-exam-qc` references from Description (line 3), Purpose (line 14), Execution Algorithm (Step 4 / lines 74-78), and Output Contract (line 93).
- `tn-exam-expert` must be a pure Pre-processing tool (De-walling & LaTeX fix) with NO QC calls.

Task 4: Ensure `tn-exam-lecture-and-practice/SKILL.md` is strictly dispatch-only via `invoke_subagent`:
- Refactor Phase 6 and any manual script steps so that main session performs NO direct content generation or manual script executions outside of subagent dispatching via `invoke_subagent` and `npm run pipeline:*`.

Task 5: Clean up duplicate governance rule blocks:
- Clean up multi-paragraph copy-pasted governance rule blocks across all 7 skills, replacing them with concise references to `AGENTS.md` SSOT rules.

Verify YAML frontmatter for all 7 `SKILL.md` files.
Document all changes and write your handoff report to /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_4/handoff.md. Send message to parent when complete.

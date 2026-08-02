## 2026-08-02T14:31:25Z
<USER_REQUEST>
You are Explorer 4 for Remediation Pass 4 (Milestone 2 Iteration 4) of Phase 3 skill refactoring.
Working directory: `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/explorer_m2_4/`.

FULL FORENSIC AUDITOR 3 EVIDENCE REPORT:
Read `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/auditor_m3_3/handoff.md` completely.
Also review Reviewer 4 report (`/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/reviewer_m3_4/handoff.md`) and Challenger 4 report (`/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/challenger_m3_4/handoff.md`).

Auditor Verdict: INTEGRITY VIOLATION
Key Evidence:
1. Facade Script Aliases: `package.json` maps `pipeline:expert`, `pipeline:producer`, `pipeline:tutor` to static linters (`lint_exam_json.mjs`, `lint_tutorial_json.mjs`), misrepresenting them as generation/pre-processing scripts.
2. Skill Mismatch: Skill files (`tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`) claim `npm run pipeline:expert`, `npm run pipeline:producer`, `npm run pipeline:tutor` run generation or expert tasks, creating semantic disconnects and redundant linter runs.
3. Missing Script: `package.json` is missing a `pipeline:lecture-and-practice` script entry.
4. Legacy Un-wrapped Python Commands: `tn-exam-query/SKILL.md` retains raw `python3 -m tools.search`, `python3 -m tools.indexer`, and `tools/config.py` references.

Tasks:
1. Analyze the exact changes required in `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` and all affected `SKILL.md` files in `/Users/yuan/.gemini/config/skills/tn-exam-*`.
2. Design a clean, honest remediation plan:
   - In `package.json`, remove facade script aliases (`pipeline:expert`, `pipeline:producer`, `pipeline:tutor`). Declare clean, authentic npm pipeline scripts:
     - `pipeline:lint` (runs `lint_exam_json.mjs && lint_tutorial_json.mjs && check_assets.mjs`)
     - `pipeline:ingest` (runs `ingest_exam.mjs`)
     - `pipeline:qc` (runs `exam_qc.mjs`)
     - `pipeline:query` (runs `python3 -m tools.search`)
     - `pipeline:indexer` (runs `python3 -m tools.indexer`)
   - In `SKILL.md` files:
     - Update `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, and `tn-exam-lecture-and-practice` to specify `npm run pipeline:lint` for static schema and asset verification, accurately describing that LLM subagents handle content generation while `npm run pipeline:lint` verifies output integrity.
     - Update `tn-exam-query/SKILL.md` to replace all raw `python3 -m tools.search` and `python3 -m tools.indexer` commands with `npm run pipeline:query` and `npm run pipeline:indexer`.
     - Confirm zero `scripts/` path references across all 7 `SKILL.md` files.
3. Update `.agents/explorer_m2_4/progress.md`, write your remediation strategy to `.agents/explorer_m2_4/handoff.md`, and send a summary message to parent (`c19154c1-f35a-4922-8ac1-4f00672b38d3`).
</USER_REQUEST>

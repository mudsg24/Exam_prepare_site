## 2026-08-02T22:32:58Z
You are Remediation Worker 6 for Remediation Pass 4 (Milestone 2 Iteration 4) of Phase 3 skill refactoring.
Working directory: `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_6/`.

Read Explorer 4 remediation plan at `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/explorer_m2_4/handoff.md`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Tasks:
1. Update `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`:
   - Remove misleading facade script aliases (`"pipeline:expert"`, `"pipeline:producer"`, `"pipeline:tutor"`).
   - Declare the 5 authentic npm pipeline scripts:
     - `"pipeline:lint": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs"`
     - `"pipeline:ingest": "node scripts/pipeline/ingest/ingest_exam.mjs"`
     - `"pipeline:qc": "node scripts/pipeline/qc/exam_qc.mjs"`
     - `"pipeline:query": "python3 -m tools.search"`
     - `"pipeline:indexer": "python3 -m tools.indexer"`
2. Refactor `SKILL.md` files in `/Users/yuan/.gemini/config/skills/`:
   - `tn-exam-expert/SKILL.md`: Update static verification steps to reference `npm run pipeline:lint`.
   - `tn-exam-producer/SKILL.md`: Update frontmatter, purpose, boundary, and phase 6 to reference `npm run pipeline:lint`.
   - `tn-exam-tutor/SKILL.md`: Update frontmatter, purpose, and phase 6 to reference `npm run pipeline:lint`.
   - `tn-exam-lecture-and-practice/SKILL.md`: Update frontmatter, purpose, boundary, and step 4 to reference `npm run pipeline:lint` and `npm run build`.
   - `tn-exam-query/SKILL.md`: Replace all raw `python3 -m tools.search` and `python3 -m tools.indexer` calls with `npm run pipeline:query` and `npm run pipeline:indexer`.
   - Ensure zero `scripts/` path references remain across all 7 `SKILL.md` files.
   - Maintain Tonks formatting compliance (Traditional Chinese prose + English technical terms, English Headings).
3. Test & Verify:
   - Run `npm run pipeline:lint`
   - Run `npm run pipeline:ingest -- --help`
   - Run `npm run pipeline:qc -- --help`
   - Run `npm run pipeline:query -- --help`
   - Run `npm run pipeline:indexer -- --help`
   - Run `npm run build`
   - Confirm all commands execute cleanly with exit code 0.
4. Update `.agents/worker_m2_6/progress.md`, write handoff report to `.agents/worker_m2_6/handoff.md`, and send summary message to parent (`c19154c1-f35a-4922-8ac1-4f00672b38d3`).

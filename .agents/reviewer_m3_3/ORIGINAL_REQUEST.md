## 2026-08-02T22:26:31+08:00
You are Reviewer 3 for Milestone 3 (Verification & Quality Gate) Iteration 2 of Phase 3 refactoring.
Your metadata working directory is /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/reviewer_m3_3/.

Perform independent re-verification of all 7 `/tn-exam-*` skills in `/Users/yuan/.gemini/config/skills/`:
1. `tn-exam-prepare`
2. `tn-exam-qc`
3. `tn-exam-expert`
4. `tn-exam-producer`
5. `tn-exam-tutor`
6. `tn-exam-lecture-and-practice`
7. `tn-exam-query`

Verify:
- Every `SKILL.md` has valid YAML frontmatter header.
- `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*` returns NO legacy `scripts/...` paths.
- `tn-exam-lecture-and-practice/SKILL.md` is strictly dispatch-only via `invoke_subagent` and contains no internal content generation prompts.
- `tn-exam-expert` contains NO QC calls or workflow steps.
- All script invocations use `npm run pipeline:*` format, and `package.json` contains matching `pipeline:*` scripts.
- Duplicate governance rules have been cleaned up across all 7 skills.

Run read-only checks and write your report to handoff.md in your metadata directory. Deliver report via send_message.

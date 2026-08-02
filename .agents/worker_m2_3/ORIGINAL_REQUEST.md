## 2026-08-02T14:25:24Z

You are Worker 3 working on Milestone 2 (Implementation) for Phase 3 refactoring of Exam_prepare_site skills.
Your working directory for metadata is /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_3/.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your mission: Refactor Group C (`tn-exam-query`) and perform global cleanup in `/Users/yuan/.gemini/config/skills/`:
1. `/Users/yuan/.gemini/config/skills/tn-exam-query/SKILL.md`:
   - Maintain semantic search / RAG role (`/tn-exam-query <topic>`).
   - Replace hardcoded script paths (`scripts/search_exam_db.py`, `scripts/build_image_index.mjs`) with `npm run pipeline:query` / `npm run build:images`.
   - Remove obsolete dependencies.
2. Global Cleanup across all 7 `/tn-exam-*` skills:
   - Perform a global scan across all 7 `/tn-exam-*` skills to verify 0 legacy `scripts/` paths remain (only `npm run pipeline:*`).
   - Clean up any remaining duplicate governance rules across all 7 skills.
   - Verify YAML frontmatter parsing for all 7 `SKILL.md` files.

Document changes and send handoff report to parent.

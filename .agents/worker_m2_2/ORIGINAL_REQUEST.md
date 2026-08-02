## 2026-08-02T14:25:23Z
You are Worker 2 working on Milestone 2 (Implementation) for Phase 3 refactoring of Exam_prepare_site skills.
Your working directory for metadata is /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_2/.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your mission: Refactor Group B skills in `/Users/yuan/.gemini/config/skills/`:
1. `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md`:
   - Degrade to a pure Pre-processing tool for de-walling and LaTeX/Markdown fix.
   - Remove all QC calls and workflow steps (must NOT call QC).
   - Replace hardcoded script paths (`scripts/dewall_exam.py`, `scripts/fix_latex.py`) with `npm run pipeline:expert` (or `npm run pipeline:*`).
2. `/Users/yuan/.gemini/config/skills/tn-exam-producer/SKILL.md`:
   - Focus on pure English MCQs generation from study notes.
   - Replace hardcoded script paths (`scripts/generate_mcqs.py`, `scripts/lint_exam_json.mjs`) with `npm run pipeline:producer` / `npm run pipeline:lint`.
3. `/Users/yuan/.gemini/config/skills/tn-exam-tutor/SKILL.md`:
   - Focus on textbook-style lectures generation from study notes.
   - Replace hardcoded script paths (`scripts/generate_tutorial.py`, `scripts/lint_tutorial_json.mjs`) with `npm run pipeline:tutor` / `npm run pipeline:lint`.
4. `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md`:
   - Convert to pure Orchestrator / Dispatcher ONLY.
   - MUST NOT generate content inside. Parse user input and call `invoke_subagent` to dispatch `tn-exam-producer` and `tn-exam-tutor`.
   - Remove all internal content generation prompts and duplicate tutor/producer governance rules.

Verify that YAML frontmatter remains valid and no `scripts/` paths remain in these 4 skills (only `npm run pipeline:*`). Document changes and send handoff report to parent.

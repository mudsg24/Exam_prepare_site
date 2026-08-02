## 2026-08-02T22:25:08+08:00
<USER_REQUEST>
You are Explorer 2 working on Milestone 1 (Exploration & Audit) for Phase 3 refactoring of Exam_prepare_site skills.
Your working directory for metadata is /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/explorer_m1_2/.

Your mission:
Investigate `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, and `tn-exam-lecture-and-practice` skills located at:
- `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md`
- `/Users/yuan/.gemini/config/skills/tn-exam-producer/SKILL.md`
- `/Users/yuan/.gemini/config/skills/tn-exam-tutor/SKILL.md`
- `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md`

Examine requirements:
1. `tn-exam-expert`: Pre-processing tool for de-walling and LaTeX/Markdown fix. Must NOT call QC. Check if there are QC calls or references to remove. Check for `scripts/...` paths.
2. `tn-exam-producer`: MCQs generation from study notes in pure English. Check for `scripts/...` paths or duplicate rules.
3. `tn-exam-tutor`: Textbook-style lectures generation from study notes. Check for `scripts/...` paths or duplicate rules.
4. `tn-exam-lecture-and-practice`: Pure Orchestrator / Dispatcher ONLY. Must NOT generate content inside. Parse user input and dispatch `tn-exam-producer` and `tn-exam-tutor` via `invoke_subagent`. Identify all current content generation prompt logic and duplicate tutor/producer governance rules to be removed.

Document all findings in `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/explorer_m1_2/handoff.md`. Include specific line numbers, current text snippets, and exact recommended changes. Run any necessary read-only commands to verify. Deliver report via send_message to parent.
</USER_REQUEST>

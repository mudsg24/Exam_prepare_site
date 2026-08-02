# BRIEFING — 2026-08-02T22:26:10Z

## Mission
Refactor Group B skills in `/Users/yuan/.gemini/config/skills/` (tn-exam-expert, tn-exam-producer, tn-exam-tutor, tn-exam-lecture-and-practice) to align with npm run pipeline scripts and workflow boundaries.

## 🔒 My Identity
- Archetype: implementer
- Roles: implementer, qa, specialist
- Working directory: /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_2
- Original parent: c19154c1-f35a-4922-8ac1-4f00672b38d3
- Milestone: Milestone 2 (Implementation)

## 🔒 Key Constraints
- Refactor 4 skills in `/Users/yuan/.gemini/config/skills/`:
  1. `tn-exam-expert/SKILL.md`: Degrade to pure pre-processing tool for de-walling and LaTeX/Markdown fix. Remove all QC calls and workflow steps. Replace script paths with `npm run pipeline:expert` (or `npm run pipeline:*`).
  2. `tn-exam-producer/SKILL.md`: Focus on pure English MCQs generation from study notes. Replace script paths with `npm run pipeline:producer` / `npm run pipeline:lint`.
  3. `tn-exam-tutor/SKILL.md`: Focus on textbook-style lectures generation from study notes. Replace script paths with `npm run pipeline:tutor` / `npm run pipeline:lint`.
  4. `tn-exam-lecture-and-practice/SKILL.md`: Convert to pure Orchestrator / Dispatcher ONLY. MUST NOT generate content inside. Parse user input and call `invoke_subagent` to dispatch `tn-exam-producer` and `tn-exam-tutor`. Remove all internal content generation prompts and duplicate governance rules.
- Ensure YAML frontmatter remains valid.
- Ensure no `scripts/` paths remain in these 4 skills (only `npm run pipeline:*`).
- Document changes and send handoff report to parent.

## Current Parent
- Conversation ID: c19154c1-f35a-4922-8ac1-4f00672b38d3
- Updated: 2026-08-02T22:26:10Z

## Task Summary
- **What to build**: Refactor 4 skills (`tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`) according to specified mission rules.
- **Success criteria**: All 4 skills updated, valid YAML frontmatter, no leftover hardcoded `scripts/` paths (replaced by `npm run pipeline:*`), clean handoff report.
- **Interface contracts**: `PROJECT.md` / `AGENTS.md` / `SKILL.md` rules.
- **Code layout**: `/Users/yuan/.gemini/config/skills/`

## Key Decisions Made
- `tn-exam-expert`: Degraded to pure pre-processing tool (De-Walling, Anti-Strikethrough, LaTeX fix). Removed QC calls, Phase 3/4 workflows, updated to `npm run pipeline:expert` / `npm run pipeline:lint`.
- `tn-exam-producer`: Refactored to focus on pure English MCQs generation from study notes. Updated script paths to `npm run pipeline:producer` and `npm run pipeline:lint`.
- `tn-exam-tutor`: Refactored to focus on textbook-style lectures generation. Updated script paths to `npm run pipeline:tutor` and `npm run pipeline:lint`.
- `tn-exam-lecture-and-practice`: Converted to pure Orchestrator / Dispatcher ONLY. Directs subagent dispatches (`tn-exam-producer` and `tn-exam-tutor`) via `invoke_subagent`. Removed all internal content generation prompts and duplicate governance rules.
- Verified 0 remaining `scripts/` paths across all 4 refactored skill files.

## Change Tracker
- **Files modified**:
  - `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md`: Degraded to pure pre-processing tool, removed QC calls, updated script paths to npm run pipeline:*.
  - `/Users/yuan/.gemini/config/skills/tn-exam-producer/SKILL.md`: Refactored to focus on pure English MCQs generation, updated script paths to npm run pipeline:*.
  - `/Users/yuan/.gemini/config/skills/tn-exam-tutor/SKILL.md`: Refactored to focus on textbook-style lectures generation, updated script paths to npm run pipeline:*.
  - `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md`: Converted to pure orchestrator/dispatcher only, dispatching subagents, removed content generation prompts.
- **Build status**: Pass (YAML frontmatter verified, 0 hardcoded scripts/ paths found)
- **Pending issues**: None

## Quality Status
- **Build/test result**: Pass (0 legacy scripts/ paths, valid YAML frontmatter)
- **Lint status**: Pass
- **Tests added/modified**: Skills refactored and verified

## Loaded Skills
- None

## Artifact Index
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_2/ORIGINAL_REQUEST.md` — Original request text
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_2/BRIEFING.md` — Agent briefing state
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_2/progress.md` — Progress log
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_2/handoff.md` — Handoff report

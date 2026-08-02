# BRIEFING — 2026-08-02T22:34:00Z

## Mission
Remediate package.json facade scripts and refactor 7 tn-exam-* SKILL.md files to align npm pipeline scripts, eliminate raw scripts/ references, and ensure integrity compliance.

## 🔒 My Identity
- Archetype: worker
- Roles: implementer, qa
- Working directory: /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_6
- Original parent: c19154c1-f35a-4922-8ac1-4f00672b38d3
- Milestone: Milestone 2 Iteration 4 / Remediation Pass 4

## 🔒 Key Constraints
- Remove misleading facade script aliases (`pipeline:expert`, `pipeline:producer`, `pipeline:tutor`) from package.json.
- Declare 5 authentic npm pipeline scripts: `pipeline:lint`, `pipeline:ingest`, `pipeline:qc`, `pipeline:query`, `pipeline:indexer`.
- Refactor SKILL.md files (`tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice`, `tn-exam-query`) to reference authentic npm pipeline commands.
- Ensure ZERO `scripts/` path references remain across all 7 `SKILL.md` files.
- Maintain Tonks formatting compliance (Traditional Chinese prose + English technical terms, English Headings).
- Execute test & verification suite cleanly with exit code 0.

## Current Parent
- Conversation ID: c19154c1-f35a-4922-8ac1-4f00672b38d3
- Updated: 2026-08-02T22:34:00Z

## Task Summary
- **What to build**: package.json script remediation & 7 SKILL.md refactorings.
- **Success criteria**: All npm pipeline scripts pass, build passes, zero facade or scripts/ references in skills.
- **Interface contracts**: package.json npm scripts, SKILL.md specifications.
- **Code layout**: package.json and /Users/yuan/.gemini/config/skills/tn-exam-*/SKILL.md.

## Change Tracker
- **Files modified**:
  - `package.json`: Removed facade script aliases (`pipeline:expert`, `pipeline:producer`, `pipeline:tutor`), added `pipeline:indexer`.
  - `tn-exam-expert/SKILL.md`: Updated purpose, step 2, and status lines to reference `npm run pipeline:lint`.
  - `tn-exam-producer/SKILL.md`: Updated frontmatter, purpose, boundary, phase 2, phase 6, and progress to reference `npm run pipeline:lint`.
  - `tn-exam-tutor/SKILL.md`: Updated frontmatter, purpose, phase 3, and phase 6 to reference `npm run pipeline:lint`.
  - `tn-exam-lecture-and-practice/SKILL.md`: Updated frontmatter, purpose, boundary, and step 4 to reference `npm run pipeline:lint` and `npm run build`.
  - `tn-exam-query/SKILL.md`: Replaced raw `python3 -m tools.search` and `python3 -m tools.indexer` calls with `npm run pipeline:query` and `npm run pipeline:indexer`.
- **Build status**: PASS (`npm run build` exit code 0)
- **Pending issues**: None

## Quality Status
- **Build/test result**: PASS (all 5 pipeline commands + build passed cleanly)
- **Lint status**: PASS (0 errors)
- **Tests added/modified**: N/A

## Loaded Skills
- None

## Key Decisions Made
- Implemented Explorer 4 remediation plan with 100% fidelity.

## Artifact Index
- `.agents/worker_m2_6/ORIGINAL_REQUEST.md` — Prompt request
- `.agents/worker_m2_6/BRIEFING.md` — Briefing document
- `.agents/worker_m2_6/progress.md` — Progress tracker & liveness heartbeat
- `.agents/worker_m2_6/handoff.md` — Final 5-component handoff report

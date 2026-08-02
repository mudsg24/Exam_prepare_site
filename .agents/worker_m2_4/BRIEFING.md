# BRIEFING — 2026-08-02T22:29:45+08:00

## Mission
Perform Remediation Pass 2 on `package.json` and 7 `tn-exam-*` skills to update pipeline scripts, eliminate residual legacy script paths, clean up `tn-exam-expert` QC steps, ensure `tn-exam-lecture-and-practice` is strictly dispatch-only, clean up duplicate governance rule blocks with concise SSOT references to `AGENTS.md`, and verify frontmatter.

## 🔒 My Identity
- Archetype: Remediation Worker
- Roles: implementer, qa, specialist
- Working directory: /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_4
- Original parent: c19154c1-f35a-4922-8ac1-4f00672b38d3
- Milestone: Remediation Pass 2

## 🔒 Key Constraints
- Follow minimal change principle and zero hallucination rules.
- Do not cheat; genuine implementations only.
- Ensure all 7 skills pass YAML frontmatter checks and legacy script path greps.
- Keep language specifications in mind (plan/briefing in Traditional Chinese + English terms, labels in English).

## Current Parent
- Conversation ID: c19154c1-f35a-4922-8ac1-4f00672b38d3
- Updated: 2026-08-02T22:29:45+08:00

## Task Summary
- **What to build**: Task 1 (package.json pipeline scripts), Task 2 (eliminate residual script paths in 7 skills), Task 3 (remove QC from tn-exam-expert), Task 4 (strictly dispatch-only tn-exam-lecture-and-practice), Task 5 (clean up duplicate governance rule blocks with SSOT references to AGENTS.md), Frontmatter verification, and Handoff report.
- **Success criteria**: 0 matches for legacy scripts in `tn-exam-*`, all pipeline commands updated, skills clean and compliant, handoff report generated, parent notified.

## Key Decisions Made
- Added `pipeline:lint`, `pipeline:ingest`, `pipeline:qc`, `pipeline:query`, `pipeline:tutor`, `pipeline:producer`, `pipeline:expert`, `pipeline:images` in `package.json`.
- Streamlined governance sections in `tn-exam-*` skills to reference `AGENTS.md § Mandatory Question Extraction Governance Rule` as SSOT.
- Retained pure pre-processing boundary in `tn-exam-expert/SKILL.md` (no QC calls or steps).
- Retained strictly dispatch-only structure in `tn-exam-lecture-and-practice/SKILL.md` via `invoke_subagent`.

## Change Tracker
- **Files modified**:
  - `package.json` — Added pipeline:* script targets and aliases.
  - `~/.gemini/config/skills/tn-exam-expert/SKILL.md` — Updated frontmatter, AGENTS.md SSOT reference, pure pre-processing boundary.
  - `~/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md` — Updated frontmatter, AGENTS.md SSOT reference, dispatch-only via invoke_subagent.
  - `~/.gemini/config/skills/tn-exam-prepare/SKILL.md` — Updated frontmatter, AGENTS.md SSOT reference, pipeline:lint validation.
  - `~/.gemini/config/skills/tn-exam-producer/SKILL.md` — Streamlined governance block with AGENTS.md SSOT reference, pipeline:producer / pipeline:lint validation.
  - `~/.gemini/config/skills/tn-exam-qc/SKILL.md` — Updated frontmatter, AGENTS.md SSOT reference, pipeline:qc / pipeline:lint validation.
  - `~/.gemini/config/skills/tn-exam-query/SKILL.md` — Updated frontmatter, AGENTS.md SSOT reference, pipeline:query.
  - `~/.gemini/config/skills/tn-exam-tutor/SKILL.md` — Streamlined governance block with AGENTS.md SSOT reference, pipeline:tutor / pipeline:lint validation.
- **Build status**: PASS (`npm run pipeline:lint`, `npm run build`)
- **Pending issues**: None

## Quality Status
- **Build/test result**: PASS (npm run pipeline:lint, npm run pipeline:tutor, npm run pipeline:producer, npm run pipeline:expert)
- **Lint status**: PASS (0 errors across 103 exam JSONs, 77 tutorial JSONs, 180 asset checks)
- **Tests added/modified**: N/A

## Loaded Skills
- None

## Artifact Index
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_4/ORIGINAL_REQUEST.md` — Original user request log
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_4/BRIEFING.md` — Persistent briefing state
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_4/progress.md` — Progress log
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/worker_m2_4/handoff.md` — Handoff report

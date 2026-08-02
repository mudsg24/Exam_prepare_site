# Project: Refactoring 7 /tn-exam-* Skills (Phase 3)

## Architecture
- Working directory for skills: `/Users/yuan/.gemini/config/skills/`
- Target skills:
  - `tn-exam-prepare`
  - `tn-exam-qc`
  - `tn-exam-expert`
  - `tn-exam-producer`
  - `tn-exam-tutor`
  - `tn-exam-lecture-and-practice`
  - `tn-exam-query`

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Exploration & Audit | Read and audit all 7 SKILL.md files to locate legacy script paths and duplicate rules | None | DONE |
| 2 | Skill Refactoring Implementation | Update package.json & SKILL.md files per Remediation Pass 4 (Facade script cleanup & query wrapping) | M1 | DONE |
| 3 | Verification & Quality Gate | Re-verify package.json scripts, npm run commands, zero facade aliases, zero legacy paths, and forensic integrity | M2 | DONE |

## Interface Contracts & Requirements
- `tn-exam-prepare`: Ingestion entry point. Pure NLP semantic extraction. Trigger `npm run pipeline:ingest`.
- `tn-exam-qc`: Quality Gate. NLM completeness & semantic review. Trigger `npm run pipeline:qc`. Remove duplicate prepare rules.
- `tn-exam-expert`: Pre-processing tool. De-walling & LaTeX/Markdown fix. NO QC calls. Static verification via `npm run pipeline:lint`.
- `tn-exam-producer`: MCQs generation from study notes (pure English). Static verification via `npm run pipeline:lint`.
- `tn-exam-tutor`: Textbook-style lectures generation from study notes. Static verification via `npm run pipeline:lint`.
- `tn-exam-lecture-and-practice`: Pure Orchestrator / Dispatcher. NO content generation inside. Parse user input and call `invoke_subagent` to dispatch `tn-exam-producer` and `tn-exam-tutor`. Trigger `npm run pipeline:lint` and `npm run build`.
- `tn-exam-query`: Semantic search / RAG role. Trigger `npm run pipeline:query` and `npm run pipeline:indexer`. Remove raw python invocations.
- General Cleanup: Remove duplicate governance rules across all 7 skills. All facade script aliases removed from `package.json`. Authentic pipeline scripts declared: `pipeline:lint`, `pipeline:ingest`, `pipeline:qc`, `pipeline:query`, `pipeline:indexer`.

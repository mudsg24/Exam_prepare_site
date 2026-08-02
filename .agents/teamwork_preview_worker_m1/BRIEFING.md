# BRIEFING — 2026-08-02T22:13:36Z

## Mission
Implement Phase 2 Script Modularization (R1, R2, R3) for Exam_prepare_site with zero breaking changes and genuine implementation.

## 🔒 My Identity
- Archetype: implementer
- Roles: implementer, qa, specialist
- Working directory: /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1
- Original parent: 8672ef55-4928-4c5b-ad69-585832245360
- Milestone: Phase 2 Script Modularization

## 🔒 Key Constraints
- Complete genuine implementation without hardcoded test results, facade implementations, or bypassing verification.
- Strictly adhere to Project Layout: project source/test code stays in project directories (`scripts/`, `package.json`, etc.), `.agents/` contains metadata only.
- Minimize edits; re-read files before editing.
- Follow D-017 sync for artifacts: English headings, Traditional Chinese prose + English technical terms.

## Current Parent
- Conversation ID: 8672ef55-4928-4c5b-ad69-585832245360
- Updated: 2026-08-02T22:13:36Z

## Task Summary
- **What to build**: Implement R1 (Directory Setup & File Relocation), R2 (Internal Path Resolution Fixes), and R3 (External Path Updates & Governance).
- **Success criteria**: All relocated scripts resolve paths correctly, `npm run lint:exams`, `npm run test`, `npm run test:py` pass with zero failures, and AGENTS.md governance rules updated.
- **Interface contracts**: `PROJECT.md` / `AGENTS.md`
- **Code layout**: `scripts/pipeline/{lint,ingest,qc,nlm,utils}/`

## Key Decisions Made
- Relocated 11 pipeline scripts into `scripts/pipeline/{lint,ingest,qc,nlm,utils}/` via `git mv`.
- Updated internal paths for moved scripts and external callers.
- Updated `package.json`, `vitest.config.ts`, `AGENTS.md`, and test files in `scripts/__tests__/`.
- Expanded `AGENTS.md` Rule 1 to clarify Red Zone vs Green Zone governance.
- Verified all build, test, and linter commands (`npm run lint:exams`, `npm run test`, `npm run test:py`) with 100% pass rate.

## Artifact Index
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1/ORIGINAL_REQUEST.md` — Original User Request
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1/progress.md` — Liveness Heartbeat
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1/BRIEFING.md` — BRIEFING Index
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1/changes.md` — Detailed Implementation Log
- `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1/handoff.md` — Handoff Report

## Change Tracker
- **Files modified**: 11 moved scripts under `scripts/pipeline/`, `package.json`, `AGENTS.md`, `vitest.config.ts`, 3 test files in `scripts/__tests__/`, 5 caller scripts in `scripts/`.
- **Build status**: PASS (`npm run lint:exams`, `npm run test`, `npm run test:py` all exit code 0).
- **Pending issues**: None.

## Quality Status
- **Build/test result**: 100% PASS (Vitest: 14 passed / 98 tests, Pytest: 2 passed, Linter: 103 exam JSONs + 77 tutorial JSONs + 180 database JSON assets passed).
- **Lint status**: 0 violations.
- **Tests added/modified**: Updated import/sys.path in 3 test files (`lint_exam_json.test.mjs`, `build_image_index.test.mjs`, `test_extract_and_attach_images.py`).

## Loaded Skills
- None

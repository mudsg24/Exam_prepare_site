# Project Plan: Exam_prepare_site Phase 2 Script Modularization

## Architecture
- Target directory: `scripts/pipeline/`
- Subdirectories:
  - `scripts/pipeline/lint/`: `lint_exam_json.mjs`, `lint_tutorial_json.mjs`, `check_assets.mjs`
  - `scripts/pipeline/ingest/`: `ingest_exam.mjs`, `extract_and_attach_images.py`
  - `scripts/pipeline/qc/`: `exam_qc.mjs`, `merge_qc_results.mjs`, `apply_qc_updates.py`
  - `scripts/pipeline/nlm/`: `ask_nlm_for_*.mjs`, `process_nlm_results.py`
  - `scripts/pipeline/utils/`: `build_image_index.mjs`

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Script Migration & Internal Path Resolution | Move scripts into `scripts/pipeline/{lint,ingest,qc,nlm,utils}/` and update internal `__dirname` / `os.path.dirname(__file__)` references | none | IN_PROGRESS |
| 2 | External Path & Config Updates | Update `package.json`, `AGENTS.md`, `scripts/__tests__/`, `vitest.config.ts` | Milestone 1 | PLANNED |
| 3 | Full Pipeline Verification & Integrity Audit | Execute `npm run lint:exams`, `npm run test`, `npm run test:py` and run Forensic Integrity Audit | Milestone 1, 2 | PLANNED |

## Interface & Path Contracts
- Scripts moved 1 level deeper into subdirectories under `scripts/pipeline/`.
- Relative imports from scripts to root/public must add `../` or calculate root correctly (`path.join(__dirname, '../../public/server-data')` etc.).
- External scripts/tests importing pipeline scripts must use updated relative paths.
- `package.json` scripts (`lint:exams`, `check:assets`, `build`, `build:images`) updated to point to `scripts/pipeline/lint/...`.
- `AGENTS.md` rules 10 and 11 updated to point to `scripts/pipeline/lint/lint_exam_json.mjs` and `scripts/pipeline/lint/check_assets.mjs`.

## Code Layout
- `scripts/pipeline/lint/`
- `scripts/pipeline/ingest/`
- `scripts/pipeline/qc/`
- `scripts/pipeline/nlm/`
- `scripts/pipeline/utils/`
- `scripts/__tests__/`

## 2026-08-02T14:12:13Z

Use high reasoning effort for deep thinking and analysis.

Identity: Worker (teamwork_preview_worker_m1)
Working directory: /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Mission: Implement Phase 2 Script Modularization (R1, R2, R3) for Exam_prepare_site.

Read the handoff reports from the Explorers for complete context:
- /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_explorer_m1_1/handoff.md
- /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_explorer_m1_2/handoff.md
- /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_explorer_m1_3/handoff.md

Step-by-Step Implementation Instructions:

1. R1 — Directory Setup & File Relocation:
   Create the following directories and move the scripts (do NOT modify core logic):
   - scripts/pipeline/lint/: lint_exam_json.mjs, lint_tutorial_json.mjs, check_assets.mjs
   - scripts/pipeline/ingest/: ingest_exam.mjs, extract_and_attach_images.py
   - scripts/pipeline/qc/: exam_qc.mjs, merge_qc_results.mjs, apply_qc_updates.py
   - scripts/pipeline/nlm/: ask_nlm_for_2026.mjs, ask_nlm_for_renal_transplant.mjs, process_nlm_results.py
   - scripts/pipeline/utils/: build_image_index.mjs

2. R2 — Internal Path Resolution Fixes:
   Update relative paths in relocated scripts so they resolve relative to root/public properly:
   - scripts/pipeline/lint/lint_exam_json.mjs:
     Line 8: '../public/server-data' -> '../../../public/server-data'
     Line 208: '../public' -> '../../../public'
   - scripts/pipeline/lint/lint_tutorial_json.mjs:
     Line 8: '../public' -> '../../../public'
   - scripts/pipeline/lint/check_assets.mjs:
     Line 8: '../public' -> '../../../public'
   - scripts/pipeline/nlm/ask_nlm_for_2026.mjs:
     Line 4: './ingest_exam.mjs' -> '../ingest/ingest_exam.mjs'
   - scripts/pipeline/nlm/ask_nlm_for_renal_transplant.mjs:
     Line 4: './ingest_exam.mjs' -> '../ingest/ingest_exam.mjs'

3. R3 — External Path Updates & Governance:
   - package.json: Update scripts (lint:exams, check:assets, build, build:images) to point to scripts/pipeline/{lint,utils}/...
   - AGENTS.md:
     - Update Rule 10, Rule 11, Rule 12 references to point to scripts/pipeline/lint/lint_exam_json.mjs and scripts/pipeline/lint/check_assets.mjs.
     - Under Rule 1 (ZERO MECHANICAL EXTRACTION MEMORY GUARD / 機械切分絕對警示鐵律), expand the rule text to explicitly define the "Red Zone" (Regex and mechanical string manipulation on question text/stem/options/explanations is strictly banned) vs "Green Zone" (JSON schema linters, asset checkers, and pipeline status scripts under scripts/pipeline/ is valid system tools).
   - vitest.config.ts: Update coverage.include array to scripts/pipeline/lint/lint_exam_json.mjs and scripts/pipeline/utils/build_image_index.mjs.
   - scripts/__tests__/:
     - lint_exam_json.test.mjs: Update import '../lint_exam_json.mjs' -> '../pipeline/lint/lint_exam_json.mjs'.
     - build_image_index.test.mjs: Update import '../build_image_index.mjs' -> '../pipeline/utils/build_image_index.mjs'.
     - test_extract_and_attach_images.py: Update sys.path to include os.path.abspath(os.path.join(..., '..', 'pipeline', 'ingest')).
   - Unmigrated scripts in scripts/:
     - scripts/reask_anomalous.mjs: Update './ingest_exam.mjs' -> './pipeline/ingest/ingest_exam.mjs'.
     - scripts/repair_nlm_dual_asking.mjs: Update './ingest_exam.mjs' -> './pipeline/ingest/ingest_exam.mjs'.
     - scripts/export_stage1_anomalous.mjs: Update './exam_qc.mjs' -> './pipeline/qc/exam_qc.mjs'.
     - scripts/prepare_stage2_batch.mjs: Update './exam_qc.mjs' -> './pipeline/qc/exam_qc.mjs'.
     - scripts/update_stage1_results.mjs: Update './exam_qc.mjs' -> './pipeline/qc/exam_qc.mjs'.

4. Verification & Testing:
   Run all build/test commands and record the outputs:
   - npm run lint:exams
   - npm run test
   - npm run test:py

5. Reporting:
   Document your changes and test results in /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1/changes.md and /Users/yuan/Projects/Exam/Exam_prepare_site/.agents/teamwork_preview_worker_m1/handoff.md. Update progress.md with your heartbeat. Send a message to parent when done.

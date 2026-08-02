# Handoff Report — Worker M2_1 (Group A Skills Refactoring)

## 1. Observation

- **Target Files**:
  - `/Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md`
  - `/Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md`
  - `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json`

- **Pre-Refactoring State**:
  - `tn-exam-prepare/SKILL.md`: Contained legacy script references (e.g. `node scripts/lint_exam_json.mjs`) and duplicated detailed governance rules that are standardly governed in `AGENTS.md`.
  - `tn-exam-qc/SKILL.md`: Contained legacy script references (`scripts/exam_qc.mjs`, `applyQcToQuestion` direct script references) and duplicate prepare/ingestion rules.
  - `package.json`: Lacked explicit `pipeline:ingest` and `pipeline:qc` script entries under `"scripts"`.

- **Post-Refactoring Commands and Execution Output**:
  - Python YAML Parser Check:
    `PASS: /Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md -> name=tn-exam-prepare, user-invocable=True`
    `PASS: /Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md -> name=tn-exam-qc, user-invocable=True`
  - Grep check for `scripts/`:
    `grep_search` for `scripts/` in `tn-exam-prepare/SKILL.md` returned `0` matches.
    `grep_search` for `scripts/` in `tn-exam-qc/SKILL.md` returned `0` matches.
  - Workspace Build & Asset Lint (`npm run build`):
    `✅ Exam JSON Lint Passed! All manifest schemas and exam files are clean.`
    `✅ Tutorial Linter Passed! All tutorial diagram schemas and image paths are valid.`
    `✅ Asset Verification Passed! All referenced image assets exist on disk.`
    `built in 2.88s`

## 2. Logic Chain

1. **Pure Ingestion Entry Point Refactoring (`tn-exam-prepare`)**:
   - Replaced legacy script calls (`scripts/ingest_exam.mjs`, `scripts/extract_and_attach_images.py`, `scripts/build_image_index.mjs`) with `npm run pipeline:ingest`.
   - Explicitly aligned boundary governance with `AGENTS.md` 12 governance rules, eliminating redundant rule duplications while preserving prepare-specific constraints (MCQ qualification, processed paper skipping, subagent batch size 5, confirmation gate, no ground truth to NLM).
   - Structured execution algorithm to focus on subagent NLP semantic extraction followed by `npm run pipeline:ingest` execution.

2. **Authoritative Quality Gate Refactoring (`tn-exam-qc`)**:
   - Replaced legacy script calls (`scripts/exam_qc.mjs`, `scripts/apply_qc_updates.py`, `scripts/merge_qc_results.mjs`) with `npm run pipeline:qc`.
   - Removed prepare/ingestion specific logic (such as file discovery, pre-screening, and paper summary confirmation) to maintain strict separation of concerns.
   - Refactored algorithm to focus on Stage 1 (technical failure scanning via `npm run pipeline:qc -- --scan-only` & `/tn-nlm-asking-mcqs` re-ask) and Stage 2 (subagent dual semantic verification and persisting flags via `npm run pipeline:qc`).

3. **Workspace Script Enablement (`package.json`)**:
   - Added `"pipeline:ingest": "node scripts/pipeline/ingest/ingest_exam.mjs"` and `"pipeline:qc": "node scripts/pipeline/qc/exam_qc.mjs"` to `package.json` to ensure npm CLI executions (`npm run pipeline:ingest` and `npm run pipeline:qc`) resolve properly.

## 3. Caveats

- `npm run pipeline:ingest` and `npm run pipeline:qc` pass flags (such as `--force`, `--dry-run`, `--scan-only`, `--paper <id>`, `--clean`) to their underlying Node.js CLI entry points in `scripts/pipeline/`.
- No further caveats; all YAML frontmatters and npm build commands pass cleanly.

## 4. Conclusion

Group A skills (`tn-exam-prepare` and `tn-exam-qc`) have been fully refactored to:
1. Act as pure Ingestion entry point (`tn-exam-prepare`) and authoritative Quality Gate (`tn-exam-qc`) respectively.
2. Rely strictly on `npm run pipeline:ingest` and `npm run pipeline:qc` without any hardcoded `scripts/...` paths.
3. Fully validate YAML frontmatter parsing and pass full workspace build/asset integrity checks (`npm run build`).

## 5. Verification Method

To independently verify:
1. **YAML Frontmatter Check**:
   ```bash
   python3 -c "import yaml, re; print(yaml.safe_load(re.match(r'^---\n(.*?)\n---', open('/Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md').read(), re.DOTALL).group(1)))"
   python3 -c "import yaml, re; print(yaml.safe_load(re.match(r'^---\n(.*?)\n---', open('/Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md').read(), re.DOTALL).group(1)))"
   ```
2. **Zero `scripts/` Path Check**:
   ```bash
   grep "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md
   grep "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md
   # Both commands must yield 0 matches.
   ```
3. **Workspace Build Verification**:
   ```bash
   cd /Users/yuan/Projects/Exam/Exam_prepare_site
   npm run build
   npm run pipeline:ingest -- --dry-run /Users/yuan/Projects/Exam/Exam_prepare_database/Processed/2025_成大
   npm run pipeline:qc -- --scan-only
   ```

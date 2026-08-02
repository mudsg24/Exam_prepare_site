# Progress Log

Last visited: 2026-08-02T22:29:40+08:00

- [x] Initialized workspace and briefing state.
- [x] Task 1: Inspect `scripts/pipeline/` and update `package.json` with `pipeline:*` npm scripts (`pipeline:lint`, `pipeline:ingest`, `pipeline:qc`, `pipeline:query`, `pipeline:tutor`, `pipeline:producer`, `pipeline:expert`, `pipeline:images`).
- [x] Task 2: Fix residual hardcoded `scripts/` paths across all 7 skills (0 matches for `scripts/` legacy paths in `~/.gemini/config/skills/tn-exam-*`).
- [x] Task 3: Remove ALL QC calls and workflow steps from `tn-exam-expert/SKILL.md` (pure pre-processing tool for de-walling and LaTeX fix).
- [x] Task 4: Refactor `tn-exam-lecture-and-practice/SKILL.md` to be strictly dispatch-only via `invoke_subagent`.
- [x] Task 5: Clean up duplicate governance rule blocks in 7 skills to reference `AGENTS.md` SSOT rules.
- [x] Verification: YAML frontmatter check (7/7 valid) & legacy path grep check (0 matches).
- [x] Handoff & Notification: Write `handoff.md` and message parent.

## 2026-08-02T14:28:20Z
<USER_REQUEST>
You are Reviewer 4 for Milestone 3 Iteration 3 Quality Gate of Phase 3 skill refactoring.
Working directory: `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/reviewer_m3_4/`.

Tasks:
1. Inspect `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` and verify that all 7 functional `pipeline:*` scripts exist in `scripts`:
   - `pipeline:ingest`
   - `pipeline:qc`
   - `pipeline:expert`
   - `pipeline:producer`
   - `pipeline:tutor`
   - `pipeline:lecture-and-practice` (or `pipeline:lecture`)
   - `pipeline:query`
2. Inspect all 7 refactored `SKILL.md` files in `/Users/yuan/.gemini/config/skills/`:
   - `tn-exam-prepare/SKILL.md`
   - `tn-exam-qc/SKILL.md`
   - `tn-exam-expert/SKILL.md`
   - `tn-exam-producer/SKILL.md`
   - `tn-exam-tutor/SKILL.md`
   - `tn-exam-lecture-and-practice/SKILL.md`
   - `tn-exam-query/SKILL.md`
3. Verify that:
   - ZERO legacy `scripts/` paths (e.g. `scripts/pipeline/...`) remain in any of the 7 `SKILL.md` files.
   - `tn-exam-expert/SKILL.md` contains ZERO QC calls or NLM dual asking steps.
   - `tn-exam-lecture-and-practice/SKILL.md` is 100% dispatch-only (parses input, dispatches `tn-exam-producer` and `tn-exam-tutor` via `invoke_subagent`, with NO embedded topic generation or MCQ writing inside).
   - Language formatting complies with Tonks standards (繁體中文敘述 + 英文專有名詞, English Headings).
4. Update `.agents/reviewer_m3_4/progress.md`, write detailed handoff report to `.agents/reviewer_m3_4/handoff.md`, and send a summary message to parent (`c19154c1-f35a-4922-8ac1-4f00672b38d3`).
</USER_REQUEST>

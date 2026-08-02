# Milestone 3 Verification & Quality Review Report

**Reviewer**: Reviewer 1 (Milestone 3)
**Target**: 7 `/tn-exam-*` skills in `/Users/yuan/.gemini/config/skills/`
**Date**: 2026-08-02
**Verdict**: **REQUEST_CHANGES**

---

## 1. Observation

Direct evidence collected via file inspection and grep search:

1. **YAML Frontmatter Header Audit**:
   - `/Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md:1-5`: Valid YAML header (`name: tn-exam-prepare`).
   - `/Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md:1-5`: Valid YAML header (`name: tn-exam-qc`).
   - `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md:1-5`: Valid YAML header (`name: tn-exam-expert`).
   - `/Users/yuan/.gemini/config/skills/tn-exam-producer/SKILL.md:1-5`: Valid YAML header (`name: tn-exam-producer`).
   - `/Users/yuan/.gemini/config/skills/tn-exam-tutor/SKILL.md:1-5`: Valid YAML header (`name: tn-exam-tutor`).
   - `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md:1-5`: Valid YAML header (`name: tn-exam-lecture-and-practice`).
   - `/Users/yuan/.gemini/config/skills/tn-exam-query/SKILL.md:1-5`: Valid YAML header (`name: tn-exam-query`).

2. **Hardcoded `scripts/` Paths (`grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*`)**:
   - `tn-exam-expert/SKILL.md:16`: `執行 node scripts/lint_exam_json.mjs`
   - `tn-exam-expert/SKILL.md:84`: `執行 run_command: node scripts/lint_exam_json.mjs`
   - `tn-exam-lecture-and-practice/SKILL.md:103`: `靜態 Linter scripts/lint_exam_json.mjs 會自動...`
   - `tn-exam-lecture-and-practice/SKILL.md:158`: `執行 node scripts/lint_exam_json.mjs`
   - `tn-exam-prepare/SKILL.md:149`: `包含 node scripts/lint_exam_json.mjs`
   - `tn-exam-producer/SKILL.md:118`: `包含 node scripts/lint_exam_json.mjs`
   - `tn-exam-qc/SKILL.md:78`: `腳本 (scripts/exam_qc.mjs) 僅作為...`

3. **`tn-exam-lecture-and-practice/SKILL.md` Dispatch Logic**:
   - Lines 116-127 (Phase 2): Contains embedded generation prompts for `Lecture Author Subagent` (language rules, schema requirements, image generation, trap analysis).
   - Lines 122-127 (Phase 3): Contains embedded generation prompts for `MCQ Producer Subagent` (stem language rules, option schema, option shuffling, explanation formatting).
   - It re-defines content generation rules inside its own file rather than delegating strictly via dispatching `/tn-exam-tutor` and `/tn-exam-producer`.

4. **`tn-exam-expert/SKILL.md` QC Contamination**:
   - Line 3: Description includes `/tn-exam-qc 品質過濾`.
   - Line 14: Purpose includes `Phase 3: 執行 /tn-exam-qc 品管 (NLM Quality Control)`.
   - Lines 74-78: Step 4 defines `Phase 3 - Execute /tn-exam-qc Pipeline`, explicitly calling `/tn-exam-qc <target_paper>`.
   - Line 93: Output contract includes `Phase 3: /tn-exam-qc 提問補齊與校對結案題數`.

5. **Governance Rules Duplication Across Skills**:
   - Full multi-paragraph governance rule blocks (`STRICT LANGUAGE CONTRACT FOR SUBAGENTS & QC`, `LIFECYCLE ABSOLUTE BAN ON REGEX & SCRIPTS`, `SYNTHETIC CLASSIFICATION HEADERS ABSOLUTE BAN`, `ABSOLUTE BAN ON REGEX NLM OPTION EXTRACTION`, `DATABASE & MANIFEST JSON SCHEMA STRICT CONTRACT`) are copied verbatim in full length across `tn-exam-prepare`, `tn-exam-producer`, `tn-exam-lecture-and-practice`, and `tn-exam-qc`.

---

## 2. Logic Chain

1. **Obs 1 $\rightarrow$ Step 1 Verification**: Frontmatter headers in all 7 files start with `---`, contain required YAML properties (`name`, `description`, `user-invocable`), and end with `---`. This criterion is satisfied.
2. **Obs 2 $\rightarrow$ Step 2 Verification**: The prompt explicitly requires `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*` to return NO hardcoded `scripts/...` paths. Grep output revealed 7 hardcoded references (`scripts/lint_exam_json.mjs` and `scripts/exam_qc.mjs`) across 5 skill files (`tn-exam-expert`, `tn-exam-lecture-and-practice`, `tn-exam-prepare`, `tn-exam-producer`, `tn-exam-qc`). Therefore, Step 2 fails.
3. **Obs 3 $\rightarrow$ Step 3 Verification**: `tn-exam-lecture-and-practice` is required to be strictly dispatch-only via `invoke_subagent` without internal content generation prompts. Observation 3 proves that lines 116-127 embed internal generation prompt instructions for lecture authoring and question generation instead of delegating dispatch to `tn-exam-tutor` and `tn-exam-producer`. Therefore, Step 3 fails.
4. **Obs 4 $\rightarrow$ Step 4 Verification**: `tn-exam-expert` is required to contain NO QC calls or workflow steps. Observation 4 proves that `tn-exam-expert/SKILL.md` explicitly includes Phase 3 (`Execute /tn-exam-qc Pipeline`), invokes `/tn-exam-qc <target_paper>`, and tracks QC results. Therefore, Step 4 fails.
5. **Obs 5 $\rightarrow$ Step 5 Verification**: Governance rules were required to be cleaned up and de-duplicated. Observation 5 shows massive verbatim duplication of 5+ governance rule sections across 4 skills instead of referencing `AGENTS.md` as the single source of truth. Therefore, Step 5 fails.

---

## 3. Findings & Design Judgment

### Review Summary
**Verdict**: **REQUEST_CHANGES**

### Findings

#### [Major] Finding 1: Hardcoded Legacy `scripts/` Paths Across 5 Skills
- **Where**: `tn-exam-expert/SKILL.md:16,84`, `tn-exam-lecture-and-practice/SKILL.md:103,158`, `tn-exam-prepare/SKILL.md:149`, `tn-exam-producer/SKILL.md:118`, `tn-exam-qc/SKILL.md:78`.
- **Why**: Hardcoded stale `scripts/` paths (such as `scripts/lint_exam_json.mjs` and `scripts/exam_qc.mjs`) violate project structure (where linter scripts reside in `scripts/pipeline/lint/`) and break the grep prohibition requirement.
- **Suggestion**: Replace hardcoded `node scripts/...` invocations with `npm run build` or canonical lint runner references, matching `AGENTS.md`.

#### [Major] Finding 2: `tn-exam-expert` Retains `/tn-exam-qc` Calls and Workflow Steps
- **Where**: `tn-exam-expert/SKILL.md:3,14,74-78,93`.
- **Why**: `tn-exam-expert` is intended solely as a pre-practice text formatting, de-walling, anti-strikethrough, and readability restructuring skill. Retaining Phase 3 (`/tn-exam-qc`) creates workflow coupling and violates single-responsibility boundary.
- **Suggestion**: Remove Phase 3 (`Execute /tn-exam-qc Pipeline`) from `tn-exam-expert/SKILL.md` completely. QC belongs exclusively to `tn-exam-qc`.

#### [Major] Finding 3: `tn-exam-lecture-and-practice` Contains Embedded Content Generation Prompts
- **Where**: `tn-exam-lecture-and-practice/SKILL.md:116-127`.
- **Why**: `tn-exam-lecture-and-practice` should act purely as an orchestrator gateway that dispatches subagents to execute `tn-exam-tutor` and `tn-exam-producer`. Inlining generation prompts duplicates implementation details and creates maintenance drift.
- **Suggestion**: Refactor `tn-exam-lecture-and-practice/SKILL.md` to be strictly dispatch-only via `invoke_subagent`, referencing `tn-exam-tutor` and `tn-exam-producer` standards for generation logic.

#### [Major] Finding 4: Massive Duplicate Governance Rule Blocks Across Skills
- **Where**: `tn-exam-prepare/SKILL.md:25-84`, `tn-exam-producer/SKILL.md:28-83`, `tn-exam-lecture-and-practice/SKILL.md:30-104`, `tn-exam-qc/SKILL.md:30-97`.
- **Why**: Duplicating 50+ lines of identical governance rules across 4 skill files bloats skill definitions and leads to inconsistent rules when updates occur.
- **Suggestion**: Clean up redundant governance rule blocks in individual skills and cross-reference `AGENTS.md` (Mandatory Governance Rules) as the Single Source of Truth, keeping only skill-specific boundary constraints.

---

## 4. Design Judgment

From an architectural standpoint, skills in `.gemini/config/skills/` serve as entrypoints and instructions for LLM agent execution. Having duplicated 100-line governance blocks in every skill definition increases prompt token overhead and creates risk of rule fragmentation. The architecture demands that project-wide rules (such as 0% Regex, 100% Pure English medical terms, JSON schemas, NLM asking rules) reside centrally in `AGENTS.md`, while skills maintain concise, action-oriented execution algorithms.

Furthermore, separating concern between text formatting (`tn-exam-expert`), quality control (`tn-exam-qc`), generation (`tn-exam-producer`/`tn-exam-tutor`), and orchestration (`tn-exam-lecture-and-practice`) is essential for reliable agent pipeline execution. Coupling `tn-exam-qc` into `tn-exam-expert` creates circular dependencies and redundant processing.

---

## 5. Verified Claims & Coverage Gaps

### Verified Claims
1. **YAML Frontmatter**: Verified all 7 skills start with `---` and contain `name`, `description`, `user-invocable` $\rightarrow$ PASS.
2. **No Hardcoded `scripts/`**: Executed `grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*` $\rightarrow$ FAIL (7 matches in 5 files).
3. **Dispatch-Only `tn-exam-lecture-and-practice`**: Verified file contents $\rightarrow$ FAIL (contains embedded generation prompts).
4. **No QC in `tn-exam-expert`**: Verified file contents $\rightarrow$ FAIL (contains Phase 3 QC workflow steps and `/tn-exam-qc` calls).
5. **De-duplicated Governance Rules**: Verified rule sections across skills $\rightarrow$ FAIL (heavy duplication persists).

### Coverage Gaps
- No coverage gaps. All 7 skills and all 5 verification dimensions were completely inspected.

---

## 6. Caveats

No caveats. Direct inspection of all target skill files was performed without restriction.

---

## 7. Conclusion

Phase 3 refactoring of the 7 `/tn-exam-*` skills does **not** pass quality gate verification.
The verdict is **REQUEST_CHANGES**.

Recommended Actions for Implementer:
1. Remove all hardcoded `scripts/...` paths from the 5 affected skill files.
2. Strip Phase 3 (`/tn-exam-qc` execution) out of `tn-exam-expert/SKILL.md`.
3. Refactor `tn-exam-lecture-and-practice/SKILL.md` to be strictly dispatch-only.
4. Clean up redundant governance rule duplications across `tn-exam-prepare`, `tn-exam-producer`, `tn-exam-lecture-and-practice`, and `tn-exam-qc`, referencing `AGENTS.md`.

---

## 8. Verification Method

To independently verify these findings:

```bash
# Check 1: Frontmatter check (all should have ---)
head -n 5 ~/.gemini/config/skills/tn-exam-*/SKILL.md

# Check 2: Hardcoded scripts check (should return 0 lines)
grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*

# Check 3: Check for /tn-exam-qc calls inside tn-exam-expert (should return 0 lines)
grep -rn "tn-exam-qc" ~/.gemini/config/skills/tn-exam-expert/SKILL.md

# Check 4: Check tn-exam-lecture-and-practice for dispatch-only compliance
cat ~/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md
```

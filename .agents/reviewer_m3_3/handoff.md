# Milestone 3 Iteration 2 Verification Report — 7 `/tn-exam-*` Skills

## Review Summary

**Verdict**: **REQUEST_CHANGES**

**Primary Rationale**: 
Independent re-verification of all 7 `/tn-exam-*` skills confirmed that YAML headers, legacy path elimination, pure dispatcher architecture (`tn-exam-lecture-and-practice`), pre-processing isolation (`tn-exam-expert`), and governance rule deduplication all meet standards. However, a **Major/Critical finding** was detected in script configuration alignment: `package.json` only contains `pipeline:ingest`, `pipeline:qc`, and `pipeline:query`, but the SKILL.md files instruct users and agents to execute `npm run pipeline:producer`, `npm run pipeline:tutor`, `npm run pipeline:expert`, and `npm run pipeline:lint`. These missing scripts will cause runtime execution failures (`npm ERR! missing script`) when those skills are invoked.

---

## 1. Observation

### Observation 1.1: YAML Frontmatter Header Verification
All 7 `SKILL.md` files in `/Users/yuan/.gemini/config/skills/` feature valid YAML frontmatter delimiters (`---`) containing `name`, `description`, and `user-invocable: true`:
- `tn-exam-prepare/SKILL.md`: Lines 1-5
  ```yaml
  ---
  name: tn-exam-prepare
  description: TSN 腎臟專科考題處理與匯入門面 Skill...
  user-invocable: true
  ---
  ```
- `tn-exam-qc/SKILL.md`: Lines 1-5
  ```yaml
  ---
  name: tn-exam-qc
  description: 專責 TSN 考題品質控制與解答爭議稽核 Skill...
  user-invocable: true
  ---
  ```
- `tn-exam-expert/SKILL.md`: Lines 1-5
  ```yaml
  ---
  name: tn-exam-expert
  description: "考前專責試卷文字牆解牆 (De-Walling)..."
  user-invocable: true
  ---
  ```
- `tn-exam-producer/SKILL.md`: Lines 1-5
  ```yaml
  ---
  name: tn-exam-producer
  description: TSN 腎臟專科考訊重點轉化與純英文練習選擇題...
  user-invocable: true
  ---
  ```
- `tn-exam-tutor/SKILL.md`: Lines 1-5
  ```yaml
  ---
  name: tn-exam-tutor
  description: TSN 腎臟專科考訊重點轉化為教科書等級主題式...
  user-invocable: true
  ---
  ```
- `tn-exam-lecture-and-practice/SKILL.md`: Lines 1-5
  ```yaml
  ---
  name: tn-exam-lecture-and-practice
  description: TSN 腎臟專科考點整合之純 Orchestrator / Dispatcher...
  user-invocable: true
  ---
  ```
- `tn-exam-query/SKILL.md`: Lines 1-5
  ```yaml
  ---
  name: tn-exam-query
  description: 使用腎臟科考試資料庫的語意搜尋系統...
  user-invocable: true
  ---
  ```

### Observation 1.2: Legacy `scripts/` Path Search Command
Executed shell command:
`grep -r "scripts/" ~/.gemini/config/skills/tn-exam-* || echo "NO_MATCHES_FOUND"`
Result: `NO_MATCHES_FOUND`.
No legacy `scripts/...` relative paths remain inside any of the 7 `/tn-exam-*` skills.

### Observation 1.3: `tn-exam-lecture-and-practice/SKILL.md` Dispatch-Only Structure
Inspected `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md`:
- Purpose (Lines 11-14): Declares "純 Orchestrator / Dispatcher 門面 (Pure Orchestrator / Dispatcher ONLY)".
- Boundary (Lines 26-28):
  ```markdown
  - **PURE ORCHESTRATOR / DISPATCHER MANDATE (純調度與派發鐵律)**:
    - 本 Skill 絕對不得在主 Session 內直接撰寫、生成或編輯講堂段落、題目內文、選項或 NLM 解析。
    - 所有內容生成任務必須且只能透過 invoke_subagent 委派給 tn-exam-tutor 與 tn-exam-producer 完成。
  ```
- Step 2 & Step 3 (Lines 42-50): Explicitly delegates generation to `tn-exam-tutor` and `tn-exam-producer` via `invoke_subagent`.
- 0 internal content generation prompt templates are present.

### Observation 1.4: `tn-exam-expert/SKILL.md` Pre-processing Isolation
Inspected `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md`:
- Line 16: `**注意：本 Skill 為純 Pre-processing 工具，不進行任何 QC 品管、不呼叫 /tn-exam-qc、亦不處理 NLM 回答可讀性。**`
- Line 44-45: `- **NO QC & NO NLM WORKFLOW CALLS (絕不呼叫 QC 與 NLM 工作流)**: 本 Skill 嚴禁呼叫 /tn-exam-qc 或執行任何 QC 品管步驟。`
- Execution Algorithm steps (Lines 49-65): Covers Step 1 (Resolve Target Paper), Step 2 (Pre-processing Execution & Stem De-Walling via `npm run pipeline:expert`), and Step 3 (Automated Static Linter Clearance via `npm run pipeline:lint`). 0 QC calls or workflow steps exist.

### Observation 1.5: Script Invocations vs `package.json`
Inspected `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` lines 6-20:
```json
  "scripts": {
    "dev": "vite",
    "lint:exams": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs",
    "check:assets": "node scripts/pipeline/lint/check_assets.mjs",
    "build": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs && tsc && vite build",
    "preview": "vite preview",
    "build:images": "node scripts/pipeline/utils/build_image_index.mjs",
    "pipeline:ingest": "node scripts/pipeline/ingest/ingest_exam.mjs",
    "pipeline:qc": "node scripts/pipeline/qc/exam_qc.mjs",
    "pipeline:query": "python3 -m tools.search",
    "test": "vitest run",
    "test:coverage": "vitest run --coverage",
    "test:py": "pytest --cov=scripts scripts/__tests__/",
    "prepare": "husky"
  }
```
Comparison of script references in SKILL.md vs `package.json`:
- `pipeline:ingest`: present in `package.json` (`node scripts/pipeline/ingest/ingest_exam.mjs`) -> MATCH
- `pipeline:qc`: present in `package.json` (`node scripts/pipeline/qc/exam_qc.mjs`) -> MATCH
- `pipeline:query`: present in `package.json` (`python3 -m tools.search`) -> MATCH
- `pipeline:producer`: referenced in `tn-exam-producer` & `tn-exam-lecture-and-practice` -> **MISSING IN package.json**
- `pipeline:tutor`: referenced in `tn-exam-tutor` & `tn-exam-lecture-and-practice` -> **MISSING IN package.json**
- `pipeline:expert`: referenced in `tn-exam-expert` -> **MISSING IN package.json**
- `pipeline:lint`: referenced in `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-lecture-and-practice` -> **MISSING IN package.json** (Note: `package.json` has `"lint:exams"` instead).

### Observation 1.6: Governance Rule Deduplication
Checked all 7 `SKILL.md` files:
- General 12 governance rules are centralized in `AGENTS.md`.
- Skills reference `AGENTS.md` (e.g. `tn-exam-prepare` line 23, `tn-exam-qc` line 28) and focus on skill-specific domain boundaries.
- No redundant, multi-page verbatim copies of generic governance rules exist across skills.

---

## 2. Logic Chain

1. **Frontmatter Verification**: By inspecting lines 1-5 of all 7 `SKILL.md` files, each file starts with valid YAML delimited by `---` containing required metadata (`name`, `description`, `user-invocable: true`). Therefore, Check 1 passes.
2. **Path Verification**: By running `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*`, 0 matches were found. Therefore, Check 2 passes.
3. **Dispatcher Architecture**: In `tn-exam-lecture-and-practice/SKILL.md`, the Purpose and Boundary sections state it is dispatch-only and strictly uses `invoke_subagent` to delegate to `tn-exam-tutor` and `tn-exam-producer`. No prompt generation text exists in the skill. Therefore, Check 3 passes.
4. **Pre-processing Isolation**: In `tn-exam-expert/SKILL.md`, the boundary explicitly forbids calling `/tn-exam-qc` or executing QC steps, and the algorithm steps perform only text de-walling and formatting. Therefore, Check 4 passes.
5. **Script Alignment Analysis**: The skills `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-expert`, and `tn-exam-lecture-and-practice` explicitly instruct running `npm run pipeline:producer`, `npm run pipeline:tutor`, `npm run pipeline:expert`, and `npm run pipeline:lint`. However, inspecting `package.json` reveals that only `pipeline:ingest`, `pipeline:qc`, and `pipeline:query` are defined under `"scripts"`. Executing the missing script commands will result in `npm ERR! missing script`. Therefore, Check 5 fails and requires changes.
6. **Governance Deduplication**: Single source of truth for the 12 governance rules is maintained in `AGENTS.md`, and all skills reference `AGENTS.md` without duplicating redundant blocks. Therefore, Check 6 passes.

---

## 3. Findings

### [Major] Finding 1: Missing `pipeline:*` Scripts in `package.json`
- **What**: `package.json` is missing 4 `pipeline:*` script entries (`pipeline:producer`, `pipeline:tutor`, `pipeline:expert`, `pipeline:lint`) that are referenced throughout the execution algorithms and output contracts of `tn-exam-producer`, `tn-exam-tutor`, `tn-exam-expert`, and `tn-exam-lecture-and-practice`.
- **Where**: `package.json` (lines 6-20) vs SKILL.md files:
  - `tn-exam-producer/SKILL.md`: lines 92, 118, 127 (`npm run pipeline:producer`, `npm run pipeline:lint`)
  - `tn-exam-tutor/SKILL.md`: lines 13, 85, 93 (`npm run pipeline:tutor`, `npm run pipeline:lint`)
  - `tn-exam-expert/SKILL.md`: lines 14, 54, 63 (`npm run pipeline:expert`, `npm run pipeline:lint`)
  - `tn-exam-lecture-and-practice/SKILL.md`: lines 16, 34, 53, 54 (`npm run pipeline:tutor`, `npm run pipeline:producer`, `npm run pipeline:lint`)
- **Why**: When an agent or user attempts to execute `npm run pipeline:producer`, `npm run pipeline:tutor`, `npm run pipeline:expert`, or `npm run pipeline:lint` during skill workflow execution, `npm` will exit with code 1 (`npm ERR! missing script`).
- **Suggestion**: Update `package.json` to include the missing scripts, mapping `pipeline:lint` to `"node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs"` (or aliasing `pipeline:lint` to `npm run lint:exams`), and adding placeholders/entrypoints for `pipeline:producer`, `pipeline:tutor`, and `pipeline:expert` (or updating SKILL.md specifications if specific script commands should be called).

---

## 4. Verified Claims

- Every `SKILL.md` has valid YAML frontmatter header → verified via direct file inspection → **PASS**
- `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*` returns NO legacy `scripts/...` paths → verified via CLI grep search → **PASS**
- `tn-exam-lecture-and-practice/SKILL.md` is strictly dispatch-only via `invoke_subagent` and contains no internal content generation prompts → verified via full file inspection → **PASS**
- `tn-exam-expert` contains NO QC calls or workflow steps → verified via full file inspection & pattern search → **PASS**
- Duplicate governance rules cleaned up across all 7 skills → verified via comparison with `AGENTS.md` → **PASS**
- All script invocations use `npm run pipeline:*` format and match `package.json` → verified via script comparison → **FAIL (4 missing scripts in package.json)**

---

## 5. Coverage Gaps

- No coverage gaps. All 7 skills and `package.json` were fully inspected and verified.

---

## 6. Unverified Items

- No unverified items.

---

## 7. Design Judgment

From an architectural standpoint, centralizing all skill scripts behind standard `npm run pipeline:*` targets in `package.json` is a good design practice because it decouples skill prompt logic from underlying script implementations. However, maintaining strict parity between skill instructions and `package.json` definitions is essential. Adding the missing script aliases (`pipeline:lint`, `pipeline:producer`, `pipeline:tutor`, `pipeline:expert`) to `package.json` will ensure that all 7 skills are 100% executable without runtime script missing errors.

---

## 8. Caveats

- No caveats.

---

## 9. Conclusion

The Phase 3 refactoring of the 7 `/tn-exam-*` skills is well-structured and complies with frontmatter, dispatcher separation, pre-processing boundaries, and governance deduplication rules. However, because `package.json` lacks matching script definitions for `pipeline:producer`, `pipeline:tutor`, `pipeline:expert`, and `pipeline:lint`, the final verdict is **REQUEST_CHANGES**. Once `package.json` is updated to include these script mappings, the quality gate can be fully approved.

---

## 10. Verification Method

To independently verify this finding:
1. Run `grep -E "pipeline:(producer|tutor|expert|lint)" package.json` in `/Users/yuan/Projects/Exam/Exam_prepare_site`.
2. Observe that `package.json` returns no matching script keys for `pipeline:producer`, `pipeline:tutor`, `pipeline:expert`, or `pipeline:lint`.
3. Run `npm run pipeline:lint` or `npm run pipeline:producer` in terminal and observe `npm ERR! missing script`.

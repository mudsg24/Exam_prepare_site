# Milestone 3 Verification & Quality Gate Handoff Report — Reviewer 2

## Review Summary

**Verdict**: REQUEST_CHANGES

**Target Scope**: 7 `/tn-exam-*` skills in `/Users/yuan/.gemini/config/skills/`
1. `tn-exam-prepare`
2. `tn-exam-qc`
3. `tn-exam-expert`
4. `tn-exam-producer`
5. `tn-exam-tutor`
6. `tn-exam-lecture-and-practice`
7. `tn-exam-query`

---

## 1. Observation

### Observation 1: Hardcoded Relative `scripts/` Paths Remaining
Command executed:
```bash
grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*
```
Output verbatim:
```text
/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md:16:5. **Phase 5: 自動化 Static Linter 驗證 (Automated Static Linter Clearance)**：執行 `node scripts/lint_exam_json.mjs` 確保 100% 通過 Build 打包門檻。
/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md:84:1. 主 Session 呼叫 `run_command`: `node scripts/lint_exam_json.mjs`。
/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md:103:    - 靜態 Linter `scripts/lint_exam_json.mjs` 會自動對所有 JSON 進行 (1) `sourceExplanation` 抄襲比對與 (2) Account 1 與 Account 2 回答字元 100% 同字比對。凡檢出造假一律中斷 Build。
/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md:158:     - 在 `Exam_prepare_site/` 目錄執行 `npm run build` (自動執行 `node scripts/lint_exam_json.mjs` 與 `tsc`)，確保 0 Static Lint Errors 且構建完全成功。
/Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md:149:   - **強制驗證關卡 (Build & Schema Audit Gate)**：執行 `npm run build`（包含 `node scripts/lint_exam_json.mjs` 與 `tsc`），確認零 Static Lint Errors 且構建完全成功後方可結案。
/Users/yuan/.gemini/config/skills/tn-exam-producer/SKILL.md:118:   - **強制驗證關卡 (Build & Schema Audit Gate)**：執行 `npm run build`（包含 `node scripts/lint_exam_json.mjs` 與 `tsc`），確認零 Static Lint Errors 且構建完全成功後方可結案。
/Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md:78:  - 腳本 (`scripts/exam_qc.mjs`) 僅作為純 JSON 讀寫與長度檢查器，不得包含任何選項解析或答案比對邏輯。
```
- Total matches: 7 instances across 5 skill files.
- Additionally, `scripts/lint_exam_json.mjs` is an outdated relative path compared to SSOT rule in `AGENTS.md` (`scripts/pipeline/lint/lint_exam_json.mjs`).

### Observation 2: Residual QC Calls & Workflow Steps in `tn-exam-expert/SKILL.md`
Inspection of `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md`:
- **Line 3 (Description)**: `description: "... /tn-exam-qc 品質過濾與 NLM 可讀性重整門面 Skill..."`
- **Line 14 (Purpose Phase 3)**: `3. Phase 3: 執行 /tn-exam-qc 品管 (NLM Quality Control)：消除 <200 字短回答，雙重語意校對選項並寫入 qcVerified: true。`
- **Line 74-78 (Execution Step 4)**: 
  ```markdown
  ### Step 4: Phase 3 - Execute /tn-exam-qc Pipeline (步驟 4: Phase 3 執行 NLM 品質控制)
  1. 呼叫 /tn-exam-qc <target_paper>:
     - Stage 1 Gate：檢查所有 NLM 回答字數是否 >= 200 字...
     - Stage 2 Gate：派發 Subagents 直讀原檔與 NLM 全文語意判讀 selectedOption...
  ```
- **Line 93 (Output Contract)**: `Phase 3: /tn-exam-qc 提問補齊與校對結案題數 (qcVerified: true)`

### Observation 3: YAML Frontmatter Verification
Inspected lines 1-5 of all 7 `SKILL.md` files:
- `tn-exam-prepare`: Valid YAML (`name: tn-exam-prepare`, `description: ...`, `user-invocable: true`)
- `tn-exam-qc`: Valid YAML
- `tn-exam-expert`: Valid YAML
- `tn-exam-producer`: Valid YAML
- `tn-exam-tutor`: Valid YAML
- `tn-exam-lecture-and-practice`: Valid YAML
- `tn-exam-query`: Valid YAML

### Observation 4: Subagent Architecture of `tn-exam-lecture-and-practice/SKILL.md`
Inspected `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md`:
- All content generation phases delegate via `invoke_subagent`: `Lecture Author Subagent`, `MCQ Producer Subagent`, `NLM Reconciler Subagent`, `Lecture Dedicated QC Subagent`, `Exam Dedicated QC Subagent`.
- No internal inline prose/content generation prompt blocks (e.g. `你是專責...`) exist for main session direct generation.

### Observation 5: Governance Rule Duplication Across 7 Skills
Comparing Governance sections:
- `STRICT LANGUAGE CONTRACT FOR SUBAGENTS & QC` is copied verbatim across `tn-exam-prepare` (lines 25-34), `tn-exam-producer` (lines 28-37), and `tn-exam-lecture-and-practice` (lines 30-39).
- `LIFECYCLE ABSOLUTE BAN ON REGEX & SCRIPTS` and `ABSOLUTE BAN ON MECHANICAL/REGEX OPTION EXTRACTION` are copied verbatim across `tn-exam-prepare` (lines 38-41, 72-75), `tn-exam-qc` (lines 36-39, 76-79), `tn-exam-producer` (lines 23-26, 38-40), and `tn-exam-lecture-and-practice` (lines 44, 87-91).
- `SYNTHETIC CLASSIFICATION HEADERS ABSOLUTE BAN` is copied verbatim across `tn-exam-prepare` (lines 42-44), `tn-exam-producer` (lines 41-43), `tn-exam-lecture-and-practice` (lines 45), and `tn-exam-expert` (lines 39-41).
- `DATABASE & MANIFEST JSON SCHEMA STRICT CONTRACT` is copied verbatim across `tn-exam-producer` (lines 54-82) and `tn-exam-lecture-and-practice` (lines 63-82).

---

## 2. Logic Chain

1. **Verification Criterion 1 (YAML Frontmatter)**: Directly supported by Observation 3. All 7 skills contain valid YAML metadata blocks with required `name`, `description`, and `user-invocable` properties. -> **PASS**.
2. **Verification Criterion 2 (No hardcoded `scripts/` paths)**: Observation 1 demonstrates 7 occurrences of hardcoded relative `scripts/` references (`scripts/lint_exam_json.mjs`, `scripts/exam_qc.mjs`). Furthermore, `scripts/lint_exam_json.mjs` points to a legacy un-nested script location rather than `scripts/pipeline/lint/lint_exam_json.mjs`. -> **FAIL (Critical)**.
3. **Verification Criterion 3 (`tn-exam-lecture-and-practice` Subagent Dispatch)**: Observation 4 confirms that `tn-exam-lecture-and-practice` operates strictly as a dispatch-only coordinator delegating to subagents via `invoke_subagent`, without inline prompt templates for main session content synthesis. -> **PASS**.
4. **Verification Criterion 4 (`tn-exam-expert` No QC Calls)**: Observation 2 shows that `tn-exam-expert` explicitly retains Phase 3 (`Execute /tn-exam-qc Pipeline`) in its Description, Purpose, Execution Algorithm (Step 4), and Output Contract. -> **FAIL (Critical)**.
5. **Verification Criterion 5 (Governance Rule Cleanup)**: Observation 5 shows that extensive multi-paragraph governance rules remain copy-pasted across 5 of the 7 skills rather than being consolidated or referencing workspace SSOT (`AGENTS.md`). -> **FAIL (Major)**.

---

## 3. Caveats

- No caveats. All 5 criteria were evaluated via exact, deterministic read-only file and grep checks.

---

## 4. Conclusion & Findings

### Findings List

#### [Critical] Finding 1: Hardcoded Relative `scripts/` Paths Present
- **Where**: 
  - `tn-exam-expert/SKILL.md`: lines 16, 84
  - `tn-exam-lecture-and-practice/SKILL.md`: lines 103, 158
  - `tn-exam-prepare/SKILL.md`: line 149
  - `tn-exam-producer/SKILL.md`: line 118
  - `tn-exam-qc/SKILL.md`: line 78
- **Why**: Hardcoded relative paths break when commands are executed from different subdirectories and violate the path independence governance rule. Additionally, `scripts/lint_exam_json.mjs` is an outdated path (SSOT: `scripts/pipeline/lint/lint_exam_json.mjs`).
- **Suggestion**: Replace relative `scripts/...` calls with npm/package script wrappers (e.g. `npm run build` or `node scripts/pipeline/lint/lint_exam_json.mjs`) or relative path parameterization anchored to the workspace root.

#### [Critical] Finding 2: Legacy QC Calls and Workflow Steps in `tn-exam-expert`
- **Where**: `tn-exam-expert/SKILL.md` (lines 3, 14, 74-78, 93)
- **Why**: Milestone 3 scope required `tn-exam-expert` to have NO QC calls or workflow steps (decoupling expert pre-practice formatting from the automated NLM QC pipeline). Retaining Phase 3 (`Execute /tn-exam-qc Pipeline`) violates this architectural separation.
- **Suggestion**: Remove Phase 3 (`/tn-exam-qc` invocation) from `tn-exam-expert/SKILL.md` and adjust the 5-Phase workflow to a 4-Phase workflow focusing purely on De-Walling, Anti-Strikethrough, Readability Formatting, and Linter Clearance.

#### [Major] Finding 3: Unconsolidated Duplicate Governance Rules Across Skills
- **Where**: `tn-exam-prepare`, `tn-exam-producer`, `tn-exam-lecture-and-practice`, `tn-exam-qc`, `tn-exam-expert`
- **Why**: Duplicating identical multi-line governance rules across skill files creates maintenance debt and risk of rule drift when updates occur.
- **Suggestion**: Clean up redundant copy-pasted governance sections across skills by referencing the workspace SSOT rules in `AGENTS.md`.

---

## Verified Claims Matrix

| Claim | Verification Method | Status |
|---|---|---|
| Every `SKILL.md` has valid YAML frontmatter header | Checked lines 1-5 of all 7 `SKILL.md` files | PASS |
| `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*` returns NO hardcoded `scripts/...` paths | Executed `grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*` | FAIL (7 matches found) |
| `tn-exam-lecture-and-practice/SKILL.md` strictly dispatch-only via `invoke_subagent` | Inspected execution algorithm and subagent delegation in `tn-exam-lecture-and-practice/SKILL.md` | PASS |
| `tn-exam-expert` contains NO QC calls or workflow steps | Inspected `tn-exam-expert/SKILL.md` lines 3, 14, 74-78, 93 | FAIL (Phase 3 retains `/tn-exam-qc` call) |
| Duplicate governance rules cleaned up across 7 skills | Cross-compared Governance sections across all 7 skills | FAIL (Extensive verbatim duplication remains) |

---

## 5. Design Judgment

From an architectural perspective:
1. **Decoupling Gate**: `tn-exam-expert` is intended for pre-practice document enhancement (formatting, de-walling, latex/strikethrough fix). Coupling it directly to `/tn-exam-qc` causes unnecessary re-asking and dual-NLM overhead during practice preparation. Stripping Phase 3 from `tn-exam-expert` is required to restore clear responsibility boundaries.
2. **SSOT Script Invocation**: Skills should avoid hardcoding direct script relative paths like `node scripts/lint_exam_json.mjs`. Using standardized workspace build targets or SSOT script paths (`scripts/pipeline/lint/lint_exam_json.mjs`) ensures consistency across environments.

---

## 6. Verification Method (For Independent Verification)

Run the following shell commands to verify all observations and findings:

```bash
# 1. Verify hardcoded scripts paths:
grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*

# 2. Verify tn-exam-expert QC references:
grep -rn "tn-exam-qc" ~/.gemini/config/skills/tn-exam-expert/SKILL.md

# 3. Verify YAML headers across all 7 skills:
head -n 5 ~/.gemini/config/skills/tn-exam-*/SKILL.md
```

**Invalidation Conditions**:
- If `grep -rn "scripts/" ~/.gemini/config/skills/tn-exam-*` returns 0 matches.
- If `grep -rn "tn-exam-qc" ~/.gemini/config/skills/tn-exam-expert/SKILL.md` returns 0 matches outside of optional historical notes.
- If duplicate governance rules are refactored into clean concise references.

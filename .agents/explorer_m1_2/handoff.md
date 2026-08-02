# Handoff Report — Phase 3 Skills Refactoring Audit (Milestone 1)

## 1. Observation

Direct observations from examining the four skill files located at `/Users/yuan/.gemini/config/skills/`:

### A. `tn-exam-expert/SKILL.md`
- **File Location**: `/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md` (96 lines)
- **Misaligned QC Calls & References**:
  - **Line 3 (Frontmatter description)**: `... /tn-exam-qc 品質過濾與 NLM 可讀性重整門面 Skill...`
  - **Line 14 (Purpose, Phase 3)**: `3. Phase 3: 執行 /tn-exam-qc 品管 (NLM Quality Control)：消除 <200 字短回答，雙重語意校對選項並寫入 qcVerified: true。`
  - **Lines 74–78 (Execution Algorithm, Step 4)**:
    ```markdown
    ### Step 4: Phase 3 - Execute `/tn-exam-qc` Pipeline (步驟 4: Phase 3 執行 NLM 品質控制)
    1. 呼叫 `/tn-exam-qc <target_paper>`：
       - **Stage 1 Gate**：檢查所有 NLM 回答字數是否 >= 200 字，若有短回答或 `INSUFFICIENT`，自動呼叫 `/tn-nlm-asking-mcqs` 重新提問。
       - **Stage 2 Gate**：派發 Subagents 直讀原檔與 NLM 全文語意判讀 `selectedOption`，寫入 `qcVerified: true`。
    ```
  - **Line 93 (Progress & Output Contract)**: `- Phase 3: /tn-exam-qc 提問補齊與校對結案題數 (qcVerified: true)`
- **Outdated Script Paths**:
  - **Line 16 (Purpose, Phase 5)**: `node scripts/lint_exam_json.mjs`
  - **Line 84 (Execution Algorithm, Step 6)**: `node scripts/lint_exam_json.mjs`
  - *Verification*: `node scripts/lint_exam_json.mjs` does not exist in root `scripts/`. Running `node scripts/pipeline/lint/lint_exam_json.mjs` succeeded with clean output (checking 103 exam files).

### B. `tn-exam-producer/SKILL.md`
- **File Location**: `/Users/yuan/.gemini/config/skills/tn-exam-producer/SKILL.md` (127 lines)
- **Outdated Script Path**:
  - **Line 118 (Execution Algorithm, Phase 6)**: `node scripts/lint_exam_json.mjs` (Missing path directory `pipeline/lint/`).
- **Redundant Governance Rules (Duplicating `AGENTS.md`)**:
  - **Lines 28–37 (`STRICT LANGUAGE CONTRACT FOR SUBAGENTS & QC`)**: Verbatim duplicates `AGENTS.md` Rule 7.
  - **Lines 38–40 (`LIFECYCLE ABSOLUTE BAN ON REGEX & SCRIPTS`)**: Verbatim duplicates `AGENTS.md` Rule 1.
  - **Lines 41–42 (`SYNTHETIC CLASSIFICATION HEADERS ABSOLUTE BAN`)**: Verbatim duplicates `AGENTS.md` Rule 2.
  - **Lines 43–46 (`MANDATORY NLM RESPONSE QUALITY & RE-ASKING GATE`)**: Duplicates `AGENTS.md` Rule 5 / Rule 12.
  - **Lines 54–82 (`DATABASE & MANIFEST JSON SCHEMA STRICT CONTRACT`)**: Verbatim duplicates `AGENTS.md` Rule 10.

### C. `tn-exam-tutor/SKILL.md`
- **File Location**: `/Users/yuan/.gemini/config/skills/tn-exam-tutor/SKILL.md` (94 lines)
- **Missing Linter Script Path Reference**:
  - **Line 93 (Phase 6)**: `寫入 public/server-data/tutorials/ 並執行 npm run build` — Omits explicit invocation of `node scripts/pipeline/lint/lint_tutorial_json.mjs`.
  - *Verification*: `node scripts/pipeline/lint/lint_tutorial_json.mjs` exists and passed (checked 77 tutorial JSON files).
- **Redundant Governance Rules (Duplicating `AGENTS.md`)**:
  - **Lines 28–32 (`章節層級正式權威圖片檢索與雙庫引用鐵律`)**: Duplicates `AGENTS.md` Rule 6.
  - **Lines 37–46 (`STRICT TUTORIAL DIAGRAM SCHEMA CONTRACT`)**: Duplicates `AGENTS.md` Rule 11.
  - **Lines 63–67 (`Zero Chinese Technical Terms & Zero Parenthetical Translations`)**: Duplicates `AGENTS.md` Rule 7.

### D. `tn-exam-lecture-and-practice/SKILL.md`
- **File Location**: `/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md` (173 lines)
- **Role Violation (Inline Generation instead of Pure Delegation)**:
  - **Lines 115–121 (Phase 2 Masterclass Lecture Generation)**: Inline content generation logic spawning `Lecture Author Subagent` instead of dispatching `tn-exam-tutor` via `invoke_subagent`.
  - **Lines 122–128 (Phase 3 High-Yield MCQ Generation)**: Inline content generation logic spawning `MCQ Producer Subagent` instead of dispatching `tn-exam-producer` via `invoke_subagent`.
  - **Lines 129–144 (Phases 4 & 5 Dual NLM asking, Reconciliation, Double-QC)**: Monolithic duplicate execution of NLM asking and QC subagents rather than delegating lifecycle management to producer and tutor sub-skills.
- **Massive Governance Rule Duplication**:
  - **Lines 25–29 (`LECTURE QUALITY MANDATE`)**: Duplicates `tn-exam-tutor`.
  - **Lines 30–39 (`STRICT LANGUAGE CONTRACT`)**: Duplicates `AGENTS.md` Rule 7.
  - **Lines 40–46 (`PRACTICE QUESTION QUALITY MANDATE`)**: Duplicates `tn-exam-producer`.
  - **Lines 47–49 (`MANDATORY DUAL NLM ASKING`)**: Duplicates `AGENTS.md` Rule 5 / `tn-exam-producer`.
  - **Lines 50–52 (`CHAPTER & FIGURE INDEX COMPLIANCE`)**: Duplicates `AGENTS.md` Rule 6 / `tn-exam-tutor`.
  - **Lines 53–62 (`STRICT TUTORIAL DIAGRAM SCHEMA CONTRACT`)**: Duplicates `AGENTS.md` Rule 11 / `tn-exam-tutor`.
  - **Lines 63–83 (`DATABASE & MANIFEST JSON SCHEMA STRICT CONTRACT`)**: Duplicates `AGENTS.md` Rule 10 / `tn-exam-producer`.
  - **Lines 87–91 (`ABSOLUTE BAN ON REGEX NLM OPTION EXTRACTION`)**: Duplicates `AGENTS.md` Rule 4.
  - **Lines 93–104 (`ABSOLUTE BAN ON FAKED/SYNTHETIC NLM RESPONSES & HONEST FAILURE DEGRADATION PROTOCOL`)**: Duplicates `AGENTS.md` Rule 12.
- **Outdated Script Paths**:
  - **Line 103 (Boundary)**: `scripts/lint_exam_json.mjs`
  - **Line 158 (Phase 6)**: `node scripts/lint_exam_json.mjs`

---

## 2. Logic Chain

1. **`tn-exam-expert` Scope Boundary Clarification**:
   - *Observation*: Lines 14 and 74–78 mandate executing `/tn-exam-qc`.
   - *Reasoning*: `tn-exam-expert` is intended as a pre-processing tool for de-walling long clinical stems, fixing wave-tilde anti-strikethrough issues, and reorganizing layout/images. Combining QC into `tn-exam-expert` violates single-responsibility design and causes redundant, unexpected QC execution during layout pre-processing.
   - *Conclusion*: Remove all `/tn-exam-qc` invocations and references from `tn-exam-expert`, reducing its workflow from 5 phases to 3 clean pre-processing phases (Phase 1: Stem De-walling & Formatting, Phase 2: Independent Review Audit Subagent, Phase 3: Automated Static Linter Clearance).

2. **Script Path Standardization (`scripts/...` -> `scripts/pipeline/lint/...`)**:
   - *Observation*: `tn-exam-expert` (lines 16, 84), `tn-exam-producer` (line 118), and `tn-exam-lecture-and-practice` (lines 103, 158) refer to `scripts/lint_exam_json.mjs`.
   - *Reasoning*: The actual script path is `scripts/pipeline/lint/lint_exam_json.mjs`. Calling `node scripts/lint_exam_json.mjs` will cause a file-not-found runtime failure during build checks.
   - *Conclusion*: Update all references across the three skills to `node scripts/pipeline/lint/lint_exam_json.mjs`. Additionally, add `node scripts/pipeline/lint/lint_tutorial_json.mjs` to `tn-exam-tutor`.

3. **Governance Rule De-duplication against `AGENTS.md`**:
   - *Observation*: Extensive governance sections in `tn-exam-producer`, `tn-exam-tutor`, and `tn-exam-lecture-and-practice` copy-paste verbatim rules from `AGENTS.md` (e.g., Pure English medical terms, Regex bans, Schema contracts, Image path integrity).
   - *Reasoning*: `AGENTS.md` in `Exam_prepare_site` is the Single Source of Truth (SSOT) for global rules. Inline duplication across individual skills creates maintenance friction and risk of policy drift when rules update.
   - *Conclusion*: Refactor skills to reference `AGENTS.md` rules by name and number, removing redundant inline blocks.

4. **`tn-exam-lecture-and-practice` Pure Dispatcher Transformation**:
   - *Observation*: `tn-exam-lecture-and-practice` contains 173 lines of code including inline content generation logic (Phase 2 & Phase 3) and direct subagent prompts for tutor/producer.
   - *Reasoning*: `tn-exam-lecture-and-practice` must function strictly as a top-level Orchestrator / Dispatcher. It should parse user input, synthesize the Lesson Map & Practice Plan (Phase 1), and then dispatch `tn-exam-tutor` and `tn-exam-producer` via `invoke_subagent` to handle content generation, NLM asking, reconciliation, QC, and database ingestion.
   - *Conclusion*: Strip all inline content generation prompt logic and duplicated governance rules from `tn-exam-lecture-and-practice`, refactoring it into a clean 3-step dispatcher algorithm:
     1. Parse user input and synthesize Lesson Map + Practice Plan.
     2. Dispatch `tn-exam-tutor` via `invoke_subagent` to generate masterclass lecture.
     3. Dispatch `tn-exam-producer` via `invoke_subagent` to generate practice test bank.

---

## 3. Caveats

- **No Source Modifications Made**: As Explorer 2 operating under read-only audit constraints, no modifications were made to `/Users/yuan/.gemini/config/skills/`. All recommended changes are documented for Phase 3 implementation.
- **External Dependency Assumptions**: Assumes `tn-exam-tutor` and `tn-exam-producer` skills are user-invocable or subagent-invocable via `invoke_subagent`.

---

## 4. Conclusion & Recommended Refactoring Blueprint

### Skill 1: `tn-exam-expert` Refactoring Plan
- **Description & Purpose**: Remove `/tn-exam-qc` from description and purpose. Reframe as dedicated pre-practice text wall de-walling and LaTeX/Markdown formatting expert.
- **QC Removal**:
  - Remove Phase 3 (`/tn-exam-qc` execution) from Purpose (Line 14), Execution Algorithm Step 4 (Lines 74-78), and Progress Contract (Line 93).
- **Script Path Fix**:
  - Replace `node scripts/lint_exam_json.mjs` with `node scripts/pipeline/lint/lint_exam_json.mjs` on lines 16 and 84.

### Skill 2: `tn-exam-producer` Refactoring Plan
- **Script Path Fix**:
  - Replace `node scripts/lint_exam_json.mjs` with `node scripts/pipeline/lint/lint_exam_json.mjs` on line 118.
- **De-duplication**:
  - Replace inline governance blocks (lines 28–82) with concise references to `AGENTS.md` Rules 1, 2, 5, 7, 10, 12.

### Skill 3: `tn-exam-tutor` Refactoring Plan
- **Script Path Addition**:
  - In Phase 6 (Execution Algorithm), explicitly add `node scripts/pipeline/lint/lint_tutorial_json.mjs` prior to `npm run build`.
- **De-duplication**:
  - Replace inline governance blocks (lines 28–32, 37–46, 63–67) with references to `AGENTS.md` Rules 6, 7, 11.

### Skill 4: `tn-exam-lecture-and-practice` Refactoring Plan
- **Role Transformation to Pure Dispatcher**:
  - Strip inline content prompt logic (Lines 115–144).
  - Remove duplicate governance blocks (Lines 25–104).
  - Update script paths on lines 103 and 158 to `scripts/pipeline/lint/lint_exam_json.mjs`.
  - Structure Execution Algorithm into pure orchestration:
    - Step 1: Parse topic, query DB & reference materials, generate Lesson Map + Practice Plan.
    - Step 2: Call `invoke_subagent` to execute `tn-exam-tutor` for lecture generation.
    - Step 3: Call `invoke_subagent` to execute `tn-exam-producer` for practice question bank generation.
    - Step 4: Verify build with `npm run build` and return report to user.

---

## 5. Verification Method

1. **Script Path Verification**:
   - Run `node scripts/pipeline/lint/lint_exam_json.mjs` in workspace root `/Users/yuan/Projects/Exam/Exam_prepare_site` to confirm zero lint errors.
   - Run `node scripts/pipeline/lint/lint_tutorial_json.mjs` in workspace root `/Users/yuan/Projects/Exam/Exam_prepare_site` to confirm zero tutorial lint errors.
2. **Post-Implementation Grep Audit**:
   - Execute `grep -rn "scripts/lint_exam_json.mjs" /Users/yuan/.gemini/config/skills/` to ensure 0 outdated script path references remain.
   - Execute `grep -rn "tn-exam-qc" /Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md` to confirm 0 QC references remain in `tn-exam-expert`.

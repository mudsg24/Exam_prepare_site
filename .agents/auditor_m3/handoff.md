# Forensic Audit Report — Milestone 3 (Verification & Quality Gate)

**Work Product**: 7 Refactored Skills in `/Users/yuan/.gemini/config/skills/tn-exam-*`  
**Working Directory**: `/Users/yuan/Projects/Exam/Exam_prepare_site/.agents/auditor_m3/`  
**Profile**: General Project  
**Verdict**: **INTEGRITY VIOLATION**

---

## 1. Observation

Direct empirical observations gathered during forensic verification:

### Observation 1: YAML Frontmatter Parsing
Ran automated YAML parser across all 7 `SKILL.md` files:
```
/Users/yuan/.gemini/config/skills/tn-exam-expert/SKILL.md: PASS (name="tn-exam-expert")
/Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md: PASS (name="tn-exam-lecture-and-practice")
/Users/yuan/.gemini/config/skills/tn-exam-prepare/SKILL.md: PASS (name="tn-exam-prepare")
/Users/yuan/.gemini/config/skills/tn-exam-producer/SKILL.md: PASS (name="tn-exam-producer")
/Users/yuan/.gemini/config/skills/tn-exam-qc/SKILL.md: PASS (name="tn-exam-qc")
/Users/yuan/.gemini/config/skills/tn-exam-query/SKILL.md: PASS (name="tn-exam-query")
/Users/yuan/.gemini/config/skills/tn-exam-tutor/SKILL.md: PASS (name="tn-exam-tutor")
```

### Observation 2: Legacy Script Paths (`scripts/`) Contamination
Ran `grep -r "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-*`. Found 7 legacy script path references across 5 files:
1. `tn-exam-expert/SKILL.md:5`: `執行 node scripts/lint_exam_json.mjs 確保 100% 通過 Build 打包門檻。`
2. `tn-exam-expert/SKILL.md:63`: `主 Session 呼叫 run_command: node scripts/lint_exam_json.mjs。`
3. `tn-exam-lecture-and-practice/SKILL.md:103`: `靜態 Linter scripts/lint_exam_json.mjs 會自動對所有 JSON...`
4. `tn-exam-lecture-and-practice/SKILL.md:158`: `在 Exam_prepare_site/ 目錄執行 npm run build (自動執行 node scripts/lint_exam_json.mjs 與 tsc)...`
5. `tn-exam-prepare/SKILL.md:149`: `執行 npm run build（包含 node scripts/lint_exam_json.mjs 與 tsc）...`
6. `tn-exam-producer/SKILL.md:118`: `執行 npm run build（包含 node scripts/lint_exam_json.mjs 與 tsc）...`
7. `tn-exam-qc/SKILL.md:78`: `腳本 (scripts/exam_qc.mjs) 僅作為純 JSON 讀寫與長度檢查器...`

Checking `/Users/yuan/Projects/Exam/Exam_prepare_site/scripts`:
- Neither `scripts/lint_exam_json.mjs` nor `scripts/exam_qc.mjs` exists at the root of `scripts/`. They were moved to `scripts/pipeline/lint/lint_exam_json.mjs` and `scripts/pipeline/qc/exam_qc.mjs`.

### Observation 3: Non-Existent (Phantom) npm Pipeline Scripts
Inspected `/Users/yuan/Projects/Exam/Exam_prepare_site/package.json` scripts section:
```json
  "scripts": {
    "dev": "vite",
    "lint:exams": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs",
    "check:assets": "node scripts/pipeline/lint/check_assets.mjs",
    "build": "node scripts/pipeline/lint/lint_exam_json.mjs && node scripts/pipeline/lint/lint_tutorial_json.mjs && node scripts/pipeline/lint/check_assets.mjs && tsc && vite build",
    "preview": "vite preview",
    "build:images": "node scripts/pipeline/utils/build_image_index.mjs",
    "test": "vitest run",
    "test:coverage": "vitest run --coverage",
    "test:py": "pytest --cov=scripts scripts/__tests__/",
    "prepare": "husky"
  }
```
Inspected instructions in `SKILL.md` files:
- `tn-exam-expert/SKILL.md`: Instructs executing `npm run pipeline:expert` and `npm run pipeline:lint`.
- `tn-exam-producer/SKILL.md`: Instructs executing `npm run pipeline:producer` and `npm run pipeline:lint`.
- `tn-exam-tutor/SKILL.md`: Instructs executing `npm run pipeline:tutor` and `npm run pipeline:lint`.

Executed `npm run pipeline:lint` and `npm run pipeline:expert`:
```
npm error Missing script: "pipeline:lint"
npm error Missing script: "pipeline:expert"
```
None of `pipeline:expert`, `pipeline:producer`, `pipeline:tutor`, or `pipeline:lint` exist in `package.json`.

### Observation 4: `tn-exam-lecture-and-practice` Inline Execution & Phantom Script
Inspected `tn-exam-lecture-and-practice/SKILL.md`:
- Phase 6 (lines 146–160): Instructs the Main Session to directly perform Python gate checks ("主 Session 必須執行 Python 門閥腳本對題庫與講堂進行 100% 欄位掃描..."), directly write JSON files (`public/server-data/2026_<topic>_(主題備考).json` and `public/server-data/tutorials/...`), directly update `exams_manifest.json`, and run `npm run build`.
- The "Python 門閥腳本" is unspecified (no path or command provided).
- Phase 6 contains non-dispatch inline logic performed by the Main Session instead of pure subagent dispatch (`invoke_subagent`).

---

## 2. Logic Chain

1. **Acceptance Criterion 1 (YAML Frontmatter)**:
   - *Observation*: All 7 files parsed without errors using `yaml.safe_load()`.
   - *Deduction*: Acceptance Criterion 1 is PASSED.

2. **Acceptance Criterion 2 (`grep -r "scripts/"`)**:
   - *Observation*: `grep -r "scripts/"` returned 7 occurrences of old script paths (`node scripts/lint_exam_json.mjs` and `scripts/exam_qc.mjs`).
   - *Observation*: Files on disk do not exist at root `scripts/`.
   - *Deduction*: Acceptance Criterion 2 is FAILED. Legacy non-existent script paths remain in 5 skill files.

3. **Acceptance Criterion 3 (`tn-exam-lecture-and-practice` Pure Dispatch)**:
   - *Observation*: `tn-exam-lecture-and-practice/SKILL.md` instructs the Main Session to run an unnamed Python gate script, write JSON files directly, update `exams_manifest.json` directly, and run `npm run build`.
   - *Deduction*: Acceptance Criterion 3 is FAILED. The skill contains inline main-session execution logic rather than pure dispatch logic via `invoke_subagent`.

4. **Acceptance Criterion 4 (`npm run pipeline:*` format)**:
   - *Observation*: `tn-exam-expert`, `tn-exam-producer`, `tn-exam-tutor` instruct running `npm run pipeline:expert`, `npm run pipeline:producer`, `npm run pipeline:tutor`, `npm run pipeline:lint`.
   - *Observation*: `package.json` in `Exam_prepare_site` contains no such npm scripts. `npm run pipeline:lint` crashes with `npm error Missing script`.
   - *Deduction*: Acceptance Criterion 4 is FAILED. The skills instruct execution of phantom npm commands that do not exist, causing fatal runtime crashes if invoked.

5. **Facade Implementation & Incomplete Refactoring Assessment**:
   - *Observation*: The refactored documentation created a facade layer by referencing phantom npm commands (`pipeline:*`) and non-existent legacy script locations (`scripts/lint_exam_json.mjs`).
   - *Deduction*: This constitutes an **INTEGRITY VIOLATION** under Prohibited Pattern #2 (Facade implementations) and Prohibited Pattern #3 (Incomplete/Fabricated refactoring).

---

## 3. Caveats

No caveats. All findings were verified through direct empirical command execution and exact file inspection.

---

## 4. Conclusion

**Verdict: INTEGRITY VIOLATION**

Summary of Acceptance Criteria:
1. YAML frontmatter parses properly: **PASS**
2. `grep -r "scripts/" ~/.gemini/config/skills/tn-exam-*` returns 0 old script paths: **FAIL** (7 matches found)
3. `tn-exam-lecture-and-practice/SKILL.md` contains only dispatch logic via `invoke_subagent`: **FAIL** (contains inline main-session serialization logic and unnamed Python script references)
4. Script invocations follow `npm run pipeline:*` format: **FAIL** (instructs running non-existent scripts `pipeline:expert`, `pipeline:producer`, `pipeline:tutor`, `pipeline:lint` missing from `package.json`)

Required Remediation Actions before Re-Audit:
1. Update `package.json` in `Exam_prepare_site` to define valid npm scripts (e.g. `pipeline:expert`, `pipeline:producer`, `pipeline:tutor`, `pipeline:lint` or update `SKILL.md` files to target valid package scripts like `lint:exams`).
2. Remove all 7 legacy `scripts/` path references (`node scripts/lint_exam_json.mjs`, `scripts/exam_qc.mjs`) from `SKILL.md` files.
3. Refactor `tn-exam-lecture-and-practice/SKILL.md` Phase 6 to use pure subagent dispatch via `invoke_subagent` and reference exact script paths/npm commands.

---

## 5. Verification Method

To independently verify these findings:

1. **Verify YAML Frontmatter**:
   ```bash
   python3 -c "
   import glob, yaml, re
   for path in sorted(glob.glob('/Users/yuan/.gemini/config/skills/tn-exam-*/SKILL.md')):
       content = open(path).read()
       match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
       print(path, 'OK' if match and yaml.safe_load(match.group(1)) else 'FAIL')
   "
   ```

2. **Verify Legacy `scripts/` Paths**:
   ```bash
   grep -r "scripts/" /Users/yuan/.gemini/config/skills/tn-exam-*
   ```

3. **Verify Phantom npm Scripts**:
   ```bash
   cd /Users/yuan/Projects/Exam/Exam_prepare_site
   npm run pipeline:lint
   npm run pipeline:expert
   ```

4. **Inspect `tn-exam-lecture-and-practice/SKILL.md` Phase 6**:
   ```bash
   sed -n '146,160p' /Users/yuan/.gemini/config/skills/tn-exam-lecture-and-practice/SKILL.md
   ```

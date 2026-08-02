# Detailed Analysis: Phase 2 Script Modularization (R1 & R2)

## 1. Executive Summary

This report documents the detailed investigation of requirements **R1 (Pipeline Module Migration)** and **R2 (Internal Path Resolution Fix)** for `Exam_prepare_site`.
A total of **11 scripts** were cataloged and mapped for migration into 5 structured pipeline subdirectories under `scripts/pipeline/`.

Each script's path mechanisms (`__dirname`, `os.path.dirname(__file__)`, relative imports, `process.cwd()`, absolute paths) were audited line by line to determine the exact string replacements and line numbers required to maintain runtime path resolution after migration.

---

## 2. Directory & Script Migration Mapping (R1)

The designated script destinations under `scripts/pipeline/` are structured as follows:

| Subdirectory | Source File | Target Migration Path |
|---|---|---|
| `scripts/pipeline/lint/` | `scripts/lint_exam_json.mjs` | `scripts/pipeline/lint/lint_exam_json.mjs` |
| `scripts/pipeline/lint/` | `scripts/lint_tutorial_json.mjs` | `scripts/pipeline/lint/lint_tutorial_json.mjs` |
| `scripts/pipeline/lint/` | `scripts/check_assets.mjs` | `scripts/pipeline/lint/check_assets.mjs` |
| `scripts/pipeline/ingest/` | `scripts/ingest_exam.mjs` | `scripts/pipeline/ingest/ingest_exam.mjs` |
| `scripts/pipeline/ingest/` | `scripts/extract_and_attach_images.py` | `scripts/pipeline/ingest/extract_and_attach_images.py` |
| `scripts/pipeline/qc/` | `scripts/exam_qc.mjs` | `scripts/pipeline/qc/exam_qc.mjs` |
| `scripts/pipeline/qc/` | `scripts/merge_qc_results.mjs` | `scripts/pipeline/qc/merge_qc_results.mjs` |
| `scripts/pipeline/qc/` | `scripts/apply_qc_updates.py` | `scripts/pipeline/qc/apply_qc_updates.py` |
| `scripts/pipeline/nlm/` | `scripts/ask_nlm_for_2026.mjs` | `scripts/pipeline/nlm/ask_nlm_for_2026.mjs` |
| `scripts/pipeline/nlm/` | `scripts/ask_nlm_for_renal_transplant.mjs` | `scripts/pipeline/nlm/ask_nlm_for_renal_transplant.mjs` |
| `scripts/pipeline/nlm/` | `scripts/process_nlm_results.py` | `scripts/pipeline/nlm/process_nlm_results.py` |
| `scripts/pipeline/utils/` | `scripts/build_image_index.mjs` | `scripts/pipeline/utils/build_image_index.mjs` |

---

## 3. Internal Path Resolution Analysis (R2)

Moving scripts from `scripts/` (1 level deep) to `scripts/pipeline/<subfolder>/` (3 levels deep) alters the directory depth relative to the project root by **+2 levels**.

### 3.1 Group 1: `lint` (`scripts/pipeline/lint/`)

#### A. `scripts/lint_exam_json.mjs`
- **Current Path**: `scripts/lint_exam_json.mjs`
- **Target Path**: `scripts/pipeline/lint/lint_exam_json.mjs`
- **Path Resolution Audit**:
  - **Line 8**: `const SERVER_DATA_DIR = path.resolve(__dirname, '../public/server-data');`
    - *Analysis*: In `scripts/pipeline/lint/`, `__dirname` refers to `project_root/scripts/pipeline/lint`. Resolving `../public/server-data` would point to `project_root/scripts/pipeline/public/server-data` (NON-EXISTENT). Navigating 3 levels up (`../../../`) reaches `project_root/public/server-data`.
    - *Line Number*: Line 8
    - *Target Replacement*: `const SERVER_DATA_DIR = path.resolve(__dirname, '../../../public/server-data');`
  - **Line 208**: `const targetPath = filename.startsWith('/') ? path.join(__dirname, '../public', filename) : path.join(SERVER_DATA_DIR, filename);`
    - *Analysis*: Resolving `../public` from `scripts/pipeline/lint/` fails. Needs 3 levels up.
    - *Line Number*: Line 208
    - *Target Replacement*: `const targetPath = filename.startsWith('/') ? path.join(__dirname, '../../../public', filename) : path.join(SERVER_DATA_DIR, filename);`

#### B. `scripts/lint_tutorial_json.mjs`
- **Current Path**: `scripts/lint_tutorial_json.mjs`
- **Target Path**: `scripts/pipeline/lint/lint_tutorial_json.mjs`
- **Path Resolution Audit**:
  - **Line 8**: `const PUBLIC_DIR = path.resolve(__dirname, '../public');`
    - *Analysis*: Moving to `scripts/pipeline/lint/` requires 3 levels up to reach `public/`.
    - *Line Number*: Line 8
    - *Target Replacement*: `const PUBLIC_DIR = path.resolve(__dirname, '../../../public');`

#### C. `scripts/check_assets.mjs`
- **Current Path**: `scripts/check_assets.mjs`
- **Target Path**: `scripts/pipeline/lint/check_assets.mjs`
- **Path Resolution Audit**:
  - **Line 8**: `const PUBLIC_DIR = path.resolve(__dirname, '../public');`
    - *Analysis*: Moving to `scripts/pipeline/lint/` requires 3 levels up to reach `public/`.
    - *Line Number*: Line 8
    - *Target Replacement*: `const PUBLIC_DIR = path.resolve(__dirname, '../../../public');`

---

### 3.2 Group 2: `ingest` (`scripts/pipeline/ingest/`)

#### A. `scripts/ingest_exam.mjs`
- **Current Path**: `scripts/ingest_exam.mjs`
- **Target Path**: `scripts/pipeline/ingest/ingest_exam.mjs`
- **Path Resolution Audit**:
  - **Line 6**: `const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');`
  - **Line 371-372**: `path.join(process.cwd(), 'tmp_nlm_input.json')`
  - **Line 463**: `if (process.argv[1] && process.argv[1].endsWith('ingest_exam.mjs'))`
  - *Analysis*: Uses `process.cwd()` and string matching on filename suffix. Runtime working directory resolution is independent of script depth.
  - *Internal Path Fixes Required*: **0 changes needed**.

#### B. `scripts/extract_and_attach_images.py`
- **Current Path**: `scripts/extract_and_attach_images.py`
- **Target Path**: `scripts/pipeline/ingest/extract_and_attach_images.py`
- **Path Resolution Audit**:
  - **Lines 8-10**: Uses absolute paths (`DB_DIR = "/Users/yuan/Projects/..."`).
  - *Internal Path Fixes Required*: **0 changes needed**.

---

### 3.3 Group 3: `qc` (`scripts/pipeline/qc/`)

#### A. `scripts/exam_qc.mjs`
- **Current Path**: `scripts/exam_qc.mjs`
- **Target Path**: `scripts/pipeline/qc/exam_qc.mjs`
- **Path Resolution Audit**:
  - **Line 4**: `const SERVER_DATA_DIR = path.join(process.cwd(), 'public', 'server-data');`
  - *Internal Path Fixes Required*: **0 changes needed**.

#### B. `scripts/merge_qc_results.mjs`
- **Current Path**: `scripts/merge_qc_results.mjs`
- **Target Path**: `scripts/pipeline/qc/merge_qc_results.mjs`
- **Path Resolution Audit**:
  - **Lines 4-5**: Uses `process.cwd()` for `serverDataDir` and `scratchDir`.
  - *Internal Path Fixes Required*: **0 changes needed**.

#### C. `scripts/apply_qc_updates.py`
- **Current Path**: `scripts/apply_qc_updates.py`
- **Target Path**: `scripts/pipeline/qc/apply_qc_updates.py`
- **Path Resolution Audit**:
  - **Lines 49-50**: `grouped_path = "scratch/grouped_nlm_responses.json"`
  - *Internal Path Fixes Required*: **0 changes needed**.

---

### 3.4 Group 4: `nlm` (`scripts/pipeline/nlm/`)

#### A. `scripts/ask_nlm_for_2026.mjs`
- **Current Path**: `scripts/ask_nlm_for_2026.mjs`
- **Target Path**: `scripts/pipeline/nlm/ask_nlm_for_2026.mjs`
- **Path Resolution Audit**:
  - **Line 4**: `import { reconcileResponses } from './ingest_exam.mjs';`
    - *Analysis*: Currently, `ask_nlm_for_2026.mjs` and `ingest_exam.mjs` are siblings in `scripts/`. Under the new modular layout:
      - `ask_nlm_for_2026.mjs` resides in `scripts/pipeline/nlm/`
      - `ingest_exam.mjs` resides in `scripts/pipeline/ingest/`
      - The relative module path from `scripts/pipeline/nlm/` to `scripts/pipeline/ingest/ingest_exam.mjs` is `../ingest/ingest_exam.mjs`.
    - *Line Number*: Line 4
    - *Target Replacement*: `import { reconcileResponses } from '../ingest/ingest_exam.mjs';`

#### B. `scripts/ask_nlm_for_renal_transplant.mjs`
- **Current Path**: `scripts/ask_nlm_for_renal_transplant.mjs`
- **Target Path**: `scripts/pipeline/nlm/ask_nlm_for_renal_transplant.mjs`
- **Path Resolution Audit**:
  - **Line 4**: `import { reconcileResponses } from './ingest_exam.mjs';`
    - *Analysis*: Relative import must point to the relocated `ingest_exam.mjs` module in `scripts/pipeline/ingest/`.
    - *Line Number*: Line 4
    - *Target Replacement*: `import { reconcileResponses } from '../ingest/ingest_exam.mjs';`

#### C. `scripts/process_nlm_results.py`
- **Current Path**: `scripts/process_nlm_results.py`
- **Target Path**: `scripts/pipeline/nlm/process_nlm_results.py`
- **Path Resolution Audit**:
  - **Lines 6-7, 41**: Uses `scratch/` paths relative to `os.getcwd()`.
  - *Internal Path Fixes Required*: **0 changes needed**.

---

### 3.5 Group 5: `utils` (`scripts/pipeline/utils/`)

#### A. `scripts/build_image_index.mjs`
- **Current Path**: `scripts/build_image_index.mjs`
- **Target Path**: `scripts/pipeline/utils/build_image_index.mjs`
- **Path Resolution Audit**:
  - **Lines 4-8**: Uses absolute directory constants (`KDIGO_DIR`, `BRENNER_DIR`) and `process.cwd()`.
  - **Line 73**: Uses `fileURLToPath(import.meta.url) === path.resolve(process.argv[1])` which dynamically verifies direct execution regardless of directory.
  - *Internal Path Fixes Required*: **0 changes needed**.

---

## 4. Cross-Reference & Dependent Updates Index (R3 Context)

For complete situational awareness during execution (Milestone 2), external references that import or invoke these scripts must also be updated:

1. **`package.json`**:
   - `lint:exams`: Change `scripts/lint_exam_json.mjs` -> `scripts/pipeline/lint/lint_exam_json.mjs`, `scripts/lint_tutorial_json.mjs` -> `scripts/pipeline/lint/lint_tutorial_json.mjs`, `scripts/check_assets.mjs` -> `scripts/pipeline/lint/check_assets.mjs`
   - `build`: Same updates as `lint:exams`.
   - `check:assets`: Change `scripts/check_assets.mjs` -> `scripts/pipeline/lint/check_assets.mjs`
   - `build:images`: Change `scripts/build_image_index.mjs` -> `scripts/pipeline/utils/build_image_index.mjs`

2. **`scripts/__tests__/`**:
   - `lint_exam_json.test.mjs:4`: Change `'../lint_exam_json.mjs'` -> `'../pipeline/lint/lint_exam_json.mjs'`
   - `build_image_index.test.mjs:4`: Change `'../build_image_index.mjs'` -> `'../pipeline/utils/build_image_index.mjs'`
   - `test_extract_and_attach_images.py:8`: Update `sys.path` to include `'../pipeline/ingest'`

3. **`scripts/reask_anomalous.mjs` & `scripts/repair_nlm_dual_asking.mjs`**:
   - Line 4: Change `import { reconcileResponses } from './ingest_exam.mjs';` -> `import { reconcileResponses } from './pipeline/ingest/ingest_exam.mjs';`

4. **`vitest.config.ts`**:
   - Line 17: Change `'scripts/lint_exam_json.mjs'` -> `'scripts/pipeline/lint/lint_exam_json.mjs'`

5. **`AGENTS.md`**:
   - Rule 10 & 11: Update `node scripts/lint_exam_json.mjs` -> `node scripts/pipeline/lint/lint_exam_json.mjs` and `node scripts/check_assets.mjs` -> `node scripts/pipeline/lint/check_assets.mjs`.

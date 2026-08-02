# Summary of Changes

## Overview
- **File modified**: `scripts/pipeline/utils/build_image_index.mjs`
- **Issue fixed**: Resolved `SyntaxError: Duplicate export of 'buildImageIndex'` when running `npm run build:images`.

## Detailed Modification

### `scripts/pipeline/utils/build_image_index.mjs`
- **Line 53**: `export function buildImageIndex() { ... }` already exports `buildImageIndex` as a named export.
- **Line 71**: Previously contained `export { scanDir, buildImageIndex };`, causing `buildImageIndex` to be exported twice.
- **Change**: Modified line 71 from `export { scanDir, buildImageIndex };` to `export { scanDir };`.

## Verification Results

1. `npm run build:images`
   - **Status**: PASSED (Exit code 0)
   - **Output**: Indexed and copied 2762 images to `public/server-data/image_index.json`.

2. `npm run lint:exams`
   - **Status**: PASSED (Exit code 0)
   - **Output**: All exam JSON, tutorial JSON, and server-data asset integrity linters passed.

3. `npm run test`
   - **Status**: PASSED (Exit code 0)
   - **Output**: 14 test files passed, 98 tests passed.

4. `npm run test:py`
   - **Status**: PASSED (Exit code 0)
   - **Output**: 2 pytest unit tests passed.

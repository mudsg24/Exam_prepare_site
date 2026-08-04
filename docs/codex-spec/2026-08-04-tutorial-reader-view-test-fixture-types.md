# `TutorialReaderView` test fixture 型別修正

## Yuan 提出的狀況與目標

Yuan 指定回查 session `019fcc86-14ce-7040-b74e-c8b4b6a2f36a` 中提到的四個 TypeScript test fixture errors，確認 `src/components/__tests__/TutorialReaderView.test.tsx` 應如何修改，使 fixture 符合目前 tutorial type contract，並解除 `package.json` production build 在 `tsc` 階段的 blocker。

本次為 explicit `$lu-spec` discussion。除本報告外，未授權修改 test、production source、Git history、branch、remote 或 build output。

## Current sources 與 evidence

### Current authority

- `src/components/__tests__/TutorialReaderView.test.tsx`
  - `mockTutorial` 明確標註為 `ExamTutorial`。
  - 三個含 `imagePath` 的 diagram fixture 都缺少 `type`。
  - 第二個 module 缺少 `diagrams`。
  - tutorial 頂層缺少 `id`、`sourceCategory`、`updatedAt`。
- `src/types/exam.ts`
  - `TutorialDiagram.type` 為必填，允許 `'mermaid' | 'micrograph' | 'ai_illustration'`。
  - `TutorialModule.diagrams` 為必填 `TutorialDiagram[]`。
  - `ExamTutorial.id`、`sourceCategory`、`updatedAt` 均為必填 `string`。
- `package.json`
  - `build` 為 `npm run pipeline:lint && tsc && vite build`；因此 test fixture 的 TypeScript error 會阻止 production build 進入 Vite build。
- `tsconfig.json`
  - `include` 包含 `src`，未排除 `src/**/__tests__/**`，所以 production `tsc` 會檢查此 test fixture。

### Live diagnostics

執行 read-only `./node_modules/.bin/tsc --noEmit --pretty false`，目前得到四項 `TS2741`：

1. line 20：section `diagram` 缺少 `type`。
2. line 32：第一個 standalone diagram 缺少 `type`。
3. line 38：第二個 standalone diagram 缺少 `type`。
4. line 46：第二個 module 缺少 `diagrams`。

調查開始時 Git working tree 為 clean；建立本次 authorized `codex-spec` report 後，只有 `docs/codex-spec/2026-08-04-tutorial-reader-view-test-fixture-types.md` 是本 task 新增的 untracked artifact。

### Historical context

- 指定 session 的原始訊息確實把這四項列為 production build blocker。
- MemPalace `Exam_prepare_site/decisions` 的 historical entry 記錄 tutorial diagram schema 已由 deprecated `relPath`／`url`、`title` 遷移至 `imagePath`、`caption`。Current fixture 已使用 `imagePath` 與 `caption`，不應倒退修改這兩個 key。
- Lupin diary 最近 20 筆沒有與本 fixture 直接相關的決策；未將一般 telemetry 提升為 authority。

## 分析與重要差異

### 四個目前可見的 errors

三個 diagram 都引用 Brenner／KDIGO authoritative image。依 current `TutorialDiagram` union 以及 repo 內 current tutorial fixtures/data 的慣例，這些 diagram 應標為：

```ts
type: 'micrograph'
```

第二個 module 沒有 standalone diagrams，但 `TutorialModule.diagrams` 是必填 array；應使用空 array 表達「本 module 沒有 standalone diagram」：

```ts
diagrams: []
```

不建議把 `TutorialModule.diagrams` 改成 optional，因為錯誤只在 stale test fixture；production contract 與 current data 都已使用明確 array。

### 修完四項後會出現的 latent mismatch

`mockTutorial` 本身仍缺少 `ExamTutorial` 的三個 required fields：`id`、`sourceCategory`、`updatedAt`。目前 TypeScript 先回報 nested object incompatibilities；若只處理畫面上的四項，下一次 typecheck 預期會再揭露頂層錯誤。

因此這次 fixture 修正應一次補齊這三個欄位，使用 deterministic literals，不使用 `new Date()`：

```ts
id: 'tutorial_demo',
sourceCategory: 'test',
updatedAt: '2026-08-04T00:00:00.000Z',
```

`id` 與 `paperId` 在此 fixture 可以同值；現有 assertions 只依 `paperId` 驗證 `onStartExam('tutorial_demo')`，不需要改測試行為。

## 建議的 specification

`mockTutorial` 應保持 `ExamTutorial` annotation，並做以下 exact contract alignment：

1. 在 tutorial 頂層補入：
   - `id: 'tutorial_demo'`
   - `sourceCategory: 'test'`
   - `updatedAt: '2026-08-04T00:00:00.000Z'`
2. 在 line 20、32、38 所在的三個 diagram object 各補入：
   - `type: 'micrograph'`
3. 在第二個 module（`mod_2`）補入：
   - `diagrams: []`
4. 不修改 `src/types/exam.ts`，不把 required properties 改 optional。
5. 不排除 tests 於 `tsconfig.json`，避免以跳過檢查掩蓋 fixture drift。
6. 不改 `imagePath`、`caption`、keyboard tests、UI assertions 或 production component behavior。

建議完成後的相關 fixture shape：

```ts
const mockTutorial: ExamTutorial = {
  id: 'tutorial_demo',
  paperId: 'tutorial_demo',
  title: 'Nephrology Study Tutorial',
  sourceCategory: 'test',
  year: 2026,
  updatedAt: '2026-08-04T00:00:00.000Z',
  modules: [
    {
      moduleId: 'mod_1',
      moduleTitle: 'Module 1: Electrolytes',
      studyGuide: 'Focus on sodium and potassium disorders.',
      sections: [
        {
          heading: 'Section 1.1 Hyponatremia',
          content: 'Hyponatremia is defined as serum sodium < 135 mEq/L.',
          diagram: {
            id: 'diag_1',
            type: 'micrograph',
            sourceBook: 'Brenner 11e',
            imagePath: '/reference-images/Brenner_Fig_1.png',
            caption: 'Hyponatremia algorithm',
          },
          items: [{ term: 'Euvolemic', description: 'SIADH, Hypothyroidism' }],
        },
      ],
      diagrams: [
        {
          id: 'diag_standalone_1',
          type: 'micrograph',
          sourceBook: 'KDIGO 2024',
          imagePath: '/reference-images/KDIGO_Fig_1.png',
          caption: 'KDIGO Overview Figure 1',
        },
        {
          id: 'diag_standalone_2',
          type: 'micrograph',
          sourceBook: 'KDIGO 2024',
          imagePath: '/reference-images/KDIGO_Fig_2.png',
          caption: 'KDIGO Overview Figure 2',
        },
      ],
    },
    {
      moduleId: 'mod_2',
      moduleTitle: 'Module 2: Glomerular Diseases',
      studyGuide: 'Focus on nephrotic vs nephritic syndromes.',
      diagrams: [],
      sections: [
        {
          heading: 'Section 2.1 IgA Nephropathy',
          content: 'IgA nephropathy is the most common primary glomerulonephritis.',
        },
      ],
    },
  ],
};
```

若後續另有 implementation authorization，最低驗證範圍應為：

- `./node_modules/.bin/tsc --noEmit --pretty false`
- `npm test -- src/components/__tests__/TutorialReaderView.test.tsx`
- `npm run build`

最後一項才可確認 production build blocker 已實際解除；本次 `$lu-spec` 未執行 target modification 或 production build。

## Yuan 已確認的 requirements 與 decisions

- 調查對象是指定 session 所述的 `TutorialReaderView.test.tsx` test fixture errors。
- 目標是確認這些問題應如何修改。
- 本輪 explicit invoke `$lu-spec`，因此 target files 保持 read-only，只建立本 task 的 `codex-spec` report。

## Unresolved decisions

無。Current type contract、fixture intent 與修正值已足以決定修改內容。

## Current authorization 與 out-of-scope actions

- 已授權：read-only 調查、歷史回查，以及建立本 `codex-spec` report。
- 未授權：修改 `TutorialReaderView.test.tsx`、修改 production types/components、建立 branch/worktree、執行 implementation、save、formal review、commit、push 或 deploy。
- 本報告是 plain working artifact，不構成 implementation authorization、approval state 或 execution gate。

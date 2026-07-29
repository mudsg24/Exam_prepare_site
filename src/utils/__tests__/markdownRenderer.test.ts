import { describe, it, expect } from 'vitest';
import { preprocessDecisionTrees, renderFormattedMarkdownToHTML } from '../markdownRenderer';

describe('markdownRenderer & decision tree auto-detection', () => {
  it('should auto-detect unfenced ASCII decision tree lines and wrap them in decision-tree block', () => {
    const rawMarkdown = `
### Pathophysiological Decision Trees

Primary Aldosteronism Diagnostic Protocol
  └─► Positive ARR & Confirmatory Suppression Test
        └─► Perform Adrenal Vein Sampling (AVS) with Cosyntropin Stimulation
              ├─► Post-ACTH A/C Ratio Lateralization >= 4:1 ──► Unilateral APA ──► Adrenalectomy
              └─► Post-ACTH A/C Ratio Lateralization < 4:1 ──► Bilateral BAH ──► MRA (Spironolactone)
`;

    const preprocessed = preprocessDecisionTrees(rawMarkdown);
    expect(preprocessed).toContain('```decision-tree');
    expect(preprocessed).toContain('Primary Aldosteronism Diagnostic Protocol');
    expect(preprocessed).toContain('└─► Positive ARR & Confirmatory Suppression Test');
  });

  it('should render HTML with custom decision tree flowchart card', () => {
    const rawMarkdown = `
Primary Aldosteronism Diagnostic Protocol
  └─► Positive ARR & Confirmatory Suppression Test
        └─► Perform Adrenal Vein Sampling (AVS) with Cosyntropin Stimulation
`;

    const html = renderFormattedMarkdownToHTML(rawMarkdown);
    expect(html).toContain('Pathophysiological Decision Tree / Clinical Flowchart');
    expect(html).toContain('overflow-x-auto');
    expect(html).toContain('Positive ARR &amp; Confirmatory Suppression Test');
  });
});

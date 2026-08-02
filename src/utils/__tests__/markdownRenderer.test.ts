import { describe, it, expect, vi } from 'vitest';
import { marked } from 'marked';
import {
  preprocessDecisionTrees,
  renderFormattedMarkdownToHTML,
} from '../markdownRenderer';

describe('markdownRenderer', () => {
  describe('preprocessDecisionTrees', () => {
    it('returns empty string for falsy input', () => {
      expect(preprocessDecisionTrees('')).toBe('');
    });

    it('wraps unfenced decision tree lines in decision-tree code fence', () => {
      const input = `Clinical Approach
Title of Tree
└─► Step 1: Check Sodium
├─► Step 2: Check Osmolality
Treatment Protocol`;

      const processed = preprocessDecisionTrees(input);
      expect(processed).toContain('```decision-tree');
      expect(processed).toContain('└─► Step 1: Check Sodium');
      expect(processed).toContain('Treatment Protocol');
    });

    it('preserves existing code blocks without double fencing', () => {
      const input = `\`\`\`js
console.log('hello');
\`\`\``;
      const processed = preprocessDecisionTrees(input);
      expect(processed).toBe(input);
    });

    it('flushes pending tree block when encountering a fence or end of text', () => {
      const input = `Title Line
└─► Step A
\`\`\`js
test
\`\`\``;
      const processed = preprocessDecisionTrees(input);
      expect(processed).toContain('```decision-tree');
      expect(processed).toContain('└─► Step A');
      expect(processed).toContain('```js');
    });
  });

  describe('renderFormattedMarkdownToHTML', () => {
    it('returns empty string when rawText is falsy', () => {
      expect(renderFormattedMarkdownToHTML('')).toBe('');
    });

    it('renders normal markdown text into styled HTML', () => {
      const html = renderFormattedMarkdownToHTML('### Header 3\nThis is **bold** text.');
      expect(html).toContain('<h3');
      expect(html).toContain('<strong>bold</strong>');
    });

    it('renders decision tree blocks into custom HTML visual cards', () => {
      const input = `\`\`\`decision-tree
┌─► Hyponatremia
└─► Euvolemic
\`\`\``;
      const html = renderFormattedMarkdownToHTML(input);
      expect(html).toContain('Pathophysiological Decision Tree / Clinical Flowchart');
      expect(html).toContain('┌─► Hyponatremia');
    });

    it('renders standard code blocks into pre container', () => {
      const input = `\`\`\`ts
const x = 10;
\`\`\``;
      const html = renderFormattedMarkdownToHTML(input);
      expect(html).toContain('<pre class="font-mono text-xs md:text-sm text-slate-200');
    });

    it('handles marked.parse throwing an exception via try/catch fallback', () => {
      const spy = vi.spyOn(marked, 'parse').mockImplementationOnce(() => {
        throw new Error('Markdown parse error');
      });

      const spyConsole = vi.spyOn(console, 'error').mockImplementation(() => {});

      const result = renderFormattedMarkdownToHTML('some text');
      expect(result).toBe('some text');
      expect(spyConsole).toHaveBeenCalled();

      spy.mockRestore();
      spyConsole.mockRestore();
    });
  });
});

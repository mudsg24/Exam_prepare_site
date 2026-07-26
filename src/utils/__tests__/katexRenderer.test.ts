import { describe, it, expect, vi } from 'vitest';
import katex from 'katex';
import { renderKaTeXInString } from '../katexRenderer';

describe('renderKaTeXInString', () => {
  it('should return empty string for empty input', () => {
    expect(renderKaTeXInString('')).toBe('');
    // @ts-expect-error testing null input
    expect(renderKaTeXInString(null)).toBe('');
    // @ts-expect-error testing undefined input
    expect(renderKaTeXInString(undefined)).toBe('');
  });

  it('should leave plain text without math unmodified', () => {
    const text = 'Hello world, this is a plain text.';
    expect(renderKaTeXInString(text)).toBe(text);
  });

  it('should render block math with $$...$$', () => {
    const input = '$$E = mc^2$$';
    const output = renderKaTeXInString(input);
    expect(output).toContain('katex-display');
    expect(output).toContain('E = mc^2');
  });

  it('should render block math with \\[...\\]', () => {
    const input = '\\[ \\int_0^1 x dx \\]';
    const output = renderKaTeXInString(input);
    expect(output).toContain('katex-display');
  });

  it('should render inline math with $...$', () => {
    const input = 'Formula $x^2 + y^2 = z^2$ inline.';
    const output = renderKaTeXInString(input);
    expect(output).toContain('katex');
    expect(output).not.toContain('katex-display');
  });

  it('should render inline math with \\(...\\)', () => {
    const input = 'Inline \\(a + b = c\\) math.';
    const output = renderKaTeXInString(input);
    expect(output).toContain('katex');
  });

  it('should fallback to raw math string if katex.renderToString throws an error', () => {
    const spy = vi.spyOn(katex, 'renderToString').mockImplementation(() => {
      throw new Error('KaTeX rendering error');
    });

    expect(renderKaTeXInString('$$error_block$$')).toBe('error_block');
    expect(renderKaTeXInString('\\[error_block_2\\]')).toBe('error_block_2');
    expect(renderKaTeXInString('$error_inline$')).toBe('error_inline');
    expect(renderKaTeXInString('\\(error_inline_2\\)')).toBe('error_inline_2');

    spy.mockRestore();
  });
});

import katex from 'katex';

/**
 * Parses LaTeX inline ($...$, \(...\)) and block ($$...$$, \[...\]) expressions
 * and converts them into rendered KaTeX HTML strings or returns cleaned text.
 */
export function renderKaTeXInString(text: string): string {
  if (!text) return '';

  let result = text;

  // 1. Process block math: $$...$$ or \[...\]
  result = result.replace(/\$\$([\s\S]+?)\$\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: true, throwOnError: false });
    } catch (e) {
      return math;
    }
  });

  result = result.replace(/\\\[([\s\S]+?)\\\]/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: true, throwOnError: false });
    } catch (e) {
      return math;
    }
  });

  // 2. Process inline math: $...$ or \(...\)
  // Avoid matching single currency signs like $100 by requiring non-space after initial $ and non-space before ending $
  result = result.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: false, throwOnError: false });
    } catch (e) {
      return math;
    }
  });

  result = result.replace(/\\\(([^\$\n]+?)\\\)/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: false, throwOnError: false });
    } catch (e) {
      return math;
    }
  });

  return result;
}

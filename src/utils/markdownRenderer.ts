import { marked } from 'marked';
import { renderKaTeXInString } from './katexRenderer';

/**
 * Pre-processes text to detect ASCII decision trees / flowcharts that lack code fences.
 * Wraps unfenced tree blocks in ```decision-tree ... ``` blocks to preserve line breaks,
 * indentation, and monospace tree structure.
 */
export function preprocessDecisionTrees(rawText: string): string {
  if (!rawText) return '';

  const lines = rawText.split('\n');
  const result: string[] = [];
  let inCodeBlock = false;
  let currentTreeBlock: string[] = [];

  const isTreeLine = (line: string): boolean => {
    return (
      line.includes('└─►') ||
      line.includes('├─►') ||
      line.includes('──►') ||
      line.includes('┌─►') ||
      line.includes('│') ||
      line.includes('└──') ||
      line.includes('├──') ||
      line.includes('-->')
    );
  };

  const isHeadingOrFence = (line: string): boolean => {
    const trimmed = line.trim();
    return trimmed.startsWith('#') || trimmed.startsWith('```') || trimmed.startsWith('---') || trimmed.startsWith('|');
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    if (trimmed.startsWith('```')) {
      // Flush any pending tree block before starting a new fence
      if (currentTreeBlock.length > 0) {
        result.push('```decision-tree');
        result.push(...currentTreeBlock);
        result.push('```');
        currentTreeBlock = [];
      }
      inCodeBlock = !inCodeBlock;
      result.push(line);
      continue;
    }

    if (inCodeBlock) {
      result.push(line);
      continue;
    }

    if (isTreeLine(line)) {
      // If we just started a new tree block and the immediately preceding line in result is a non-empty title line (and not a heading/fence/empty),
      // pull that title line into the tree block!
      if (currentTreeBlock.length === 0 && result.length > 0) {
        const lastResultLine = result[result.length - 1];
        if (lastResultLine && lastResultLine.trim().length > 0 && !isHeadingOrFence(lastResultLine)) {
          // Check if there was a line before lastResultLine that was empty or heading
          const prevResultLine = result.length > 1 ? result[result.length - 2] : '';
          if (prevResultLine === '' || prevResultLine.trim().startsWith('#') || prevResultLine.trim().startsWith('---')) {
            result.pop(); // remove title line from result
            currentTreeBlock.push(lastResultLine); // move title line into tree block
          }
        }
      }
      currentTreeBlock.push(line);
    } else {
      // If line is empty or part of the tree title/subtitle block following a tree line (e.g. Treatment Protocol)
      if (currentTreeBlock.length > 0) {
        if (
          trimmed.length > 0 &&
          !isHeadingOrFence(line) &&
          (trimmed.toLowerCase().includes('protocol') ||
            trimmed.toLowerCase().includes('treatment') ||
            trimmed.toLowerCase().includes('pathophysiology') ||
            trimmed.toLowerCase().includes('management') ||
            trimmed.toLowerCase().includes('diagnosis'))
        ) {
          currentTreeBlock.push(line);
        } else {
          // End of decision tree block
          result.push('```decision-tree');
          result.push(...currentTreeBlock);
          result.push('```');
          currentTreeBlock = [];
          result.push(line);
        }
      } else {
        result.push(line);
      }
    }
  }

  if (currentTreeBlock.length > 0) {
    result.push('```decision-tree');
    result.push(...currentTreeBlock);
    result.push('```');
  }

  return result.join('\n');
}

/**
 * Custom marked renderer instance tailored for medical exam site.
 * Renders decision tree blocks with interactive visual cards and horizontal scrolling.
 */
const customRenderer = new marked.Renderer();

customRenderer.code = ({ text, lang }: { text: string; lang?: string }) => {
  const isTree =
    lang === 'decision-tree' ||
    text.includes('└─►') ||
    text.includes('├─►') ||
    text.includes('──►') ||
    text.includes('┌─►') ||
    text.includes('│');

  if (isTree) {
    // Escape HTML inside code block to prevent injection
    const safeText = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    return `<div class="my-5 rounded-2xl border border-sky-500/30 dark:border-sky-500/40 bg-slate-900 shadow-lg overflow-hidden transition-all">
      <div class="px-4 py-2.5 bg-slate-950 border-b border-slate-800 flex items-center justify-between text-xs font-mono font-bold text-sky-400">
        <span class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
          <span>Pathophysiological Decision Tree / Clinical Flowchart</span>
        </span>
        <span class="text-[10px] text-slate-400 font-sans bg-slate-900 px-2 py-0.5 rounded border border-slate-800">
          ↔ 可橫向滾動檢視 (Scroll Horizontally)
        </span>
      </div>
      <div class="p-4 md:p-5 overflow-x-auto scrollbar-thin">
        <pre class="font-mono text-xs md:text-sm text-slate-100 leading-relaxed whitespace-pre font-medium tracking-wide selection:bg-sky-500 selection:text-white">${safeText}</pre>
      </div>
    </div>`;
  }

  const safeText = text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

  return `<div class="my-4 rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
    <div class="p-4 overflow-x-auto">
      <pre class="font-mono text-xs md:text-sm text-slate-200 leading-relaxed whitespace-pre">${safeText}</pre>
    </div>
  </div>`;
};

/**
 * Renders raw markdown into styled HTML with KaTeX math rendering and decision tree diagram auto-formatting.
 */
export function renderFormattedMarkdownToHTML(rawText: string): string {
  if (!rawText) return '';
  const preprocessed = preprocessDecisionTrees(rawText);
  const mathRendered = renderKaTeXInString(preprocessed);

  try {
    return marked.parse(mathRendered, {
      async: false,
      renderer: customRenderer,
    }) as string;
  } catch (e) {
    console.error('Failed to parse markdown:', e);
    return mathRendered;
  }
}

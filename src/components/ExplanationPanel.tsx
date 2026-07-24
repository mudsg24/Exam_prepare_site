import React, { useState } from 'react';
import { BookOpen, Image as ImageIcon, CheckCircle, AlertTriangle, Sparkles, FileText } from 'lucide-react';
import { marked } from 'marked';
import { ExamQuestion, ResolvedImage, ThemeMode } from '../types/exam';
import { renderKaTeXInString } from '../utils/katexRenderer';

interface ExplanationPanelProps {
  question: ExamQuestion;
  onOpenImage: (image: ResolvedImage) => void;
  themeMode?: ThemeMode;
}

function cleanNlmResponseText(raw: string): string {
  if (!raw) return '';
  let cleaned = raw;
  if (cleaned.includes('AskResult(') && cleaned.includes('answer=')) {
    const m = cleaned.match(/answer=["']([\s\S]*?)["']\s*,\s*(?:conversation_id|turn_number|raw_response)=/);
    if (m) {
      cleaned = m[1];
    }
  }
  cleaned = cleaned.replace(/\\n/g, '\n').replace(/\\"/g, '"');
  return cleaned.trim();
}

function renderFormattedMarkdown(rawText: string, isLight: boolean) {
  if (!rawText) return null;
  const cleaned = cleanNlmResponseText(rawText);
  // Render LaTeX math expressions first
  const mathRendered = renderKaTeXInString(cleaned);

  try {
    const html = marked.parse(mathRendered, { async: false }) as string;
    return (
      <div
        className={`prose max-w-none text-[15px] leading-relaxed space-y-4 font-sans selection:bg-sky-500 selection:text-white ${
          isLight ? 'text-slate-800' : 'text-slate-200 prose-invert'
        }`}
        dangerouslySetInnerHTML={{ __html: html }}
      />
    );
  } catch (e) {
    return (
      <div
        className={`whitespace-pre-line text-[15px] leading-relaxed ${
          isLight ? 'text-slate-800' : 'text-slate-200'
        }`}
        dangerouslySetInnerHTML={{ __html: mathRendered }}
      />
    );
  }
}

export const ExplanationPanel: React.FC<ExplanationPanelProps> = ({
  question,
  onOpenImage,
  themeMode = 'light',
}) => {
  const [activeNlmTab, setActiveNlmTab] = useState<number>(0);
  const isLight = themeMode === 'light';

  const hasSourceAnswer = question.sourceAnswerStatus === 'provided' && question.sourceProvidedAnswer;
  const nlmResponses = question.nlmResponses || [];

  return (
    <div
      className={`glass-panel border rounded-2xl p-6 md:p-8 shadow-md mt-6 space-y-6 transition-colors ${
        isLight ? 'bg-white border-slate-200 text-slate-900' : 'bg-slate-900/90 border-slate-800 text-slate-100'
      }`}
    >
      {/* Panel Header */}
      <div className="flex items-center justify-between pb-4 border-b border-slate-200 dark:border-slate-800">
        <div className="flex items-center gap-3">
          <span className="p-2.5 rounded-xl bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border border-indigo-500/20">
            <Sparkles className="w-5 h-5" />
          </span>
          <div>
            <h3 className={`text-base font-bold ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
              試題正解與雙重 NotebookLM 權威對比解析
            </h3>
            <p className="text-xs text-slate-500">含 KDIGO / Brenner 11e 權威考點出處與圖表對照</p>
          </div>
        </div>
      </div>

      {/* 1. Ground Truth Summary Banner */}
      <div
        className={`p-4 md:p-5 rounded-2xl border flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 ${
          isLight ? 'bg-slate-50 border-slate-200' : 'bg-slate-950 border-slate-800'
        }`}
      >
        <div className="flex items-center gap-3.5">
          <span className="w-10 h-10 rounded-xl bg-emerald-500/15 text-emerald-700 dark:text-emerald-400 border border-emerald-500/30 flex items-center justify-center font-bold font-mono text-lg shrink-0">
            {hasSourceAnswer ? question.sourceProvidedAnswer : '?'}
          </span>
          <div>
            <div className="text-xs font-semibold text-slate-500">原始考題標示解答</div>
            <div className={`text-base font-bold ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
              {hasSourceAnswer ? `答案選項 (${question.sourceProvidedAnswer})` : '原始檔案未標記解答 (無 Ground Truth)'}
            </div>
          </div>
        </div>

        {/* Dispute Status Note */}
        {question.reconciliationNotes && (
          <div className="text-xs font-medium text-amber-700 dark:text-amber-300 bg-amber-500/10 border border-amber-500/20 px-3.5 py-2 rounded-xl max-w-lg">
            {question.reconciliationNotes}
          </div>
        )}
      </div>

      {/* 2. Dual NotebookLM Response Tabs & Section */}
      {nlmResponses.length > 0 ? (
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <h4 className={`text-sm font-bold flex items-center gap-2 ${isLight ? 'text-slate-800' : 'text-slate-200'}`}>
              <BookOpen className="w-4 h-4 text-sky-500" />
              <span>NotebookLM 雙重 AI 權威比對 ({nlmResponses.length} 次提問結果)</span>
            </h4>

            {/* NLM Tabs Selector */}
            <div
              className={`flex items-center rounded-xl border p-1 text-xs font-mono ${
                isLight ? 'bg-slate-100 border-slate-200' : 'bg-slate-950 border-slate-800'
              }`}
            >
              {nlmResponses.map((res, idx) => (
                <button
                  key={idx}
                  onClick={() => setActiveNlmTab(idx)}
                  className={`px-3 py-1.5 rounded-lg transition-all cursor-pointer ${
                    activeNlmTab === idx
                      ? 'bg-sky-600 text-white font-bold shadow-xs'
                      : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'
                  }`}
                >
                  {res.notebookTitle || `Notebook #${idx + 1}`} (NLM選 {res.selectedOption || '無'})
                </button>
              ))}
            </div>
          </div>

          {/* Active NLM Formatted Card */}
          {nlmResponses[activeNlmTab] && (
            <div
              className={`p-5 md:p-6 rounded-2xl border space-y-4 ${
                isLight ? 'bg-white border-slate-200 shadow-sm' : 'bg-slate-950/80 border-slate-800'
              }`}
            >
              {/* Header Info */}
              <div className="flex items-center justify-between text-xs pb-3 border-b border-slate-200 dark:border-slate-800">
                <span className="text-slate-500 font-mono">
                  知識庫來源: <strong className={isLight ? 'text-slate-800' : 'text-slate-200'}>{nlmResponses[activeNlmTab].notebookTitle}</strong> ({nlmResponses[activeNlmTab].accountProfile})
                </span>
                <span className="px-2.5 py-1 rounded-lg bg-sky-500/10 text-sky-700 dark:text-sky-300 font-mono font-bold border border-sky-500/20">
                  NLM 判定答案: <strong>{nlmResponses[activeNlmTab].selectedOption || 'N/A'}</strong>
                </span>
              </div>

              {/* Rationale Content with KaTeX */}
              <div
                className={`p-5 rounded-2xl border leading-relaxed ${
                  isLight ? 'bg-slate-50/80 border-slate-200' : 'bg-slate-950 border-slate-800'
                }`}
              >
                {renderFormattedMarkdown(nlmResponses[activeNlmTab].rawResponse, isLight)}
              </div>

              {/* Citations List */}
              {nlmResponses[activeNlmTab].citations?.length > 0 && (
                <div className="pt-2">
                  <div className="text-xs font-semibold text-slate-500 mb-1.5">對應教科書與章節引用:</div>
                  <div className="flex flex-wrap gap-2">
                    {nlmResponses[activeNlmTab].citations.map((c, cIdx) => (
                      <span
                        key={cIdx}
                        className={`px-2.5 py-1 rounded-lg border text-xs font-mono ${
                          isLight ? 'bg-slate-100 text-slate-700 border-slate-200' : 'bg-slate-900 text-slate-300 border-slate-800'
                        }`}
                      >
                        📖 {c.chapter} {c.page ? `pg.${c.page}` : ''}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      ) : (
        <div
          className={`p-6 rounded-2xl border text-xs text-slate-500 text-center ${
            isLight ? 'bg-slate-50 border-slate-200' : 'bg-slate-950 border-slate-800'
          }`}
        >
          尚無 NotebookLM 的回答資料
        </div>
      )}

      {/* 3. Resolved Reference Images (KDIGO & Brenner 11e) */}
      {question.resolvedImages && question.resolvedImages.length > 0 && (
        <div className="pt-4 border-t border-slate-200 dark:border-slate-800">
          <h4 className={`text-sm font-bold mb-3 flex items-center gap-2 ${isLight ? 'text-slate-800' : 'text-slate-200'}`}>
            <ImageIcon className="w-4 h-4 text-sky-500" />
            <span>對應權威圖表資料 ({question.resolvedImages.length} 張)</span>
          </h4>

          <div className="grid grid-cols-2 sm:grid-cols-3 gap-4">
            {question.resolvedImages.map((img) => (
              <button
                key={img.id}
                onClick={() => onOpenImage(img)}
                className={`group p-2.5 rounded-2xl border text-left flex flex-col justify-between overflow-hidden transition-all cursor-pointer ${
                  isLight
                    ? 'bg-white border-slate-200 hover:border-sky-300 hover:shadow-md'
                    : 'bg-slate-950 border-slate-800 hover:border-sky-500/30'
                }`}
              >
                <div className="h-32 w-full rounded-xl bg-slate-950 overflow-hidden mb-2 border border-slate-800 flex items-center justify-center">
                  <img
                    src={img.relPath}
                    alt={img.title}
                    className="max-h-full max-w-full object-contain group-hover:scale-105 transition-transform"
                  />
                </div>
                <div className="px-1">
                  <div className={`text-xs font-semibold truncate ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
                    {img.title}
                  </div>
                  <div className="text-[11px] text-sky-600 dark:text-sky-400 font-mono">{img.bookSource}</div>
                </div>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

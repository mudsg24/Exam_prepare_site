import React, { useState } from 'react';
import { BookOpen, Image as ImageIcon, CheckCircle, AlertTriangle, FileText, Sparkles } from 'lucide-react';
import { marked } from 'marked';
import { ExamQuestion, ResolvedImage } from '../types/exam';

interface ExplanationPanelProps {
  question: ExamQuestion;
  onOpenImage: (image: ResolvedImage) => void;
}

function cleanNlmResponseText(raw: string): string {
  if (!raw) return '';
  let cleaned = raw;
  // If wrapped in AskResult(...)
  if (cleaned.includes('AskResult(') && cleaned.includes('answer=')) {
    const m = cleaned.match(/answer=["']([\s\S]*?)["']\s*,\s*(?:conversation_id|turn_number|raw_response)=/);
    if (m) {
      cleaned = m[1];
    }
  }
  // Replace escaped \n with actual newlines
  cleaned = cleaned.replace(/\\n/g, '\n').replace(/\\"/g, '"');
  return cleaned.trim();
}

function renderMarkdownContent(content: string) {
  if (!content) return null;
  const cleaned = cleanNlmResponseText(content);
  try {
    const html = marked.parse(cleaned, { async: false }) as string;
    return (
      <div
        className="prose prose-invert max-w-none text-xs text-slate-200 leading-relaxed space-y-3 font-sans selection:bg-cyan-500 selection:text-slate-950"
        dangerouslySetInnerHTML={{ __html: html }}
      />
    );
  } catch (e) {
    return <div className="whitespace-pre-line text-xs text-slate-300">{cleaned}</div>;
  }
}

export const ExplanationPanel: React.FC<ExplanationPanelProps> = ({ question, onOpenImage }) => {
  const [activeNlmTab, setActiveNlmTab] = useState<number>(0);

  const hasSourceAnswer = question.sourceAnswerStatus === 'provided' && question.sourceProvidedAnswer;
  const nlmResponses = question.nlmResponses || [];

  return (
    <div className="glass-panel border border-slate-800/80 rounded-2xl p-6 shadow-xl mt-6 space-y-6">
      {/* Panel Title Header */}
      <div className="flex items-center justify-between pb-3 border-b border-slate-800">
        <div className="flex items-center gap-2.5">
          <span className="p-2 rounded-lg bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
            <Sparkles className="w-4 h-4" />
          </span>
          <div>
            <h3 className="text-sm font-bold text-slate-100">試題解答與雙重 NotebookLM 解析</h3>
            <p className="text-xs text-slate-400">含 KDIGO / Brenner 11e 權威圖表與出處對比</p>
          </div>
        </div>
      </div>

      {/* 1. Original Answer Summary Card */}
      <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <span className="w-8 h-8 rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 flex items-center justify-center font-bold font-mono text-sm">
            {hasSourceAnswer ? question.sourceProvidedAnswer : '?'}
          </span>
          <div>
            <div className="text-xs text-slate-400">原始考題給予答案</div>
            <div className="text-sm font-semibold text-slate-100">
              {hasSourceAnswer ? `答案選項 (${question.sourceProvidedAnswer})` : '原始檔案未標記解答 (無 Ground Truth)'}
            </div>
          </div>
        </div>

        {/* Dispute Summary Note */}
        {question.reconciliationNotes && (
          <div className="text-xs text-amber-300/90 bg-amber-500/10 border border-amber-500/20 px-3 py-1.5 rounded-lg max-w-md">
            {question.reconciliationNotes}
          </div>
        )}
      </div>

      {/* 2. Dual NotebookLM Response Section */}
      {nlmResponses.length > 0 ? (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h4 className="text-xs font-semibold text-slate-300 flex items-center gap-2">
              <BookOpen className="w-3.5 h-3.5 text-cyan-400" />
              <span>NotebookLM 雙重權威對比 ({nlmResponses.length} 次提問結果)</span>
            </h4>

            {/* NLM Tabs Selector */}
            <div className="flex items-center rounded-lg bg-slate-900 border border-slate-800 p-0.5 text-xs font-mono">
              {nlmResponses.map((res, idx) => (
                <button
                  key={idx}
                  onClick={() => setActiveNlmTab(idx)}
                  className={`px-3 py-1 rounded-md transition-colors ${
                    activeNlmTab === idx
                      ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-semibold'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {res.notebookTitle || `Notebook #${idx + 1}`} ({res.selectedOption || '無答'})
                </button>
              ))}
            </div>
          </div>

          {/* Active NLM Card */}
          {nlmResponses[activeNlmTab] && (
            <div className="p-4 rounded-xl glass-card space-y-3">
              <div className="flex items-center justify-between text-xs pb-2 border-b border-slate-800/80">
                <span className="text-slate-400 font-mono">
                  知識庫來源: <strong className="text-slate-200">{nlmResponses[activeNlmTab].notebookTitle}</strong> ({nlmResponses[activeNlmTab].accountProfile})
                </span>
                <span className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">
                  NLM 選擇: <strong className="text-cyan-400 font-bold">{nlmResponses[activeNlmTab].selectedOption || 'N/A'}</strong>
                </span>
              </div>

              {/* Detailed Formatted Explanation */}
              <div className="bg-slate-950/60 p-4 rounded-xl border border-slate-800/80">
                {renderMarkdownContent(nlmResponses[activeNlmTab].rawResponse)}
              </div>


              {/* Citations List */}
              {nlmResponses[activeNlmTab].citations?.length > 0 && (
                <div className="pt-2">
                  <div className="text-[11px] font-semibold text-slate-400 mb-1">對應章節引用:</div>
                  <div className="flex flex-wrap gap-1.5">
                    {nlmResponses[activeNlmTab].citations.map((c, cIdx) => (
                      <span
                        key={cIdx}
                        className="px-2 py-0.5 rounded bg-slate-900 text-slate-300 border border-slate-800 text-[11px] font-mono"
                      >
                        {c.chapter} {c.page ? `pg.${c.page}` : ''}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      ) : (
        <div className="p-4 rounded-xl bg-slate-900/50 border border-slate-800 text-xs text-slate-400 text-center">
          尚無 NotebookLM 的回答資料 (等待 /tn-exam-prepare 進行提問)
        </div>
      )}

      {/* 3. Resolved Reference Images (KDIGO & Brenner 11e) */}
      {question.resolvedImages && question.resolvedImages.length > 0 && (
        <div className="pt-2 border-t border-slate-800/80">
          <h4 className="text-xs font-semibold text-slate-300 mb-3 flex items-center gap-2">
            <ImageIcon className="w-3.5 h-3.5 text-cyan-400" />
            <span>對應參考圖表資料 ({question.resolvedImages.length} 張)</span>
          </h4>

          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {question.resolvedImages.map((img) => (
              <button
                key={img.id}
                onClick={() => onOpenImage(img)}
                className="group p-2 rounded-xl glass-card glass-card-hover text-left flex flex-col justify-between overflow-hidden"
              >
                <div className="h-28 w-full rounded-lg bg-slate-950 overflow-hidden mb-2 border border-slate-800 flex items-center justify-center">
                  <img
                    src={img.relPath}
                    alt={img.title}
                    className="max-h-full max-w-full object-contain group-hover:scale-105 transition-transform"
                  />
                </div>
                <div className="px-1">
                  <div className="text-xs font-medium text-slate-200 truncate">{img.title}</div>
                  <div className="text-[10px] text-cyan-400 font-mono">{img.bookSource}</div>
                </div>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

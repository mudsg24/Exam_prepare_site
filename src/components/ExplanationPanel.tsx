import React, { useState } from 'react';
import { BookOpen, Image as ImageIcon, CheckCircle, AlertTriangle, Sparkles, FileText, ChevronDown, ChevronRight } from 'lucide-react';
import { renderFormattedMarkdownToHTML } from '../utils/markdownRenderer';
import { ExamQuestion, ResolvedImage, ThemeMode } from '../types/exam';

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
  const html = renderFormattedMarkdownToHTML(cleaned);

  return (
    <div
      className={`prose max-w-none text-[15px] leading-relaxed space-y-4 font-sans selection:bg-sky-500 selection:text-white ${
        isLight ? 'text-slate-800' : 'text-slate-200 prose-invert'
      }`}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}

interface NlmSection {
  title: string;
  content: string;
}

function parseNlmSections(rawText: string): NlmSection[] {
  const cleaned = cleanNlmResponseText(rawText);
  if (!cleaned) return [];

  const lines = cleaned.split('\n');
  const sections: NlmSection[] = [];
  let currentTitle = '解析摘要 Overview';
  let currentLines: string[] = [];

  for (const line of lines) {
    const headerMatch = line.match(/^#{2,3}\s+\*?\*?(.*?)\*?\*?$/);
    if (headerMatch && headerMatch[1].trim()) {
      if (currentLines.length > 0) {
        const body = currentLines.join('\n').trim();
        if (body) {
          sections.push({ title: currentTitle, content: body });
        }
      }
      currentTitle = headerMatch[1].replace(/\*/g, '').trim();
      currentLines = [];
    } else {
      currentLines.push(line);
    }
  }

  if (currentLines.length > 0) {
    const body = currentLines.join('\n').trim();
    if (body) {
      sections.push({ title: currentTitle, content: body });
    }
  }

  return sections;
}

export const ExplanationPanel: React.FC<ExplanationPanelProps> = ({
  question,
  onOpenImage,
  themeMode = 'light',
}) => {
  const [activeNlmTab, setActiveNlmTab] = useState<number>(0);
  const [openSections, setOpenSections] = useState<Record<string, boolean>>({});

  const toggleSection = (key: string) => {
    setOpenSections((prev) => ({ ...prev, [key]: !prev[key] }));
  };

  const isLight = themeMode === 'light';

  if (!question) return null;

  const hasSourceAnswer = (question.sourceAnswerStatus === 'provided' || question.sourceAnswerStatus === 'synthetic_tonks') && !!question.sourceProvidedAnswer;
  const isSynthetic = question.sourceAnswerStatus === 'synthetic_tonks';
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
            <div className="text-xs font-semibold text-slate-500">
              {isSynthetic ? 'Tonks 擬真命題正解' : '原始考題標示解答'}
            </div>
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

      {/* 1.4. Gemini / Source Dedicated Official Rationale Section */}
      {question.sourceExplanation && question.sourceExplanation.trim().length > 0 && (
        <div
          className={`p-5 md:p-6 rounded-2xl border space-y-4 ${
            isLight ? 'bg-sky-50/50 border-sky-200/80 shadow-xs' : 'bg-slate-950 border-sky-900/50'
          }`}
        >
          <div className="flex items-center justify-between pb-3 border-b border-sky-200/60 dark:border-sky-900/60">
            <h4 className="text-sm font-bold flex items-center gap-2 text-sky-700 dark:text-sky-300">
              <Sparkles className="w-4 h-4 text-sky-500" />
              <span>
                {isSynthetic ? '✨ Gemini 專責正式解析' : '📖 原始考題解析／出處備註'}
              </span>
            </h4>
            <span className="px-2.5 py-1 rounded-lg bg-sky-500/10 text-sky-700 dark:text-sky-300 font-mono text-xs font-semibold border border-sky-500/20">
              {isSynthetic ? 'Gemini Official Rationale' : 'Source Explanation'}
            </span>
          </div>

          <div className={`p-4 rounded-xl text-sm leading-relaxed border ${
            isLight ? 'bg-white border-sky-100 text-slate-800' : 'bg-slate-900 border-sky-950 text-slate-200'
          }`}>
            {renderFormattedMarkdown(question.sourceExplanation, isLight)}
          </div>
        </div>
      )}

      {/* 1.5. Codex Dedicated Official Rationale Section */}
      {question.codexExplanation && (
        <div
          className={`p-5 md:p-6 rounded-2xl border space-y-4 ${
            isLight ? 'bg-indigo-50/50 border-indigo-200/80 shadow-xs' : 'bg-slate-950 border-indigo-900/50'
          }`}
        >
          <div className="flex items-center justify-between pb-3 border-b border-indigo-200/60 dark:border-indigo-900/60">
            <h4 className="text-sm font-bold flex items-center gap-2 text-indigo-700 dark:text-indigo-300">
              <Sparkles className="w-4 h-4 text-indigo-500" />
              <span>🏆 腎專聯合研析組 Codex 正式解析與選項剖析</span>
            </h4>
            <span className="px-2.5 py-1 rounded-lg bg-indigo-500/10 text-indigo-700 dark:text-indigo-300 font-mono text-xs font-semibold border border-indigo-500/20">
              Codex Official Rationale
            </span>
          </div>

          {/* Explanation Text */}
          {question.codexExplanation.explanationZh && (
            <div className="space-y-2">
              <div className="text-xs font-semibold text-indigo-600 dark:text-indigo-400">【核心解析 Summary Rationale】</div>
              <div className={`p-4 rounded-xl text-sm leading-relaxed border ${
                isLight ? 'bg-white border-indigo-100 text-slate-800' : 'bg-slate-900 border-indigo-950 text-slate-200'
              }`}>
                {renderFormattedMarkdown(question.codexExplanation.explanationZh, isLight)}
              </div>
            </div>
          )}

          {/* Option Analysis Breakdown */}
          {question.codexExplanation.optionAnalysisZh && Object.keys(question.codexExplanation.optionAnalysisZh).length > 0 && (
            <div className="space-y-2">
              <div className="text-xs font-semibold text-indigo-600 dark:text-indigo-400">【選項詳細剖析 Option-by-Option Breakdown】</div>
              <div className="grid grid-cols-1 gap-2">
                {Object.entries(question.codexExplanation.optionAnalysisZh).map(([optId, analysisText]) => (
                  <div
                    key={optId}
                    className={`p-3 rounded-xl border text-xs leading-relaxed flex items-start gap-2.5 ${
                      isLight ? 'bg-white/80 border-indigo-100 text-slate-700' : 'bg-slate-900/80 border-indigo-950 text-slate-300'
                    }`}
                  >
                    <span className="px-2 py-0.5 rounded-md bg-indigo-500/15 text-indigo-700 dark:text-indigo-300 font-bold font-mono text-xs shrink-0 border border-indigo-500/20">
                      選項 ({optId})
                    </span>
                    <div className="flex-1">{renderFormattedMarkdown(analysisText, isLight)}</div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Authority Evidence & Citations */}
          {question.codexExplanation.authorityEvidence && question.codexExplanation.authorityEvidence.length > 0 && (
            <div className="pt-2">
              <div className="text-xs font-semibold text-slate-500 mb-1.5">考點權威依據 & Brenner / KDIGO 出處:</div>
              <div className="flex flex-wrap gap-2">
                {question.codexExplanation.authorityEvidence.map((ev, evIdx) => (
                  <span
                    key={evIdx}
                    className={`px-2.5 py-1 rounded-lg border text-xs font-mono ${
                      isLight ? 'bg-white text-indigo-800 border-indigo-200' : 'bg-slate-900 text-indigo-300 border-indigo-900'
                    }`}
                  >
                    📚 {ev.source} — {ev.locator} {ev.note_zh ? `(${ev.note_zh})` : ''}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      )}

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
              {nlmResponses.map((res, idx) => {
                const choice = res.extractedChoice || res.selectedOption || '無';
                const isNone = choice === 'NONE' || choice === '無';
                return (
                  <button
                    key={idx}
                    onClick={() => setActiveNlmTab(idx)}
                    className={`px-3 py-1.5 rounded-lg transition-all cursor-pointer ${
                      activeNlmTab === idx
                        ? 'bg-sky-600 text-white font-bold shadow-xs'
                        : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'
                    }`}
                  >
                    {res.notebookTitle || `Notebook #${idx + 1}`} (NLM選 {isNone ? '無' : choice})
                  </button>
                );
              })}
            </div>
          </div>

          {/* Active NLM Formatted Card */}
          {nlmResponses[activeNlmTab] && (() => {
            const currentNlm = nlmResponses[activeNlmTab];
            const currentChoice = currentNlm.extractedChoice || currentNlm.selectedOption || 'N/A';
            const parsedSections = parseNlmSections(currentNlm.formattedResponse || currentNlm.rawResponse);

            return (
              <div
                className={`p-5 md:p-6 rounded-2xl border space-y-4 ${
                  isLight ? 'bg-white border-slate-200 shadow-sm' : 'bg-slate-950/80 border-slate-800'
                }`}
              >
                {/* Header Info */}
                <div className="flex items-center justify-between text-xs pb-3 border-b border-slate-200 dark:border-slate-800">
                  <span className="text-slate-500 font-mono">
                    知識庫來源: <strong className={isLight ? 'text-slate-800' : 'text-slate-200'}>{currentNlm.notebookTitle}</strong> ({currentNlm.accountProfile})
                  </span>
                  <span className="px-2.5 py-1 rounded-lg bg-sky-500/10 text-sky-700 dark:text-sky-300 font-mono font-bold border border-sky-500/20">
                    NLM 判定答案: <strong>{currentChoice === 'NONE' ? '無 (INSUFFICIENT)' : currentChoice}</strong>
                  </span>
                </div>

                {/* Rationale Content with Accordion Sections */}
                {parsedSections.length > 1 ? (
                  <div className="space-y-3">
                    {parsedSections.map((sec, secIdx) => {
                      const secKey = `${activeNlmTab}_${secIdx}`;
                      // Default all sections to expanded/open
                      const isOpen = openSections[secKey] !== undefined ? openSections[secKey] : true;

                      return (
                        <div
                          key={secIdx}
                          className={`rounded-2xl border transition-all overflow-hidden ${
                            isLight ? 'bg-slate-50/80 border-slate-200' : 'bg-slate-950 border-slate-800'
                          }`}
                        >
                          <button
                            onClick={() => toggleSection(secKey)}
                            className={`w-full px-4 py-3 flex items-center justify-between font-bold text-sm text-left transition-colors cursor-pointer ${
                              isLight
                                ? 'bg-slate-100/70 hover:bg-slate-200/60 text-slate-800'
                                : 'bg-slate-900/60 hover:bg-slate-900 text-slate-200'
                            }`}
                          >
                            <span className="flex items-center gap-2">
                              <span className="text-sky-500 font-mono text-xs">#{secIdx + 1}</span>
                              <span>{sec.title}</span>
                            </span>
                            {isOpen ? (
                              <ChevronDown className="w-4 h-4 text-slate-400" />
                            ) : (
                              <ChevronRight className="w-4 h-4 text-slate-400" />
                            )}
                          </button>

                          {isOpen && (
                            <div className="p-4 md:p-5 border-t border-slate-200 dark:border-slate-800">
                              {renderFormattedMarkdown(sec.content, isLight)}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                ) : (
                  <div
                    className={`p-5 rounded-2xl border leading-relaxed ${
                      isLight ? 'bg-slate-50/80 border-slate-200' : 'bg-slate-950 border-slate-800'
                    }`}
                  >
                    {renderFormattedMarkdown(currentNlm.rawResponse, isLight)}
                  </div>
                )}

                {/* Citations List */}
                {!!currentNlm.citations && currentNlm.citations.length > 0 && (
                  <div className="pt-2">
                    <div className="text-xs font-semibold text-slate-500 mb-1.5">對應教科書與章節引用:</div>
                    <div className="flex flex-wrap gap-2">
                      {currentNlm.citations.map((c, cIdx) => (
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
            );
          })()}
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

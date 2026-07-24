import React from 'react';
import { Star, ChevronLeft, ChevronRight, CheckCircle2 } from 'lucide-react';
import { ExamQuestion, OptionId, ThemeMode } from '../types/exam';
import { DisputeBadge } from './DisputeBadge';
import { renderKaTeXInString } from '../utils/katexRenderer';

interface QuestionPanelProps {
  question: ExamQuestion;
  currentIndex: number;
  totalQuestions: number;
  selectedOption: OptionId | undefined;
  onSelectOption: (optId: OptionId) => void;
  isFlagged: boolean;
  onToggleFlag: () => void;
  onPrev: () => void;
  onNext: () => void;
  isSubmitted: boolean;
  themeMode?: ThemeMode;
}

function renderFormattedText(text: string, isLight: boolean) {
  if (!text) return null;
  // First convert em/strong
  let cleanHtml = text
    .replace(/<em\b[^>]*>(.*?)<\/em>/gi, '<em class="italic text-sky-600 dark:text-sky-300 font-semibold">$1</em>')
    .replace(/<strong\b[^>]*>(.*?)<\/strong>/gi, '<strong class="font-bold text-amber-700 dark:text-amber-300 underline decoration-amber-500/50">$1</strong>');

  // Render KaTeX Math
  cleanHtml = renderKaTeXInString(cleanHtml);

  return <span dangerouslySetInnerHTML={{ __html: cleanHtml }} />;
}

export const QuestionPanel: React.FC<QuestionPanelProps> = ({
  question,
  currentIndex,
  totalQuestions,
  selectedOption,
  onSelectOption,
  isFlagged,
  onToggleFlag,
  onPrev,
  onNext,
  isSubmitted,
  themeMode = 'light',
}) => {
  const isLight = themeMode === 'light';

  return (
    <div
      className={`flex-1 glass-panel border rounded-2xl p-6 md:p-8 flex flex-col justify-between shadow-sm transition-colors ${
        isLight ? 'bg-white border-slate-200 text-slate-900' : 'bg-slate-900/90 border-slate-800 text-slate-100'
      }`}
    >
      <div>
        {/* Top Bar */}
        <div className="flex items-center justify-between pb-4 mb-4 border-b border-slate-200 dark:border-slate-800">
          <div className="flex items-center gap-3">
            <span className="px-3 py-1 rounded-xl bg-sky-500/10 text-sky-700 dark:text-sky-400 font-mono text-sm font-bold border border-sky-500/20">
              第 {question.number || currentIndex + 1} 題
            </span>
            {isSubmitted && (
              <DisputeBadge status={question.reconciliationStatus} notes={question.reconciliationNotes} />
            )}
          </div>

          <div className="flex items-center gap-2">
            {/* Star/Flag Button */}
            <button
              onClick={onToggleFlag}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-semibold transition-all cursor-pointer ${
                isFlagged
                  ? 'bg-amber-500/15 border-amber-500/40 text-amber-700 dark:text-amber-300'
                  : isLight
                  ? 'bg-slate-100 border-slate-200 text-slate-600 hover:text-slate-900'
                  : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
              }`}
            >
              <Star className={`w-3.5 h-3.5 ${isFlagged ? 'fill-amber-400 text-amber-400' : ''}`} />
              <span>{isFlagged ? '已標記' : '標記此題'}</span>
            </button>

            <span className="text-xs text-slate-500 font-mono ml-2">
              {currentIndex + 1} / {totalQuestions}
            </span>
          </div>
        </div>

        {/* Question Stem Content */}
        <div className="mb-6">
          <div className={`text-base md:text-[17px] font-medium leading-relaxed whitespace-pre-line selection:bg-sky-500 selection:text-white ${
            isLight ? 'text-slate-900' : 'text-slate-100'
          }`}>
            {renderFormattedText(question.stem, isLight)}
          </div>
        </div>

        {/* Options List */}
        <div className="space-y-3 mb-6">
          {question.options.map((opt) => {
            const isSelected = selectedOption === opt.id;
            const isSourceCorrect = isSubmitted && question.sourceProvidedAnswer === opt.id;
            const isUserWrong = isSubmitted && isSelected && !isSourceCorrect;

            let optionStyle = isLight
              ? 'bg-slate-50 border-slate-200 text-slate-800 hover:border-sky-300 hover:bg-sky-50/50'
              : 'bg-slate-950/60 border-slate-800 text-slate-300 hover:border-slate-700 hover:bg-slate-900';

            if (isSubmitted) {
              if (isSourceCorrect) {
                optionStyle = isLight
                  ? 'bg-emerald-50 border-emerald-500 text-emerald-900 shadow-xs'
                  : 'bg-emerald-950/70 border-emerald-500 text-emerald-200';
              } else if (isUserWrong) {
                optionStyle = isLight
                  ? 'bg-rose-50 border-rose-400 text-rose-900'
                  : 'bg-rose-950/70 border-rose-500 text-rose-200';
              } else if (isSelected) {
                optionStyle = isLight
                  ? 'bg-slate-200 border-slate-400 text-slate-900'
                  : 'bg-slate-800 border-slate-600 text-slate-200';
              }
            } else if (isSelected) {
              optionStyle = isLight
                ? 'bg-sky-50 border-sky-500 text-sky-950 shadow-xs'
                : 'bg-sky-950/80 border-sky-500 text-sky-200 shadow-lg shadow-sky-500/10';
            }

            return (
              <button
                key={opt.id}
                onClick={() => !isSubmitted && onSelectOption(opt.id)}
                disabled={isSubmitted}
                className={`w-full text-left p-4 rounded-2xl border flex items-start gap-3.5 transition-all cursor-pointer ${optionStyle}`}
              >
                {/* Option Letter Pill */}
                <span
                  className={`w-7 h-7 rounded-xl flex items-center justify-center font-mono font-bold text-xs shrink-0 border ${
                    isSelected
                      ? 'bg-sky-600 text-white border-sky-500 shadow-xs'
                      : isLight
                      ? 'bg-white text-slate-600 border-slate-300'
                      : 'bg-slate-900 text-slate-400 border-slate-700'
                  }`}
                >
                  {opt.id}
                </span>

                {/* Option Text */}
                <div className="flex-1 pt-0.5 text-sm md:text-[15px] leading-relaxed">
                  {renderFormattedText(opt.text, isLight)}
                </div>

                {/* Post-submission Indicators */}
                {isSubmitted && isSourceCorrect && (
                  <span className="text-emerald-600 dark:text-emerald-400 flex items-center gap-1 text-xs font-bold shrink-0 pt-1">
                    <CheckCircle2 className="w-4 h-4" />
                    <span>正確答案</span>
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Navigation Footer */}
      <div className="flex items-center justify-between pt-4 border-t border-slate-200 dark:border-slate-800 mt-4">
        <button
          onClick={onPrev}
          disabled={currentIndex === 0}
          className={`flex items-center gap-1.5 px-4 py-2 rounded-xl border text-xs font-semibold transition-colors cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed ${
            isLight
              ? 'bg-slate-100 border-slate-200 text-slate-700 hover:bg-slate-200'
              : 'bg-slate-950 border-slate-800 text-slate-300 hover:bg-slate-900'
          }`}
        >
          <ChevronLeft className="w-4 h-4" />
          <span>上一題</span>
        </button>

        <span className="text-xs text-slate-500 font-mono hidden sm:inline">
          快捷鍵: Z (上一題) | V (下一題) | T (標記) | A-E (選擇)
        </span>

        <button
          onClick={onNext}
          disabled={currentIndex === totalQuestions - 1}
          className={`flex items-center gap-1.5 px-4 py-2 rounded-xl border text-xs font-semibold transition-colors cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed ${
            isLight
              ? 'bg-slate-100 border-slate-200 text-slate-700 hover:bg-slate-200'
              : 'bg-slate-950 border-slate-800 text-slate-300 hover:bg-slate-900'
          }`}
        >
          <span>下一題</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

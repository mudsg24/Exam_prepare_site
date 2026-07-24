import React from 'react';
import { Star, AlertCircle, Check, X } from 'lucide-react';
import { ExamQuestion, OptionId, ThemeMode } from '../types/exam';

interface QuestionMatrixProps {
  questions: ExamQuestion[];
  currentIndex: number;
  onSelectIndex: (idx: number) => void;
  userAnswers: Record<string, OptionId>;
  flagged: Record<string, boolean>;
  isSubmitted: boolean;
  themeMode?: ThemeMode;
}

export const QuestionMatrix: React.FC<QuestionMatrixProps> = ({
  questions,
  currentIndex,
  onSelectIndex,
  userAnswers,
  flagged,
  isSubmitted,
  themeMode = 'light',
}) => {
  const isLight = themeMode === 'light';

  return (
    <aside
      className={`w-full md:w-64 glass-panel border rounded-2xl p-4 flex flex-col h-full shrink-0 shadow-sm transition-colors ${
        isLight ? 'bg-white border-slate-200 text-slate-900' : 'bg-slate-900/90 border-slate-800 text-slate-100'
      }`}
    >
      <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-200 dark:border-slate-800">
        <h2 className={`text-sm font-bold flex items-center gap-2 ${isLight ? 'text-slate-900' : 'text-slate-200'}`}>
          <span>題目列表</span>
          <span className="text-xs text-slate-500 font-mono">({questions.length} 題)</span>
        </h2>
        <span className="text-[11px] text-slate-400 font-mono">方格快選</span>
      </div>

      {/* Question Grid */}
      <div className="grid grid-cols-5 gap-2 overflow-y-auto max-h-[calc(100vh-220px)] p-1">
        {questions.map((q, idx) => {
          const isCurrent = idx === currentIndex;
          const isAnswered = !!userAnswers[q.id];
          const isFlagged = !!flagged[q.id];
          const isDisputed = q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED');

          let isCorrect: boolean | null = null;
          if (isSubmitted && q.sourceProvidedAnswer && userAnswers[q.id]) {
            isCorrect = userAnswers[q.id] === q.sourceProvidedAnswer;
          }

          // Base style per theme
          let boxBg = isLight
            ? 'bg-slate-100 border-slate-200 text-slate-700 hover:border-sky-400 hover:bg-sky-50'
            : 'bg-slate-950/80 border-slate-800 text-slate-400 hover:border-slate-700';

          if (isSubmitted) {
            if (isCorrect === true) {
              boxBg = isLight
                ? 'bg-emerald-100 border-emerald-400 text-emerald-900 font-bold'
                : 'bg-emerald-950/60 border-emerald-500/50 text-emerald-300';
            } else if (isCorrect === false) {
              boxBg = isLight
                ? 'bg-rose-100 border-rose-400 text-rose-900 font-bold'
                : 'bg-rose-950/60 border-rose-500/50 text-rose-300';
            } else if (isAnswered) {
              boxBg = isLight
                ? 'bg-slate-200 border-slate-300 text-slate-900'
                : 'bg-slate-800 border-slate-700 text-slate-200';
            }
          } else if (isAnswered) {
            boxBg = isLight
              ? 'bg-sky-100 border-sky-400 text-sky-900 font-bold'
              : 'bg-sky-950/50 border-sky-500/40 text-sky-300';
          }

          if (isCurrent) {
            boxBg += isLight
              ? ' ring-2 ring-sky-500 ring-offset-2 ring-offset-white font-extrabold shadow-sm'
              : ' ring-2 ring-sky-400 ring-offset-2 ring-offset-slate-950 font-bold';
          }

          return (
            <button
              key={q.id}
              onClick={() => onSelectIndex(idx)}
              className={`relative h-10 rounded-xl border font-mono text-xs flex items-center justify-center transition-all cursor-pointer ${boxBg}`}
            >
              <span>{q.number}</span>

              {/* Starred / Flagged Tag */}
              {isFlagged && (
                <span className="absolute top-0.5 right-0.5 text-amber-500">
                  <Star className="w-2.5 h-2.5 fill-amber-500" />
                </span>
              )}

              {/* Disputed Alert Indicator */}
              {isSubmitted && isDisputed && (
                <span className="absolute bottom-0.5 left-0.5 text-amber-500" title="此題有爭議">
                  <AlertCircle className="w-2.5 h-2.5" />
                </span>
              )}

              {/* Post-submission Check/Cross Icon */}
              {isSubmitted && isCorrect !== null && (
                <span className="absolute bottom-0.5 right-0.5">
                  {isCorrect ? (
                    <Check className="w-2.5 h-2.5 text-emerald-600 dark:text-emerald-400" />
                  ) : (
                    <X className="w-2.5 h-2.5 text-rose-600 dark:text-rose-400" />
                  )}
                </span>
              )}
            </button>
          );
        })}
      </div>

      {/* Legend Footer */}
      <div className="mt-4 pt-3 border-t border-slate-200 dark:border-slate-800 text-[11px] text-slate-500 space-y-1.5 font-mono">
        <div className="flex items-center gap-2">
          <span className={`w-3 h-3 rounded border inline-block ${
            isLight ? 'bg-sky-100 border-sky-400' : 'bg-sky-950 border-sky-500/40'
          }`} />
          <span>已回答</span>
          <span className={`w-3 h-3 rounded border inline-block ml-2 ${
            isLight ? 'bg-slate-100 border-slate-200' : 'bg-slate-900 border-slate-800'
          }`} />
          <span>未回答</span>
        </div>
        {isSubmitted && (
          <div className="flex items-center gap-2 pt-1 border-t border-slate-200 dark:border-slate-800">
            <span className={`w-3 h-3 rounded border inline-block ${
              isLight ? 'bg-emerald-100 border-emerald-400' : 'bg-emerald-950 border-emerald-500/50'
            }`} />
            <span>答對</span>
            <span className={`w-3 h-3 rounded border inline-block ml-2 ${
              isLight ? 'bg-rose-100 border-rose-400' : 'bg-rose-950 border-rose-500/50'
            }`} />
            <span>答錯</span>
          </div>
        )}
      </div>
    </aside>
  );
};

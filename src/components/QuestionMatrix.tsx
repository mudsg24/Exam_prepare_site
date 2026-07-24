import React from 'react';
import { Star, AlertCircle, Check, X } from 'lucide-react';
import { ExamQuestion, OptionId } from '../types/exam';

interface QuestionMatrixProps {
  questions: ExamQuestion[];
  currentIndex: number;
  onSelectIndex: (idx: number) => void;
  userAnswers: Record<string, OptionId>;
  flagged: Record<string, boolean>;
  isSubmitted: boolean;
}

export const QuestionMatrix: React.FC<QuestionMatrixProps> = ({
  questions,
  currentIndex,
  onSelectIndex,
  userAnswers,
  flagged,
  isSubmitted,
}) => {
  return (
    <aside className="w-full md:w-64 glass-panel border border-slate-800/80 rounded-2xl p-4 flex flex-col h-full shrink-0 shadow-lg">
      <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-800">
        <h2 className="text-sm font-semibold text-slate-200 flex items-center gap-2">
          <span>題目列表</span>
          <span className="text-xs text-slate-400 font-mono">({questions.length} 題)</span>
        </h2>
        <span className="text-[11px] text-slate-500 font-mono">方格快選</span>
      </div>

      {/* Question Grid */}
      <div className="grid grid-cols-5 gap-2 overflow-y-auto max-h-[calc(100vh-220px)] p-1">
        {questions.map((q, idx) => {
          const isCurrent = idx === currentIndex;
          const isAnswered = !!userAnswers[q.id];
          const isFlagged = !!flagged[q.id];
          const isDisputed = q.reconciliationStatus.startsWith('DISPUTED');

          let isCorrect: boolean | null = null;
          if (isSubmitted && q.sourceProvidedAnswer && userAnswers[q.id]) {
            isCorrect = userAnswers[q.id] === q.sourceProvidedAnswer;
          }

          // Base style
          let boxBg = 'bg-slate-900/80 border-slate-800 text-slate-400 hover:border-slate-700';

          if (isSubmitted) {
            if (isCorrect === true) {
              boxBg = 'bg-emerald-950/60 border-emerald-500/50 text-emerald-300';
            } else if (isCorrect === false) {
              boxBg = 'bg-rose-950/60 border-rose-500/50 text-rose-300';
            } else if (isAnswered) {
              boxBg = 'bg-slate-800 border-slate-700 text-slate-200';
            }
          } else if (isAnswered) {
            boxBg = 'bg-cyan-950/50 border-cyan-500/40 text-cyan-300';
          }

          if (isCurrent) {
            boxBg += ' ring-2 ring-cyan-400 ring-offset-2 ring-offset-slate-950 font-bold';
          }

          return (
            <button
              key={q.id}
              onClick={() => onSelectIndex(idx)}
              className={`relative h-10 rounded-lg border font-mono text-xs flex items-center justify-center transition-all ${boxBg}`}
            >
              <span>{q.number}</span>

              {/* Starred / Flagged Tag */}
              {isFlagged && (
                <span className="absolute top-0.5 right-0.5 text-amber-400">
                  <Star className="w-2.5 h-2.5 fill-amber-400" />
                </span>
              )}

              {/* Disputed Alert Indicator */}
              {isSubmitted && isDisputed && (
                <span className="absolute bottom-0.5 left-0.5 text-amber-400" title="此題有爭議">
                  <AlertCircle className="w-2.5 h-2.5" />
                </span>
              )}

              {/* Post-submission Check/Cross Icon */}
              {isSubmitted && isCorrect !== null && (
                <span className="absolute bottom-0.5 right-0.5">
                  {isCorrect ? (
                    <Check className="w-2.5 h-2.5 text-emerald-400" />
                  ) : (
                    <X className="w-2.5 h-2.5 text-rose-400" />
                  )}
                </span>
              )}
            </button>
          );
        })}
      </div>

      {/* Legend Footer */}
      <div className="mt-4 pt-3 border-t border-slate-800 text-[11px] text-slate-400 space-y-1.5 font-mono">
        <div className="flex items-center gap-2">
          <span className="w-3 h-3 rounded bg-cyan-950 border border-cyan-500/40 inline-block" />
          <span>已回答</span>
          <span className="w-3 h-3 rounded bg-slate-900 border border-slate-800 inline-block ml-2" />
          <span>未回答</span>
        </div>
        {isSubmitted && (
          <div className="flex items-center gap-2 pt-1 border-t border-slate-800/60">
            <span className="w-3 h-3 rounded bg-emerald-950 border border-emerald-500/50 inline-block" />
            <span>答對</span>
            <span className="w-3 h-3 rounded bg-rose-950 border border-rose-500/50 inline-block ml-2" />
            <span>答錯</span>
          </div>
        )}
      </div>
    </aside>
  );
};

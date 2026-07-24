import React from 'react';
import { Star, ChevronLeft, ChevronRight, CheckCircle2 } from 'lucide-react';
import { ExamQuestion, OptionId } from '../types/exam';
import { DisputeBadge } from './DisputeBadge';

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
}) => {
  return (
    <div className="flex-1 glass-panel border border-slate-800/80 rounded-2xl p-6 flex flex-col justify-between shadow-xl">
      <div>
        {/* Top Bar for Question Panel */}
        <div className="flex items-center justify-between pb-4 mb-4 border-b border-slate-800">
          <div className="flex items-center gap-3">
            <span className="px-3 py-1 rounded-lg bg-cyan-500/10 text-cyan-400 font-mono text-sm font-bold border border-cyan-500/20">
              第 {question.number} 題
            </span>
            {isSubmitted && (
              <DisputeBadge status={question.reconciliationStatus} notes={question.reconciliationNotes} />
            )}
          </div>

          <div className="flex items-center gap-2">
            {/* Star/Flag Button */}
            <button
              onClick={onToggleFlag}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg border text-xs font-medium transition-all ${
                isFlagged
                  ? 'bg-amber-500/15 border-amber-500/40 text-amber-300'
                  : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-slate-200'
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

        {/* Stem Content */}
        <div className="mb-6">
          <div className="text-base text-slate-100 font-medium leading-relaxed whitespace-pre-line selection:bg-cyan-500 selection:text-slate-950">
            {question.stem}
          </div>
        </div>

        {/* Radio Options List */}
        <div className="space-y-3 mb-6">
          {question.options.map((opt) => {
            const isSelected = selectedOption === opt.id;
            const isSourceCorrect = isSubmitted && question.sourceProvidedAnswer === opt.id;
            const isUserWrong = isSubmitted && isSelected && !isSourceCorrect;

            let optionStyle = 'bg-slate-900/60 border-slate-800 text-slate-300 hover:border-slate-700 hover:bg-slate-900';

            if (isSubmitted) {
              if (isSourceCorrect) {
                optionStyle = 'bg-emerald-950/70 border-emerald-500 text-emerald-200 shadow-md shadow-emerald-500/10';
              } else if (isUserWrong) {
                optionStyle = 'bg-rose-950/70 border-rose-500 text-rose-200';
              } else if (isSelected) {
                optionStyle = 'bg-slate-800 border-slate-600 text-slate-200';
              }
            } else if (isSelected) {
              optionStyle = 'bg-cyan-950/80 border-cyan-500 text-cyan-200 shadow-lg shadow-cyan-500/10';
            }

            return (
              <button
                key={opt.id}
                onClick={() => !isSubmitted && onSelectOption(opt.id)}
                disabled={isSubmitted}
                className={`w-full text-left p-4 rounded-xl border flex items-start gap-3.5 transition-all ${optionStyle}`}
              >
                {/* Option Letter Pill */}
                <span
                  className={`w-7 h-7 rounded-lg flex items-center justify-center font-mono font-bold text-xs shrink-0 border ${
                    isSelected
                      ? 'bg-cyan-500 text-slate-950 border-cyan-400 shadow'
                      : 'bg-slate-800 text-slate-400 border-slate-700'
                  }`}
                >
                  {opt.id}
                </span>

                {/* Option Text */}
                <div className="flex-1 pt-0.5 text-sm leading-relaxed">
                  {opt.text}
                </div>

                {/* Post-submission Indicators */}
                {isSubmitted && isSourceCorrect && (
                  <span className="text-emerald-400 flex items-center gap-1 text-xs font-semibold shrink-0 pt-1">
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
      <div className="flex items-center justify-between pt-4 border-t border-slate-800 mt-4">
        <button
          onClick={onPrev}
          disabled={currentIndex === 0}
          className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 text-xs font-medium hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>上一題</span>
        </button>

        <span className="text-xs text-slate-500 font-mono hidden sm:inline">
          提示: 可使用方向鍵 ← / → 切換題目
        </span>

        <button
          onClick={onNext}
          disabled={currentIndex === totalQuestions - 1}
          className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 text-xs font-medium hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >
          <span>下一題</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

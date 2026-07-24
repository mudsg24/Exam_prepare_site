import React, { useEffect, useState } from 'react';
import { Timer, CheckCircle, AlertCircle, FileText, RefreshCw, BarChart2, Filter } from 'lucide-react';
import { ExamManifestItem } from '../types/exam';

interface HeaderProps {
  manifest: ExamManifestItem[];
  selectedPaperId: string;
  onSelectPaper: (id: string) => void;
  elapsedSeconds: number;
  totalQuestions: number;
  answeredCount: number;
  isSubmitted: boolean;
  scoreCorrect: number | null;
  disputedCount: number;
  filterMode: 'all' | 'disputed' | 'wrong';
  onFilterChange: (mode: 'all' | 'disputed' | 'wrong') => void;
  onReset: () => void;
  onSubmitExam: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  manifest,
  selectedPaperId,
  onSelectPaper,
  elapsedSeconds,
  totalQuestions,
  answeredCount,
  isSubmitted,
  scoreCorrect,
  disputedCount,
  filterMode,
  onFilterChange,
  onReset,
  onSubmitExam,
}) => {
  const [currentTime, setCurrentTime] = useState<string>('');

  useEffect(() => {
    const update = () => {
      const now = new Date();
      setCurrentTime(
        now.toLocaleTimeString('zh-TW', { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' })
      );
    };
    update();
    const interval = setInterval(update, 1000);
    return () => clearInterval(interval);
  }, []);

  const formatTimer = (secs: number) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const progressPercent = totalQuestions > 0 ? Math.round((answeredCount / totalQuestions) * 100) : 0;

  return (
    <header className="sticky top-0 z-40 glass-panel border-b border-slate-800/80 px-6 py-3 shadow-xl">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
        
        {/* Left Brand & Paper Selector */}
        <div className="flex items-center gap-4 w-full md:w-auto">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 text-white shadow-lg shadow-cyan-500/20">
              <FileText className="w-5 h-5" />
            </div>
            <div>
              <h1 className="text-base font-bold tracking-tight text-slate-100 flex items-center gap-2">
                <span>TSN 腎臟專科練習站</span>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 font-mono">
                  練習題模式
                </span>
              </h1>
              <p className="text-xs text-slate-400 font-mono">本機時間: {currentTime}</p>
            </div>
          </div>

          {/* Paper Dropdown */}
          <div className="ml-2">
            <select
              value={selectedPaperId}
              onChange={(e) => onSelectPaper(e.target.value)}
              className="bg-slate-900 text-slate-200 text-xs rounded-lg border border-slate-700/80 px-3 py-1.5 focus:outline-none focus:border-cyan-500 transition-colors"
            >
              {manifest.length === 0 ? (
                <option value="">載入試卷中...</option>
              ) : (
                manifest.map((item) => (
                  <option key={item.id} value={item.id}>
                    {item.title} ({item.questionCount} 題)
                  </option>
                ))
              )}
            </select>
          </div>
        </div>

        {/* Center Timer & Progress */}
        <div className="flex items-center gap-6">
          {/* Elapsed Timer */}
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-900/80 border border-slate-800 text-xs font-mono text-cyan-300">
            <Timer className="w-4 h-4 text-cyan-400 animate-pulse" />
            <span>答題計時: {formatTimer(elapsedSeconds)}</span>
          </div>

          {/* Progress Bar */}
          <div className="hidden lg:flex items-center gap-3">
            <div className="w-36 h-2 rounded-full bg-slate-800 overflow-hidden border border-slate-800">
              <div
                className="h-full bg-gradient-to-r from-cyan-500 to-blue-500 transition-all duration-300"
                style={{ width: `${progressPercent}%` }}
              />
            </div>
            <span className="text-xs text-slate-400 font-mono">
              {answeredCount} / {totalQuestions} ({progressPercent}%)
            </span>
          </div>
        </div>

        {/* Right Stats & Actions */}
        <div className="flex items-center gap-3 w-full md:w-auto justify-end">
          {/* Post-submission Score Display */}
          {isSubmitted && scoreCorrect !== null && (
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-semibold">
              <BarChart2 className="w-4 h-4 text-emerald-400" />
              <span>得分: {scoreCorrect} / {totalQuestions} ({Math.round((scoreCorrect / totalQuestions) * 100)}%)</span>
            </div>
          )}

          {/* Filter Mode Selector (Only when submitted or reviewing) */}
          {isSubmitted && (
            <div className="flex items-center rounded-lg bg-slate-900 border border-slate-800 p-0.5 text-xs">
              <button
                onClick={() => onFilterChange('all')}
                className={`px-2.5 py-1 rounded-md transition-colors ${
                  filterMode === 'all' ? 'bg-slate-800 text-cyan-400 font-medium' : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                全部
              </button>
              <button
                onClick={() => onFilterChange('disputed')}
                className={`px-2.5 py-1 rounded-md transition-colors flex items-center gap-1 ${
                  filterMode === 'disputed' ? 'bg-amber-500/20 text-amber-300 font-medium' : 'text-slate-400 hover:text-amber-300'
                }`}
              >
                <AlertCircle className="w-3 h-3" />
                <span>爭議 ({disputedCount})</span>
              </button>
              <button
                onClick={() => onFilterChange('wrong')}
                className={`px-2.5 py-1 rounded-md transition-colors ${
                  filterMode === 'wrong' ? 'bg-rose-500/20 text-rose-300 font-medium' : 'text-slate-400 hover:text-rose-300'
                }`}
              >
                錯題
              </button>
            </div>
          )}

          {/* Reset Progress Button */}
          <button
            onClick={onReset}
            title="重新開始答題"
            className="p-2 rounded-lg bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200 hover:border-slate-700 transition-colors"
          >
            <RefreshCw className="w-4 h-4" />
          </button>

          {/* Submit Exam Button */}
          {!isSubmitted ? (
            <button
              onClick={onSubmitExam}
              className="px-4 py-1.5 rounded-lg bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-semibold text-xs shadow-lg shadow-cyan-500/25 transition-all"
            >
              送出答案並看解答
            </button>
          ) : (
            <span className="px-3 py-1 rounded-md bg-emerald-500/10 text-emerald-400 text-xs font-semibold border border-emerald-500/20">
              已完成練習
            </span>
          )}
        </div>

      </div>
    </header>
  );
};

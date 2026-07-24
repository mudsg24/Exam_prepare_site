import React, { useEffect, useState, useMemo } from 'react';
import {
  Timer,
  AlertCircle,
  FileText,
  RefreshCw,
  BarChart2,
  Home,
  BookOpen,
  Sun,
  Moon,
  Zap,
  CheckCircle2,
} from 'lucide-react';
import { ExamManifestItem, AppView, ThemeMode, StudyMode } from '../types/exam';

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
  currentView: AppView;
  onNavigateView: (view: AppView) => void;
  themeMode: ThemeMode;
  onToggleTheme: () => void;
  studyMode: StudyMode;
  onToggleStudyMode: () => void;
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
  currentView,
  onNavigateView,
  themeMode,
  onToggleTheme,
  studyMode,
  onToggleStudyMode,
}) => {
  const [currentTime, setCurrentTime] = useState<string>('');

  const groupedPapersByYear = useMemo(() => {
    const years = Array.from(new Set(manifest.map((p) => p.year))).sort((a, b) => b - a);
    return years.map((year) => {
      const papers = manifest
        .filter((p) => p.year === year)
        .sort((a, b) => b.title.localeCompare(a.title, 'zh-Hant', { numeric: true }));
      return { year, papers };
    });
  }, [manifest]);
  const isLight = themeMode === 'light';

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

  return (
    <header className={`sticky top-0 z-40 glass-panel border-b px-4 md:px-6 py-3 shadow-sm transition-colors ${
      isLight ? 'bg-white/95 border-slate-200 text-slate-800' : 'bg-slate-900/95 border-slate-800 text-slate-100'
    }`}>
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">

        {/* Left Brand & View Navigation */}
        <div className="flex items-center gap-4 w-full md:w-auto justify-between md:justify-start">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-gradient-to-tr from-sky-500 to-blue-600 text-white shadow-md">
              <FileText className="w-5 h-5" />
            </div>
            <div>
              <h1 className="text-base font-bold tracking-tight flex items-center gap-2">
                <span>TSN 腎臟專科刷題站</span>
              </h1>
              <p className="text-[11px] text-slate-500 font-mono hidden sm:block">時間: {currentTime}</p>
            </div>
          </div>

          {/* Navigation View Selector */}
          <div className={`flex items-center p-1 rounded-xl border text-xs font-semibold ${
            isLight ? 'bg-slate-100 border-slate-200' : 'bg-slate-950 border-slate-800'
          }`}>
            <button
              onClick={() => onNavigateView('dashboard')}
              className={`px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition-all cursor-pointer ${
                currentView === 'dashboard'
                  ? 'bg-sky-600 text-white shadow-sm font-bold'
                  : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'
              }`}
            >
              <Home className="w-3.5 h-3.5" />
              <span>首頁入口</span>
            </button>
            <button
              onClick={() => onNavigateView('exam')}
              className={`px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition-all cursor-pointer ${
                currentView === 'exam'
                  ? 'bg-sky-600 text-white shadow-sm font-bold'
                  : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>答題測驗室</span>
            </button>
          </div>
        </div>

        {/* Center: Exam Room Controls & Work Mode Toggle */}
        {currentView === 'exam' && (
          <div className="flex items-center gap-3">
            {/* Paper Selector Dropdown */}
            <select
              value={selectedPaperId}
              onChange={(e) => onSelectPaper(e.target.value)}
              className={`text-xs rounded-lg border px-3 py-1.5 max-w-[180px] sm:max-w-[240px] truncate focus:outline-none focus:border-sky-500 ${
                isLight ? 'bg-slate-50 text-slate-900 border-slate-300' : 'bg-slate-950 text-slate-100 border-slate-800'
              }`}
            >
              {manifest.length === 0 ? (
                <option value="">載入試卷中...</option>
              ) : (
                groupedPapersByYear.map(({ year, papers }) => (
                  <optgroup key={year} label={`${year} 年`}>
                    {papers.map((item) => (
                      <option key={item.id} value={item.id}>
                        {item.title} ({item.questionCount} 題)
                      </option>
                    ))}
                  </optgroup>
                ))
              )}
            </select>

            {/* Mode Switcher Button: Practice vs Work Mode (Direct Study) */}
            <button
              onClick={onToggleStudyMode}
              title={studyMode === 'work' ? '切換回測驗模式' : '切換至直看解答/工作速查模式'}
              className={`px-3 py-1.5 rounded-xl border text-xs font-bold flex items-center gap-1.5 transition-all cursor-pointer ${
                studyMode === 'work'
                  ? 'bg-amber-500 text-white border-amber-600 shadow-sm animate-pulse-subtle'
                  : isLight
                  ? 'bg-slate-100 border-slate-200 text-slate-700 hover:bg-slate-200'
                  : 'bg-slate-950 border-slate-800 text-slate-300 hover:bg-slate-900'
              }`}
            >
              <Zap className="w-3.5 h-3.5" />
              <span>{studyMode === 'work' ? '工作模式 (直看解答中)' : '練習測驗中'}</span>
            </button>

            {/* Elapsed Timer */}
            {studyMode === 'practice' && (
              <div className={`hidden sm:flex items-center gap-1.5 px-2.5 py-1 rounded-lg border text-xs font-mono font-semibold ${
                isLight ? 'bg-slate-100 border-slate-200 text-sky-700' : 'bg-slate-950 border-slate-800 text-sky-300'
              }`}>
                <Timer className="w-3.5 h-3.5 text-sky-500 animate-pulse" />
                <span>{formatTimer(elapsedSeconds)}</span>
              </div>
            )}
          </div>
        )}

        {/* Right Controls & Theme Switcher */}
        <div className="flex items-center gap-3 w-full md:w-auto justify-end">
          {/* Exam View Post-Submission Score */}
          {currentView === 'exam' && (isSubmitted || studyMode === 'work') && scoreCorrect !== null && (
            <div className="flex items-center gap-1.5 px-3 py-1 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-600 dark:text-emerald-300 text-xs font-semibold">
              <BarChart2 className="w-3.5 h-3.5 text-emerald-500" />
              <span>正解數: {scoreCorrect}/{totalQuestions}</span>
            </div>
          )}

          {/* Exam View Filters */}
          {currentView === 'exam' && (isSubmitted || studyMode === 'work') && (
            <div className={`flex items-center rounded-lg border p-0.5 text-xs ${
              isLight ? 'bg-slate-100 border-slate-200' : 'bg-slate-950 border-slate-800'
            }`}>
              <button
                onClick={() => onFilterChange('all')}
                className={`px-2 py-1 rounded-md transition-colors cursor-pointer ${
                  filterMode === 'all' ? 'bg-white dark:bg-slate-800 text-sky-600 font-bold shadow-xs' : 'text-slate-500'
                }`}
              >
                全部
              </button>
              <button
                onClick={() => onFilterChange('disputed')}
                className={`px-2 py-1 rounded-md transition-colors flex items-center gap-1 cursor-pointer ${
                  filterMode === 'disputed' ? 'bg-amber-500/20 text-amber-700 dark:text-amber-300 font-bold' : 'text-slate-500'
                }`}
              >
                <AlertCircle className="w-3 h-3" />
                <span>爭議 ({disputedCount})</span>
              </button>
              <button
                onClick={() => onFilterChange('wrong')}
                className={`px-2 py-1 rounded-md transition-colors cursor-pointer ${
                  filterMode === 'wrong' ? 'bg-rose-500/20 text-rose-700 dark:text-rose-300 font-bold' : 'text-slate-500'
                }`}
              >
                錯題
              </button>
            </div>
          )}

          {/* Reset Exam Button */}
          {currentView === 'exam' && (
            <button
              onClick={onReset}
              title="重新開始答題"
              className={`p-2 rounded-xl border transition-colors cursor-pointer ${
                isLight ? 'bg-slate-100 border-slate-200 text-slate-600 hover:bg-slate-200' : 'bg-slate-950 border-slate-800 text-slate-400 hover:text-slate-200'
              }`}
            >
              <RefreshCw className="w-3.5 h-3.5" />
            </button>
          )}

          {/* Submit Exam Button */}
          {currentView === 'exam' && !isSubmitted && studyMode === 'practice' && (
            <button
              onClick={onSubmitExam}
              className="px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-sky-600 to-blue-600 hover:from-sky-500 hover:to-blue-500 text-white font-semibold text-xs shadow-md transition-all cursor-pointer"
            >
              送出看解答
            </button>
          )}

          {/* Theme Toggle Button */}
          <button
            onClick={onToggleTheme}
            title={isLight ? '切換至深色主題' : '切換至明亮主題'}
            className={`p-2 rounded-xl border transition-all cursor-pointer flex items-center justify-center ${
              isLight
                ? 'bg-amber-50 border-amber-200 text-amber-600 hover:bg-amber-100'
                : 'bg-slate-800 border-slate-700 text-sky-300 hover:bg-slate-700'
            }`}
          >
            {isLight ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4" />}
          </button>
        </div>

      </div>
    </header>
  );
};

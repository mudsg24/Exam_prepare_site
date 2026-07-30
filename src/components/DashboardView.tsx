import React, { useState, useMemo } from 'react';
import {
  BookOpen,
  CheckCircle2,
  AlertTriangle,
  FileText,
  Target,
  Flame,
  Award,
  Sparkles,
  ChevronRight,
  Calendar,
} from 'lucide-react';
import {
  ExamManifestItem,
  GlobalPracticeStats,
  CustomPracticeType,
  ThemeMode,
} from '../types/exam';

interface DashboardViewProps {
  manifest: ExamManifestItem[];
  stats: GlobalPracticeStats;
  onSelectPaper: (paperId: string) => void;
  onSelectTutorial?: (paperId: string) => void;
  onStartCustomPractice: (type: CustomPracticeType, count?: number) => void;
  paperProgressMap: Record<string, { total: number; answered: number; correct: number }>;
  themeMode: ThemeMode;
}

export const sanitizePaperTitle = (title: string): string => {
  return (title || '').replace(/\s*\(\s*重點轉化\s*\)/g, '').trim();
};

export const isGNPaper = (paper: ExamManifestItem): boolean => {
  return Boolean(
    (paper.sourceCategory && paper.sourceCategory.includes('GN')) ||
    (paper.title && paper.title.includes('GN'))
  );
};

export const isTopicPracticePaper = (paper: ExamManifestItem): boolean => {
  if (isGNPaper(paper)) return false;
  return Boolean(
    (paper.sourceCategory && paper.sourceCategory.includes('主題練習')) ||
    (paper.title && paper.title.includes('主題備考')) ||
    (paper.id && paper.id.includes('主題備考'))
  );
};

export const isKeyPointTransformationPaper = (paper: ExamManifestItem): boolean => {
  if (isGNPaper(paper) || isTopicPracticePaper(paper)) return false;
  return Boolean(
    (paper.sourceCategory && paper.sourceCategory.includes('重點轉化')) ||
    (paper.title && paper.title.includes('重點轉化')) ||
    (paper.id && paper.id.includes('重點轉化'))
  );
};

export const DashboardView: React.FC<DashboardViewProps> = ({
  manifest,
  stats,
  onSelectPaper,
  onSelectTutorial,
  onStartCustomPractice,
  paperProgressMap,
  themeMode,
}) => {
  const [customUnattemptedCount, setCustomUnattemptedCount] = useState<number>(10);
  const isLight = themeMode === 'light';

  const overallAccuracy =
    stats.completedQuestions > 0
      ? Math.round((stats.correctCount / stats.completedQuestions) * 100)
      : 0;

  // Group manifest by year (2026 then 2025), and sub-group into Standard Library vs Key Point Transformation vs GN vs Topic Practice
  const groupedPaperSections = useMemo(() => {
    const years = Array.from(
      new Set(manifest.map((p) => p?.year).filter((y): y is number => typeof y === 'number'))
    ).sort((a, b) => b - a);

    return years.map((year) => {
      const yearPapers = manifest.filter((p) => p && p.year === year);

      const standardPapers = yearPapers
        .filter((p) => !isKeyPointTransformationPaper(p) && !isTopicPracticePaper(p) && !isGNPaper(p))
        .sort((a, b) => (b.title || '').localeCompare(a.title || '', 'zh-Hant', { numeric: true }));

      const keyPointPapers = yearPapers
        .filter((p) => isKeyPointTransformationPaper(p))
        .sort((a, b) => (b.title || '').localeCompare(a.title || '', 'zh-Hant', { numeric: true }));

      const gnPapers = yearPapers
        .filter((p) => isGNPaper(p))
        .sort((a, b) => (b.title || '').localeCompare(a.title || '', 'zh-Hant', { numeric: true }));

      const topicPapers = yearPapers
        .filter((p) => isTopicPracticePaper(p))
        .sort((a, b) => (b.title || '').localeCompare(a.title || '', 'zh-Hant', { numeric: true }));

      const sections = [];
      if (standardPapers.length > 0) {
        sections.push({
          key: `${year}-standard`,
          title: `${year} 年試卷與章節練習庫`,
          papers: standardPapers,
          categoryType: 'standard' as const,
        });
      }
      if (keyPointPapers.length > 0) {
        sections.push({
          key: `${year}-keypoint`,
          title: `${year} 醫院重點轉化`,
          papers: keyPointPapers,
          categoryType: 'keyPoint' as const,
        });
      }
      if (gnPapers.length > 0) {
        sections.push({
          key: `${year}-gn`,
          title: `${year} GN`,
          papers: gnPapers,
          categoryType: 'gn' as const,
        });
      }
      if (topicPapers.length > 0) {
        sections.push({
          key: `${year}-topic`,
          title: `${year} 主題練習`,
          papers: topicPapers,
          categoryType: 'topic' as const,
        });
      }

      return { year, sections };
    });
  }, [manifest]);

  return (
    <div className="max-w-7xl mx-auto w-full p-4 md:p-6 space-y-8">
      {/* 1. Welcome Banner & Global Stats Grid */}
      <div className="space-y-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h2 className={`text-2xl font-bold tracking-tight ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
              TSN 腎臟專科醫師甄試與歷年考題練習總覽
            </h2>
            <p className={`text-sm mt-1 ${isLight ? 'text-slate-600' : 'text-slate-400'}`}>
              權威國標試題、歷年交換題與雙重 NotebookLM 智慧圖文對比分析
            </p>
          </div>
        </div>

        {/* Stats Summary Cards */}
        <div className="grid grid-cols-2 lg:grid-cols-5 gap-4">
          {/* Total Questions */}
          <div className={`glass-panel p-5 rounded-2xl border shadow-sm ${isLight ? 'bg-white border-slate-200' : 'bg-slate-900/80 border-slate-800'}`}>
            <div className="flex items-center justify-between text-slate-500 mb-2">
              <span className="text-xs font-semibold uppercase tracking-wider">全站題庫總數</span>
              <BookOpen className="w-4 h-4 text-sky-500" />
            </div>
            <div className={`text-2xl font-bold font-mono ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
              {stats.totalQuestions} <span className="text-xs font-sans font-normal text-slate-500">題</span>
            </div>
          </div>

          {/* Answered Questions */}
          <div className={`glass-panel p-5 rounded-2xl border shadow-sm ${isLight ? 'bg-white border-slate-200' : 'bg-slate-900/80 border-slate-800'}`}>
            <div className="flex items-center justify-between text-slate-500 mb-2">
              <span className="text-xs font-semibold uppercase tracking-wider">已完成練習</span>
              <CheckCircle2 className="w-4 h-4 text-emerald-500" />
            </div>
            <div className={`text-2xl font-bold font-mono ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
              {stats.completedQuestions}{' '}
              <span className="text-xs font-sans font-normal text-slate-500">
                ({stats.totalQuestions > 0 ? Math.round((stats.completedQuestions / stats.totalQuestions) * 100) : 0}%)
              </span>
            </div>
          </div>

          {/* Accuracy */}
          <div className={`glass-panel p-5 rounded-2xl border shadow-sm ${isLight ? 'bg-white border-slate-200' : 'bg-slate-900/80 border-slate-800'}`}>
            <div className="flex items-center justify-between text-slate-500 mb-2">
              <span className="text-xs font-semibold uppercase tracking-wider">平均正確率</span>
              <Award className="w-4 h-4 text-amber-500" />
            </div>
            <div className={`text-2xl font-bold font-mono ${overallAccuracy >= 70 ? 'text-emerald-600' : 'text-amber-600'}`}>
              {overallAccuracy}%
            </div>
          </div>

          {/* Mistake Bank */}
          <div className={`glass-panel p-5 rounded-2xl border shadow-sm ${isLight ? 'bg-white border-slate-200' : 'bg-slate-900/80 border-slate-800'}`}>
            <div className="flex items-center justify-between text-slate-500 mb-2">
              <span className="text-xs font-semibold uppercase tracking-wider">待訂正錯題</span>
              <Flame className="w-4 h-4 text-rose-500" />
            </div>
            <div className="text-2xl font-bold font-mono text-rose-600">
              {stats.wrongCount} <span className="text-xs font-sans font-normal text-slate-500">題</span>
            </div>
          </div>

          {/* Unattempted Bank */}
          <div className={`glass-panel p-5 rounded-2xl border shadow-sm ${isLight ? 'bg-white border-slate-200' : 'bg-slate-900/80 border-slate-800'}`}>
            <div className="flex items-center justify-between text-slate-500 mb-2">
              <span className="text-xs font-semibold uppercase tracking-wider">全新未做題</span>
              <Target className="w-4 h-4 text-indigo-500" />
            </div>
            <div className="text-2xl font-bold font-mono text-indigo-600">
              {stats.unattemptedCount} <span className="text-xs font-sans font-normal text-slate-500">題</span>
            </div>
          </div>
        </div>
      </div>

      {/* 2. Quick Practice Generators Section */}
      <div className="space-y-4">
        <h3 className={`text-lg font-bold flex items-center gap-2 ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
          <Sparkles className="w-5 h-5 text-sky-500" />
          <span>快捷智慧刷題模式</span>
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Card 1: Unattempted Questions */}
          <div className={`glass-panel p-6 rounded-2xl border flex flex-col justify-between space-y-5 transition-all shadow-sm ${
            isLight ? 'bg-white border-slate-200 hover:border-sky-300' : 'bg-slate-900/80 border-slate-800 hover:border-sky-500/30'
          }`}>
            <div>
              <div className="flex items-center justify-between mb-3">
                <span className="p-2.5 rounded-xl bg-sky-500/10 text-sky-600 font-bold border border-sky-500/20 flex items-center gap-2">
                  <Target className="w-5 h-5" />
                  <span className="text-sm">🎯 未寫過題目特訓</span>
                </span>
                <span className="text-xs font-mono text-slate-500">庫存 {stats.unattemptedCount} 題</span>
              </div>
              <p className={`text-xs leading-relaxed ${isLight ? 'text-slate-600' : 'text-slate-400'}`}>
                從全站題庫中自動抽樣你完全未做過的全新題目，進行快速特訓與測驗。
              </p>
            </div>

            <div className="space-y-3 pt-2 border-t border-slate-200/60 dark:border-slate-800">
              <div className="flex items-center gap-2">
                {[5, 10, 20].map((count) => (
                  <button
                    key={count}
                    disabled={stats.unattemptedCount === 0}
                    onClick={() => onStartCustomPractice('unattempted', count)}
                    className="flex-1 py-2 px-3 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-sky-700 dark:text-sky-300 text-xs font-bold border border-sky-500/30 transition-all disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer"
                  >
                    練 {count} 題
                  </button>
                ))}
              </div>

              {/* Custom Input */}
              <div className="flex items-center gap-2">
                <input
                  type="number"
                  min={1}
                  max={Math.max(1, stats.unattemptedCount)}
                  value={customUnattemptedCount}
                  onChange={(e) => setCustomUnattemptedCount(Math.max(1, parseInt(e.target.value) || 1))}
                  className={`w-20 px-3 py-1.5 rounded-xl text-xs font-mono border focus:outline-none focus:border-sky-500 ${
                    isLight ? 'bg-slate-50 text-slate-900 border-slate-300' : 'bg-slate-950 text-slate-100 border-slate-800'
                  }`}
                />
                <button
                  disabled={stats.unattemptedCount === 0}
                  onClick={() => onStartCustomPractice('unattempted', customUnattemptedCount)}
                  className="flex-1 py-1.5 px-3 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-xs font-bold transition-all shadow disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-1 cursor-pointer"
                >
                  <span>自訂出題</span>
                  <ChevronRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          </div>

          {/* Card 2: Mistake Review */}
          <div className={`glass-panel p-6 rounded-2xl border flex flex-col justify-between space-y-5 transition-all shadow-sm ${
            isLight ? 'bg-white border-slate-200 hover:border-rose-300' : 'bg-slate-900/80 border-slate-800 hover:border-rose-500/30'
          }`}>
            <div>
              <div className="flex items-center justify-between mb-3">
                <span className="p-2.5 rounded-xl bg-rose-500/10 text-rose-600 font-bold border border-rose-500/20 flex items-center gap-2">
                  <Flame className="w-5 h-5" />
                  <span className="text-sm">🔥 歷史錯題重練</span>
                </span>
                <span className="text-xs font-mono text-slate-500">錯題 {stats.wrongCount} 題</span>
              </div>
              <p className={`text-xs leading-relaxed ${isLight ? 'text-slate-600' : 'text-slate-400'}`}>
                收集過往答錯但尚未訂正成功的題目，重複練習鎖定痛點與弱點。
              </p>
            </div>

            <div className="space-y-3 pt-2 border-t border-slate-200/60 dark:border-slate-800">
              <div className="flex items-center gap-2">
                {[5, 10].map((count) => (
                  <button
                    key={count}
                    disabled={stats.wrongCount === 0}
                    onClick={() => onStartCustomPractice('wrong', count)}
                    className="flex-1 py-2 px-3 rounded-xl bg-rose-500/10 hover:bg-rose-500/20 text-rose-700 dark:text-rose-300 text-xs font-bold border border-rose-500/30 transition-all disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer"
                  >
                    練 {count} 題
                  </button>
                ))}
              </div>

              <button
                disabled={stats.wrongCount === 0}
                onClick={() => onStartCustomPractice('wrong', stats.wrongCount)}
                className="w-full py-2 px-4 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold transition-all shadow disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <span>重練全站所有錯題 ({stats.wrongCount} 題)</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Card 3: Disputed Questions */}
          <div className={`glass-panel p-6 rounded-2xl border flex flex-col justify-between space-y-5 transition-all shadow-sm ${
            isLight ? 'bg-white border-slate-200 hover:border-amber-300' : 'bg-slate-900/80 border-slate-800 hover:border-amber-500/30'
          }`}>
            <div>
              <div className="flex items-center justify-between mb-3">
                <span className="p-2.5 rounded-xl bg-amber-500/10 text-amber-600 font-bold border border-amber-500/20 flex items-center gap-2">
                  <AlertTriangle className="w-5 h-5" />
                  <span className="text-sm">⚖️ 雙重 NLM 爭議題特訓</span>
                </span>
                <span className="text-xs font-mono text-slate-500">爭議 {stats.disputedCount} 題</span>
              </div>
              <p className={`text-xs leading-relaxed ${isLight ? 'text-slate-600' : 'text-slate-400'}`}>
                針對原始解答與兩組 NotebookLM AI 推論產生分歧或爭議的考題進行專項審查。
              </p>
            </div>

            <div className="space-y-3 pt-2 border-t border-slate-200/60 dark:border-slate-800">
              <div className="flex items-center gap-2">
                {[10, 20, 50].map((count) => (
                  <button
                    key={count}
                    disabled={stats.disputedCount === 0}
                    onClick={() => onStartCustomPractice('disputed', count)}
                    className="flex-1 py-2 px-3 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 text-amber-700 dark:text-amber-300 text-xs font-bold border border-amber-500/30 transition-all disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer"
                  >
                    練 {count} 題
                  </button>
                ))}
              </div>

              <button
                disabled={stats.disputedCount === 0}
                onClick={() => onStartCustomPractice('disputed', stats.disputedCount)}
                className="w-full py-2.5 px-4 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold transition-all shadow disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <span>特訓全站所有爭議題 ({stats.disputedCount} 題)</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* 3. Paper Library Section */}
      <div className="space-y-6">
        <div className="flex items-center justify-between border-b pb-3 border-slate-200/60 dark:border-slate-800">
          <h3 className={`text-lg font-bold flex items-center gap-2 ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
            <FileText className="w-5 h-5 text-sky-500" />
            <span>歷年試卷與章節練習庫</span>
          </h3>
          <span className="text-xs text-slate-500 font-mono">共 {manifest.length} 份試卷</span>
        </div>

        {groupedPaperSections.map(({ year, sections }) => (
          <div key={year} className="space-y-6">
            {sections.map((section) => (
              <div key={section.key} className="space-y-4">
                <div className="flex items-center justify-between pt-2">
                  <span
                    className={`px-3 py-1 rounded-xl text-xs font-bold border flex items-center gap-1.5 shadow-sm ${
                      section.categoryType === 'gn'
                        ? 'bg-cyan-500/10 text-cyan-800 dark:text-cyan-300 border-cyan-500/30'
                        : section.categoryType === 'topic'
                        ? 'bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 border-emerald-500/30'
                        : section.categoryType === 'keyPoint'
                        ? 'bg-[#e9d5ff]/40 text-purple-800 dark:text-purple-200 border-[#d8b4fe]/60'
                        : 'bg-sky-500/10 text-sky-700 dark:text-sky-300 border-sky-500/20'
                    }`}
                  >
                    {section.categoryType === 'gn' ? (
                      <Target className="w-3.5 h-3.5 text-cyan-500" />
                    ) : section.categoryType === 'topic' ? (
                      <BookOpen className="w-3.5 h-3.5 text-emerald-500" />
                    ) : section.categoryType === 'keyPoint' ? (
                      <Sparkles className="w-3.5 h-3.5 text-purple-500" />
                    ) : (
                      <Calendar className="w-3.5 h-3.5" />
                    )}
                    <span>{section.title}</span>
                  </span>
                  <span className="text-xs text-slate-400 font-mono">{section.papers.length} 份試卷</span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {section.papers.map((paper) => {
                    const prog = paperProgressMap[paper.id] || { total: paper.questionCount, answered: 0, correct: 0 };
                    const percent = prog.total > 0 ? Math.round((prog.answered / prog.total) * 100) : 0;
                    const isCompleted = prog.answered === prog.total && prog.total > 0;
                    const displayTitle = sanitizePaperTitle(paper.title);

                    return (
                      <div
                        key={paper.id}
                        className={`glass-panel p-5 rounded-2xl border flex flex-col justify-between space-y-4 transition-all glass-card-hover ${
                          isLight ? 'bg-white border-slate-200' : 'bg-slate-900/80 border-slate-800'
                        }`}
                      >
                        <div className="space-y-2">
                          {paper.sourceCategory &&
                            !/^\d{4}\s*年?(交換題|試卷與章節練習庫|重點轉化|主題練習|GN)$/.test(paper.sourceCategory) &&
                            section.categoryType === 'standard' && (
                              <div className="flex items-center justify-between">
                                <span className="px-2.5 py-0.5 rounded-full bg-sky-500/10 text-sky-700 dark:text-sky-400 text-[11px] font-semibold border border-sky-500/20">
                                  {paper.sourceCategory}
                                </span>
                              </div>
                            )}

                          <h4 className={`text-sm font-bold leading-snug line-clamp-2 ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
                            {displayTitle}
                          </h4>
                        </div>

                        <div className="space-y-3 pt-3 border-t border-slate-200/60 dark:border-slate-800">
                          {/* Progress info */}
                          <div className="flex items-center justify-between text-xs">
                            <span className="text-slate-500">
                              進度: <strong className={isLight ? 'text-slate-800' : 'text-slate-200'}>{prog.answered} / {prog.total} 題</strong>
                            </span>
                            <span className="font-mono text-slate-500">{percent}%</span>
                          </div>

                          <div className={`w-full h-2 rounded-full overflow-hidden ${isLight ? 'bg-slate-100 border border-slate-200' : 'bg-slate-800 border border-slate-800'}`}>
                            <div
                              className={`h-full transition-all duration-300 ${
                                isCompleted
                                  ? 'bg-emerald-500'
                                  : section.categoryType === 'topic'
                                  ? 'bg-gradient-to-r from-emerald-500 to-teal-600'
                                  : section.categoryType === 'keyPoint'
                                  ? 'bg-gradient-to-r from-[#d8b4fe] to-[#c084fc]'
                                  : 'bg-gradient-to-r from-sky-500 to-blue-600'
                              }`}
                              style={{ width: `${percent}%` }}
                            />
                          </div>

                          {/* Topic Tutorial Button */}
                          <button
                            onClick={() => onSelectTutorial && onSelectTutorial(paper.id)}
                            disabled={!paper.hasTutorial}
                            className={`w-full py-2 px-3 rounded-xl text-xs font-extrabold flex items-center justify-center gap-1.5 transition-all cursor-pointer ${
                              paper.hasTutorial
                                ? 'bg-emerald-500/15 hover:bg-emerald-500/25 text-emerald-800 dark:text-emerald-300 border border-emerald-500/30 shadow-sm ring-1 ring-emerald-500/20'
                                : 'bg-slate-100 dark:bg-slate-800/40 text-slate-400 border border-slate-200 dark:border-slate-800 opacity-60 cursor-not-allowed'
                            }`}
                          >
                            <Sparkles className="w-3.5 h-3.5 text-emerald-500" />
                            <span>{paper.hasTutorial ? '🎓 主題式備考教學' : '🎓 主題式備考 (尚無講堂)'}</span>
                            <ChevronRight className="w-3.5 h-3.5 ml-auto" />
                          </button>

                          {/* Start Exam Button */}
                          <button
                            onClick={() => onSelectPaper(paper.id)}
                            className={`w-full py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 transition-all cursor-pointer ${
                              isCompleted
                                ? 'bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 border border-slate-300 dark:border-slate-700'
                                : section.categoryType === 'topic'
                                ? 'bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold shadow-sm'
                                : section.categoryType === 'keyPoint'
                                ? 'bg-[#d8b4fe] hover:bg-[#c084fc] text-purple-950 font-extrabold shadow-sm border border-purple-300/40'
                                : 'bg-sky-600 hover:bg-sky-500 text-white shadow-md'
                            }`}
                          >
                            <span>{isCompleted ? '重新練習試卷' : prog.answered > 0 ? '繼續答題' : '進入試卷答題'}</span>
                            <ChevronRight className="w-3.5 h-3.5" />
                          </button>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

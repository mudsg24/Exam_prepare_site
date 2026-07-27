import React, { useState, useEffect } from 'react';
import {
  ArrowLeft,
  BookOpen,
  Sparkles,
  ChevronRight,
  Bookmark,
  Layers,
  Lightbulb,
  FileImage,
  Maximize2,
  X,
} from 'lucide-react';
import { marked } from 'marked';
import { renderKaTeXInString } from '../utils/katexRenderer';
import { ExamTutorial, ThemeMode, TutorialModule, TutorialDiagram } from '../types/exam';

interface TutorialReaderViewProps {
  tutorial: ExamTutorial;
  themeMode: ThemeMode;
  onBack: () => void;
  onStartExam: (paperId: string) => void;
}

function renderFormattedMarkdown(rawText: string, isLight: boolean) {
  if (!rawText) return null;
  const mathRendered = renderKaTeXInString(rawText);

  try {
    const html = marked.parse(mathRendered, { async: false }) as string;
    return (
      <div
        className={`prose max-w-none text-sm md:text-base leading-relaxed space-y-3 font-sans selection:bg-emerald-500 selection:text-white ${
          isLight ? 'text-slate-800' : 'text-slate-200 prose-invert'
        }`}
        dangerouslySetInnerHTML={{ __html: html }}
      />
    );
  } catch (e) {
    return (
      <div
        className={`whitespace-pre-line text-sm leading-relaxed ${
          isLight ? 'text-slate-800' : 'text-slate-200'
        }`}
      >
        {rawText}
      </div>
    );
  }
}

export const TutorialReaderView: React.FC<TutorialReaderViewProps> = ({
  tutorial,
  themeMode,
  onBack,
  onStartExam,
}) => {
  const [activeModuleId, setActiveModuleId] = useState<string>(
    tutorial.modules[0]?.moduleId || ''
  );
  const [zoomDiagram, setZoomDiagram] = useState<TutorialDiagram | null>(null);
  const [imageFitMode, setImageFitMode] = useState<Record<string, 'width' | 'height'>>({});
  const isLight = themeMode === 'light';

  const activeModule: TutorialModule | undefined = tutorial.modules.find(
    (m) => m.moduleId === activeModuleId
  ) || tutorial.modules[0];

  // Keyboard shortcut for chapter navigation (ArrowLeft / ArrowRight)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (
        zoomDiagram ||
        e.target instanceof HTMLInputElement ||
        e.target instanceof HTMLTextAreaElement
      ) {
        return;
      }

      if (e.key === 'ArrowLeft') {
        const currentIndex = tutorial.modules.findIndex((m) => m.moduleId === activeModuleId);
        if (currentIndex > 0) {
          setActiveModuleId(tutorial.modules[currentIndex - 1].moduleId);
        }
      } else if (e.key === 'ArrowRight') {
        const currentIndex = tutorial.modules.findIndex((m) => m.moduleId === activeModuleId);
        if (currentIndex !== -1 && currentIndex < tutorial.modules.length - 1) {
          setActiveModuleId(tutorial.modules[currentIndex + 1].moduleId);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [tutorial.modules, activeModuleId, zoomDiagram]);

  return (
    <div className="max-w-7xl mx-auto w-full p-4 md:p-6 space-y-6">
      {/* 1. Header & Back Navigation */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b pb-4 border-slate-200/60 dark:border-slate-800">
        <div className="flex items-center gap-3">
          <button
            onClick={onBack}
            className="p-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 transition-all cursor-pointer flex items-center gap-1.5 text-xs font-bold shadow-sm"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>返回總覽</span>
          </button>
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-800 dark:text-emerald-300 text-xs font-extrabold border border-emerald-500/20 flex items-center gap-1">
                <Sparkles className="w-3 h-3 text-emerald-500" />
                <span>主題式備考教學講堂</span>
              </span>
              <span className="text-xs font-mono text-slate-400">{tutorial.year} 年考訊重點</span>
            </div>
            <h1 className={`text-xl md:text-2xl font-extrabold tracking-tight mt-1 ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
              {tutorial.title}
            </h1>
          </div>
        </div>

        <button
          onClick={() => onStartExam(tutorial.paperId)}
          className="px-4 py-2.5 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-extrabold text-xs shadow-md transition-all flex items-center gap-2 cursor-pointer self-start md:self-auto"
        >
          <BookOpen className="w-4 h-4" />
          <span>進入此章節題庫刷題</span>
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>

      {/* 2. Main Reader Grid Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Left Column: Sidebar Module Navigation (Sticky & Floating) */}
        <div className="lg:col-span-1 space-y-3 lg:sticky lg:top-6 self-start">
          <div className={`p-4 rounded-2xl border glass-panel ${isLight ? 'bg-white border-slate-200 shadow-sm' : 'bg-slate-900/80 border-slate-800'}`}>
            <h3 className="text-xs font-extrabold uppercase tracking-wider text-slate-400 mb-3 flex items-center justify-between">
              <span className="flex items-center gap-1.5">
                <Layers className="w-3.5 h-3.5 text-sky-500" />
                <span>講堂章節目錄 ({tutorial.modules.length})</span>
              </span>
              <span className="text-[10px] font-medium text-slate-400 dark:text-slate-500 flex items-center gap-0.5" title="使用鍵盤左右方向鍵翻閱章節">
                <kbd className="px-1 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-mono text-[9px]">←</kbd>
                <kbd className="px-1 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 font-mono text-[9px]">→</kbd>
              </span>
            </h3>

            <div className="space-y-1.5 max-h-[calc(100vh-10rem)] overflow-y-auto pr-0.5">
              {tutorial.modules.map((mod, idx) => {
                const isActive = mod.moduleId === activeModule?.moduleId;
                return (
                  <button
                    key={mod.moduleId}
                    onClick={() => setActiveModuleId(mod.moduleId)}
                    className={`w-full text-left p-3 rounded-xl transition-all cursor-pointer text-xs font-bold flex items-start gap-2.5 ${
                      isActive
                        ? 'bg-emerald-500/15 text-emerald-900 dark:text-emerald-300 border border-emerald-500/30 shadow-sm ring-1 ring-emerald-500/20'
                        : isLight
                        ? 'hover:bg-slate-100 text-slate-700'
                        : 'hover:bg-slate-800/60 text-slate-300'
                    }`}
                  >
                    <span className={`w-5 h-5 rounded-lg flex items-center justify-center text-[10px] font-mono shrink-0 ${
                      isActive ? 'bg-emerald-500 text-white font-extrabold' : 'bg-slate-200 dark:bg-slate-800 text-slate-500'
                    }`}>
                      {idx + 1}
                    </span>
                    <span className="line-clamp-2 leading-snug">{mod.moduleTitle}</span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Right Column: Lecture Content Display */}
        <div className="lg:col-span-3 space-y-6">
          {activeModule && (
            <div className={`p-6 rounded-2xl border glass-panel space-y-8 ${
              isLight ? 'bg-white border-slate-200 shadow-sm' : 'bg-slate-900/80 border-slate-800'
            }`}>
              {/* Module Header */}
              <h2 className={`text-xl md:text-2xl font-extrabold leading-snug flex items-center gap-2.5 ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
                <Bookmark className="w-6 h-6 text-emerald-500 shrink-0" />
                <span>{activeModule.moduleTitle}</span>
              </h2>

              {/* Study Strategy Callout */}
              {activeModule.studyGuide && (
                <div className="p-5 rounded-2xl bg-amber-500/10 border border-amber-500/30 space-y-2.5 shadow-sm">
                  <div className="flex items-center gap-2 text-amber-800 dark:text-amber-300 text-xs font-extrabold">
                    <Lightbulb className="w-4 h-4 text-amber-500 shrink-0" />
                    <span>備考需知與核心學習指南 (Study Strategy)</span>
                  </div>
                  <div className="text-xs md:text-sm font-medium">
                    {renderFormattedMarkdown(activeModule.studyGuide, isLight)}
                  </div>
                </div>
              )}

              {/* Module Reference Micrographs / Standalone Figures Gallery */}
              {(() => {
                const standaloneDiagrams = activeModule.diagrams?.filter(
                  (diag) => !activeModule.sections.some((sec) =>
                    sec.diagram?.id === diag.id ||
                    sec.diagram?.imagePath === diag.imagePath ||
                    sec.diagrams?.some((d) => d.id === diag.id || d.imagePath === diag.imagePath)
                  )
                ) || [];
                const has1to1Matching = activeModule.diagrams?.length === activeModule.sections.length;

                if (standaloneDiagrams.length === 0 || has1to1Matching) return null;

                return (
                  <div className="space-y-6 pt-4 border-t border-slate-200/60 dark:border-slate-800">
                    <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                      <Sparkles className="w-3.5 h-3.5 text-sky-500" />
                      <span>權威參考圖表 (Authority Micrographs & Reference Figures)</span>
                    </h4>

                    <div className="grid grid-cols-1 gap-6">
                      {standaloneDiagrams.map((diag) => (
                        <div
                          key={diag.id}
                          className={`p-4 md:p-5 rounded-2xl border shadow-sm space-y-3 transition-all ${
                            isLight ? 'bg-slate-50/80 border-slate-200' : 'bg-slate-950/60 border-slate-800'
                          }`}
                        >
                          <div className="flex items-center justify-between">
                            <span className="px-2.5 py-0.5 rounded-full bg-sky-500/10 text-sky-700 dark:text-sky-300 text-[11px] font-mono font-extrabold border border-sky-500/20 flex items-center gap-1">
                              <FileImage className="w-3 h-3 text-sky-500" />
                              <span>{diag.sourceBook || 'AI Medical Illustration'}</span>
                            </span>

                            {diag.imagePath && (
                              <div className="flex items-center gap-1.5 bg-slate-200/60 dark:bg-slate-800/60 p-1 rounded-xl border border-slate-300/50 dark:border-slate-700/50">
                                <button
                                  onClick={() => setImageFitMode((prev) => ({ ...prev, [diag.id]: 'width' }))}
                                  className={`px-2.5 py-1 rounded-lg text-xs font-extrabold transition-all cursor-pointer ${
                                    (imageFitMode[diag.id] || 'width') === 'width'
                                      ? 'bg-sky-500 text-white shadow-sm'
                                      : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                                  }`}
                                  title="Fit 寬度 (滿寬排版)"
                                >
                                  Fit 寬度
                                </button>
                                <button
                                  onClick={() => setImageFitMode((prev) => ({ ...prev, [diag.id]: 'height' }))}
                                  className={`px-2.5 py-1 rounded-lg text-xs font-extrabold transition-all cursor-pointer ${
                                    imageFitMode[diag.id] === 'height'
                                      ? 'bg-sky-500 text-white shadow-sm'
                                      : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                                  }`}
                                  title="Fit 高度 (限制最大高度 500px)"
                                >
                                  Fit 高度
                                </button>
                                <button
                                  onClick={() => setZoomDiagram(diag)}
                                  className="px-2.5 py-1 rounded-lg text-xs font-extrabold text-slate-600 dark:text-slate-300 hover:text-sky-500 flex items-center gap-1 transition-all cursor-pointer"
                                  title="全螢幕放大顯示"
                                >
                                  <Maximize2 className="w-3.5 h-3.5" />
                                  <span>放大顯示</span>
                                </button>
                              </div>
                            )}
                          </div>

                          {diag.imagePath && (
                            <div
                              onClick={() => setZoomDiagram(diag)}
                              className="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-2 flex justify-center cursor-pointer group"
                            >
                              <img
                                src={diag.imagePath}
                                alt={diag.caption}
                                className={`rounded-lg transition-transform duration-300 group-hover:scale-[1.01] ${
                                  (imageFitMode[diag.id] || 'width') === 'width'
                                    ? 'w-full h-auto'
                                    : 'w-full max-h-[500px] object-contain'
                                }`}
                              />
                            </div>
                          )}

                          {diag.caption && (
                            <p className="text-xs font-bold text-center text-slate-600 dark:text-slate-400 italic leading-relaxed">
                              {diag.caption}
                            </p>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                );
              })()}

              {/* Interleaved Lecture Chapters (解釋圖片 -> 解釋文字) */}
              <div className="space-y-10 pt-6 border-t border-slate-200/60 dark:border-slate-800">
                {activeModule.sections.map((sec, sIdx) => {
                  const secDiagrams: TutorialDiagram[] = sec.diagrams && sec.diagrams.length > 0
                    ? sec.diagrams
                    : (sec.diagram ? [sec.diagram] : (
                        activeModule.diagrams && activeModule.diagrams.length === activeModule.sections.length
                          ? [activeModule.diagrams[sIdx]]
                          : []
                      ));

                  return (
                    <div key={sIdx} className="space-y-4">
                      {/* Chapter Heading */}
                      <h3 className={`text-lg font-extrabold flex items-center gap-2.5 ${isLight ? 'text-slate-900' : 'text-slate-100'}`}>
                        <span className="w-3 h-3 rounded-full bg-emerald-500 shrink-0" />
                        <span>{sec.heading}</span>
                      </h3>

                      {/* Explanation Images (解釋圖片) */}
                      {secDiagrams.map((diag) => (
                        <div
                          key={diag.id}
                          className={`p-4 md:p-5 rounded-2xl border shadow-sm space-y-3 transition-all ${
                            isLight ? 'bg-slate-50/80 border-slate-200' : 'bg-slate-950/60 border-slate-800'
                          }`}
                        >
                          <div className="flex items-center justify-between">
                            <span className="px-2.5 py-0.5 rounded-full bg-sky-500/10 text-sky-700 dark:text-sky-300 text-[11px] font-mono font-extrabold border border-sky-500/20 flex items-center gap-1">
                              <FileImage className="w-3 h-3 text-sky-500" />
                              <span>{diag.sourceBook || 'AI Medical Illustration'}</span>
                            </span>

                            {diag.imagePath && (
                              <div className="flex items-center gap-1.5 bg-slate-200/60 dark:bg-slate-800/60 p-1 rounded-xl border border-slate-300/50 dark:border-slate-700/50">
                                <button
                                  onClick={() => setImageFitMode((prev) => ({ ...prev, [diag.id]: 'width' }))}
                                  className={`px-2.5 py-1 rounded-lg text-xs font-extrabold transition-all cursor-pointer ${
                                    (imageFitMode[diag.id] || 'width') === 'width'
                                      ? 'bg-sky-500 text-white shadow-sm'
                                      : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                                  }`}
                                  title="Fit 寬度 (滿寬排版)"
                                >
                                  Fit 寬度
                                </button>
                                <button
                                  onClick={() => setImageFitMode((prev) => ({ ...prev, [diag.id]: 'height' }))}
                                  className={`px-2.5 py-1 rounded-lg text-xs font-extrabold transition-all cursor-pointer ${
                                    imageFitMode[diag.id] === 'height'
                                      ? 'bg-sky-500 text-white shadow-sm'
                                      : 'text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white'
                                  }`}
                                  title="Fit 高度 (限制最大高度 500px)"
                                >
                                  Fit 高度
                                </button>
                                <button
                                  onClick={() => setZoomDiagram(diag)}
                                  className="px-2.5 py-1 rounded-lg text-xs font-extrabold text-slate-600 dark:text-slate-300 hover:text-sky-500 flex items-center gap-1 transition-all cursor-pointer"
                                  title="全螢幕放大顯示"
                                >
                                  <Maximize2 className="w-3.5 h-3.5" />
                                  <span>放大顯示</span>
                                </button>
                              </div>
                            )}
                          </div>

                          {diag.imagePath && (
                            <div
                              onClick={() => setZoomDiagram(diag)}
                              className="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-2 flex justify-center cursor-pointer group"
                            >
                              <img
                                src={diag.imagePath}
                                alt={diag.caption}
                                className={`rounded-lg transition-transform duration-300 group-hover:scale-[1.01] ${
                                  (imageFitMode[diag.id] || 'width') === 'width'
                                    ? 'w-full h-auto'
                                    : 'w-full max-h-[500px] object-contain'
                                }`}
                              />
                            </div>
                          )}

                          {diag.caption && (
                            <p className="text-xs font-bold text-center text-slate-600 dark:text-slate-400 italic leading-relaxed">
                              {diag.caption}
                            </p>
                          )}
                        </div>
                      ))}

                      {/* Explanation Text (解釋文字) */}
                      {sec.content && (
                        <div className="pl-5 border-l-2 border-slate-200 dark:border-slate-800">
                          {renderFormattedMarkdown(sec.content, isLight)}
                        </div>
                      )}

                      {sec.items && sec.items.length > 0 && (
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 pl-5 pt-2">
                          {sec.items.map((item, iIdx) => (
                            <div
                              key={iIdx}
                              className={`p-4 rounded-xl border ${
                                isLight ? 'bg-slate-50 border-slate-200' : 'bg-slate-950/60 border-slate-800'
                              }`}
                            >
                              <div className="font-extrabold text-xs text-sky-700 dark:text-sky-300 mb-1">
                                {item.term}
                              </div>
                              <div className="text-xs text-slate-700 dark:text-slate-300">
                                {item.description}
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>

              {/* Bottom Action */}
              <div className="pt-8 border-t border-slate-200/60 dark:border-slate-800 flex items-center justify-between">
                <div className="text-xs md:text-sm text-slate-500 font-medium">
                  研讀完本講堂章節觀念？點擊右側按鈕立即進行刷題驗證！
                </div>
                <button
                  onClick={() => onStartExam(tutorial.paperId)}
                  className="px-5 py-3 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-extrabold text-xs md:text-sm transition-all shadow-md flex items-center gap-2 cursor-pointer"
                >
                  <BookOpen className="w-4 h-4" />
                  <span>進入本章節題庫刷題</span>
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Image Zoom Lightbox Modal */}
      {zoomDiagram && (
        <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4">
          <div className="relative max-w-6xl w-full bg-slate-900 rounded-2xl p-4 md:p-6 border border-slate-800 space-y-4 max-h-[90vh] flex flex-col">
            <div className="flex items-center justify-between border-b pb-3 border-slate-800">
              <span className="text-sm font-extrabold text-slate-200 flex items-center gap-2">
                <FileImage className="w-4 h-4 text-sky-400" />
                <span>{zoomDiagram.caption}</span>
              </span>
              <button
                onClick={() => setZoomDiagram(null)}
                className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="flex-1 overflow-auto flex items-center justify-center p-2">
              <img
                src={zoomDiagram.imagePath}
                alt={zoomDiagram.caption}
                className="max-h-full max-w-full object-contain rounded-lg"
              />
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

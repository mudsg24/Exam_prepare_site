import React, { useEffect, useState, useCallback, useMemo } from 'react';
import { Header } from './components/Header';
import { QuestionMatrix } from './components/QuestionMatrix';
import { QuestionPanel } from './components/QuestionPanel';
import { ExplanationPanel } from './components/ExplanationPanel';
import { ImageModal, DisplayableImage } from './components/ImageModal';
import { DashboardView } from './components/DashboardView';
import { TutorialReaderView } from './components/TutorialReaderView';
import {
  ExamManifestItem,
  ExamPaper,
  ExamQuestion,
  ExamTutorial,
  OptionId,
  ResolvedImage,
  AttachedImage,
  UserAttemptState,
  ThemeMode,
  AppView,
  StudyMode,
  GlobalPracticeStats,
  CustomPracticeType,
} from './types/exam';

const MOCK_MANIFEST: ExamManifestItem[] = [
  {
    id: 'demo_2025_zhongshan',
    title: '2025 114出題表格_傳統題_中山吳勝文',
    sourceCategory: '2025 年交換題',
    questionCount: 3,
    year: 2025,
  },
];

const MOCK_PAPER: ExamPaper = {
  id: 'demo_2025_zhongshan',
  title: '2025 114出題表格_傳統題_中山吳勝文',
  rawTitle: '2025 114出題表格_傳統題_中山吳勝文 - 原檔',
  sourceCategory: '2025 年交換題',
  year: 2025,
  questionCount: 3,
  createdAt: new Date().toISOString(),
  questions: [
    {
      id: 'demo_q1',
      number: 1,
      stem: 'With regards to renal diseases treated with therapeutic plasma exchange, which of following condition is not standard primary therapy?',
      options: [
        { id: 'A', text: 'Thrombotic thrombocytopenia purpura' },
        { id: 'B', text: 'Recurrent focal and segmental glomerulosclerosis in transplanted kidney' },
        { id: 'C', text: 'Systemic lupus nephritis, class III or IV' },
        { id: 'D', text: 'Rapidly progressive glomerulonephritis (ANCA) with requiring dialysis' },
      ],
      sourceAnswerStatus: 'provided',
      sourceProvidedAnswer: 'C',
      nlmResponses: [
        {
          notebookTitle: 'TSN：出題 (1-1)',
          notebookId: '6bd5caab-d00a-4f59-a464-459156966b8c',
          accountProfile: 'mudskipper24',
          selectedOption: 'C',
          rawResponse: '1. Answer: (C) Systemic lupus nephritis, class III or IV.\n2. Detailed Explanation: Plasma exchange is not routinely indicated as standard primary therapy for Class III/IV lupus nephritis unless severe refractory features exist.\n3. Citations: Chapter 64 page 2133.',
          citations: [{ chapter: 'Chap 64', page: '2133' }],
          figureMentions: ['Fig 64-1'],
          databaseSufficiency: 'SUFFICIENT',
          error: null,
        },
      ],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '原始答案 (C) 與 NotebookLM 檢索結果一致。',
      resolvedImages: [],
    },
    {
      id: 'demo_q2',
      number: 2,
      stem: 'In each session of hemodialysis, many factors could influence the effectiveness of solute clearance. Which of below description is wrong?',
      options: [
        { id: 'A', text: 'Solute-related variables and their distributions in the body are determinants for their clearance, in which the size of the molecule is the most important intrinsic physical feature governing its removal.' },
        { id: 'B', text: 'Permeability of the membrane to solutes of various sizes and membrane surface area could decide the effectiveness of clearance' },
        { id: 'C', text: 'The clearances of larger molecules could be influenced by blood or dialysate flow rates' },
        { id: 'D', text: 'Treatment time is important for both clearances of small and middle molecules' },
      ],
      sourceAnswerStatus: 'provided',
      sourceProvidedAnswer: 'C',
      nlmResponses: [],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '原始答案 (C)。',
      resolvedImages: [],
    },
    {
      id: 'demo_q3',
      number: 3,
      stem: 'What is the reason for excessively low arterial pressures in blood circuit during hemodialysis, except of ?',
      options: [
        { id: 'A', text: 'Inadequate blood access flow' },
        { id: 'B', text: 'Kinking of arterial blood tubing' },
        { id: 'C', text: 'Needle placement against vessel wall' },
        { id: 'D', text: 'Dialyzer blood leak' },
      ],
      sourceAnswerStatus: 'provided',
      sourceProvidedAnswer: 'D',
      nlmResponses: [],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '原始答案 (D)。',
      resolvedImages: [],
    },
  ],
};

export const App: React.FC = () => {
  const [themeMode, setThemeMode] = useState<ThemeMode>('light');
  const [currentView, setCurrentView] = useState<AppView>('dashboard');
  const [studyMode, setStudyMode] = useState<StudyMode>('practice');
  const [manifest, setManifest] = useState<ExamManifestItem[]>(MOCK_MANIFEST);
  const [allPapersMap, setAllPapersMap] = useState<Record<string, ExamPaper>>({
    [MOCK_PAPER.id]: MOCK_PAPER,
  });

  const [selectedPaperId, setSelectedPaperId] = useState<string>(MOCK_PAPER.id);
  const [currentPaper, setCurrentPaper] = useState<ExamPaper>(MOCK_PAPER);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [filterMode, setFilterMode] = useState<'all' | 'disputed' | 'wrong'>('all');
  const [modalImage, setModalImage] = useState<DisplayableImage | null>(null);

  // User Attempt State per Paper (LocalStorage)
  const [attemptState, setAttemptState] = useState<UserAttemptState>(() => {
    const saved = localStorage.getItem(`attempt_${selectedPaperId}`);
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        /* ignore */
      }
    }
    return {
      paperId: selectedPaperId,
      answers: {},
      flagged: {},
      startTime: Date.now(),
      elapsedSeconds: 0,
      isSubmitted: false,
      submittedAt: null,
    };
  });

  // Sync Document Class for Theme Mode
  useEffect(() => {
    if (themeMode === 'dark') {
      document.documentElement.classList.add('theme-dark');
    } else {
      document.documentElement.classList.remove('theme-dark');
    }
  }, [themeMode]);

  // Load Manifest & Preload All Paper JSONs for Global Analytics
  useEffect(() => {
    fetch('/server-data/exams_manifest.json')
      .then((res) => (res.ok ? res.json() : null))
      .then(async (manifestData: ExamManifestItem[]) => {
        if (manifestData && Array.isArray(manifestData) && manifestData.length > 0) {
          setManifest(manifestData);

          // Preload paper JSONs
          const loadedMap: Record<string, ExamPaper> = {};
          await Promise.all(
            manifestData.map((item) => {
              if (!item || !item.id) return Promise.resolve();
              return fetch(`/server-data/${item.id}.json`)
                .then((r) => (r.ok ? r.json() : null))
                .then((paperData: any) => {
                  if (paperData) {
                    const rawQuestions = Array.isArray(paperData) ? paperData : (paperData.questions || []);
                    const questions = rawQuestions.map((q: any, qIdx: number) => ({
                      ...q,
                      number: q.number || qIdx + 1,
                      options: (q.options || []).map((opt: any, optIdx: number) => {
                        if (typeof opt === 'string') {
                          const letters = ['A', 'B', 'C', 'D', 'E'];
                          return { id: letters[optIdx] || 'A', text: opt };
                        }
                        return opt;
                      }),
                    }));
                    const normalizedPaper: ExamPaper = {
                      id: paperData.id || paperData.paperId || item.id,
                      title: paperData.title || paperData.paperTitle || item.title,
                      rawTitle: paperData.rawTitle || paperData.paperTitle || item.title,
                      sourceCategory: paperData.sourceCategory || paperData.category || item.sourceCategory,
                      year: paperData.year || item.year || 2026,
                      questionCount: paperData.questionCount || paperData.totalQuestions || questions.length,
                      createdAt: paperData.createdAt || new Date().toISOString(),
                      questions,
                    };
                    loadedMap[item.id] = normalizedPaper;
                  }
                })
                .catch(() => {});
            })
          );

          if (Object.keys(loadedMap).length > 0) {
            setAllPapersMap((prev) => ({ ...prev, ...loadedMap }));
            const firstId = manifestData[0].id;
            if (loadedMap[firstId]) {
              setSelectedPaperId(firstId);
              setCurrentPaper(loadedMap[firstId]);
            }
          }
        }
      })
      .catch(() => {
        /* Fallback to mock paper */
      });
  }, []);

  // Handle Paper Selection Change
  useEffect(() => {
    const paper = allPapersMap[selectedPaperId];
    if (paper) {
      setCurrentPaper(paper);
      setCurrentIndex(0);
    }
  }, [selectedPaperId, allPapersMap]);

  // Sync / Restore Attempt State on paper change
  useEffect(() => {
    const saved = localStorage.getItem(`attempt_${selectedPaperId}`);
    if (saved) {
      try {
        setAttemptState(JSON.parse(saved));
        return;
      } catch (e) {
        /* ignore */
      }
    }
    setAttemptState({
      paperId: selectedPaperId,
      answers: {},
      flagged: {},
      startTime: Date.now(),
      elapsedSeconds: 0,
      isSubmitted: false,
      submittedAt: null,
    });
  }, [selectedPaperId]);

  // Auto-Save Attempt State
  useEffect(() => {
    if (attemptState.paperId === selectedPaperId) {
      localStorage.setItem(`attempt_${selectedPaperId}`, JSON.stringify(attemptState));
    }
  }, [attemptState, selectedPaperId]);

  // Timer Effect
  useEffect(() => {
    if (currentView !== 'exam' || attemptState.isSubmitted || studyMode === 'work') return;
    const timer = setInterval(() => {
      setAttemptState((prev) => ({
        ...prev,
        elapsedSeconds: prev.elapsedSeconds + 1,
      }));
    }, 1000);
    return () => clearInterval(timer);
  }, [currentView, attemptState.isSubmitted, studyMode]);

  // Compute Global Analytics & Progress Map
  const { globalStats, paperProgressMap } = useMemo(() => {
    let totalQuestions = 0;
    let completedQuestions = 0;
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;
    let disputedCount = 0;
    const progressMap: Record<string, { total: number; answered: number; correct: number }> = {};

    Object.values(allPapersMap).forEach((paper) => {
      const paperId = paper.id || (paper as any).paperId;
      if (!paperId || !paper.questions) return;

      let paperAnswered = 0;
      let paperCorrect = 0;

      let paperAnswers: Record<string, OptionId> = {};
      if (paperId === attemptState.paperId) {
        paperAnswers = attemptState.answers || {};
      } else {
        const savedAttemptStr = localStorage.getItem(`attempt_${paperId}`);
        if (savedAttemptStr) {
          try {
            const parsed: UserAttemptState = JSON.parse(savedAttemptStr);
            paperAnswers = parsed.answers || {};
          } catch (e) {}
        }
      }

      paper.questions.forEach((q) => {
        totalQuestions++;
        if (q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED')) {
          disputedCount++;
        }

        const userAns = paperAnswers[q.id];
        if (userAns) {
          completedQuestions++;
          paperAnswered++;
          if (q.sourceProvidedAnswer && userAns === q.sourceProvidedAnswer) {
            correctCount++;
            paperCorrect++;
          } else if (q.sourceProvidedAnswer) {
            wrongCount++;
          }
        } else {
          unattemptedCount++;
        }
      });

      progressMap[paperId] = {
        total: paper.questions.length,
        answered: paperAnswered,
        correct: paperCorrect,
      };
    });

    const stats: GlobalPracticeStats = {
      totalQuestions,
      completedQuestions,
      correctCount,
      wrongCount,
      unattemptedCount,
      disputedCount,
    };

    return { globalStats: stats, paperProgressMap: progressMap };
  }, [allPapersMap, attemptState]);

  // Launch Custom Practice Session
  const handleStartCustomPractice = (type: CustomPracticeType, count?: number) => {
    const allQuestions: ExamQuestion[] = [];
    Object.values(allPapersMap).forEach((paper) => {
      let paperAnswers: Record<string, OptionId> = {};
      if (paper.id === attemptState.paperId) {
        paperAnswers = attemptState.answers || {};
      } else {
        const savedAttemptStr = localStorage.getItem(`attempt_${paper.id}`);
        if (savedAttemptStr) {
          try {
            const parsed: UserAttemptState = JSON.parse(savedAttemptStr);
            paperAnswers = parsed.answers || {};
          } catch (e) {}
        }
      }

      paper.questions.forEach((q) => {
        const userAns = paperAnswers[q.id];
        if (type === 'unattempted' && !userAns) {
          allQuestions.push(q);
        } else if (type === 'wrong' && userAns && q.sourceProvidedAnswer && userAns !== q.sourceProvidedAnswer) {
          allQuestions.push(q);
        } else if (type === 'disputed' && q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED')) {
          allQuestions.push(q);
        }
      });
    });

    if (allQuestions.length === 0) {
      alert('無符合條件的題目');
      return;
    }

    const limitCount = count !== undefined ? count : allQuestions.length;
    const selectedQuestions = allQuestions.slice(0, limitCount).map((q, idx) => ({
      ...q,
      number: idx + 1,
    }));

    const titleMap = {
      unattempted: `🎯 專屬特訓 - 全新未寫題 (${selectedQuestions.length}題)`,
      wrong: `🔥 專屬特訓 - 歷史錯題重練 (${selectedQuestions.length}題)`,
      disputed: `⚖️ 專屬特訓 - NLM 雙重爭議題 (${selectedQuestions.length}題)`,
      paper: '專屬特訓',
    };

    const customPaper: ExamPaper = {
      id: `custom_${type}_${Date.now()}`,
      title: titleMap[type],
      rawTitle: titleMap[type],
      sourceCategory: '智慧特訓',
      year: new Date().getFullYear(),
      questionCount: selectedQuestions.length,
      createdAt: new Date().toISOString(),
      questions: selectedQuestions,
    };

    setSelectedPaperId(customPaper.id);
    setCurrentPaper(customPaper);
    setAllPapersMap((prev) => ({ ...prev, [customPaper.id]: customPaper }));
    setCurrentIndex(0);
    setCurrentView('exam');
  };

  const [activeTutorial, setActiveTutorial] = useState<ExamTutorial | null>(null);

  // Select Paper from Dashboard
  const handleSelectPaperFromDashboard = (paperId: string) => {
    setSelectedPaperId(paperId);
    if (allPapersMap[paperId]) {
      setCurrentPaper(allPapersMap[paperId]);
    }
    setCurrentIndex(0);
    setCurrentView('exam');
  };

  // Select Tutorial from Dashboard
  const handleSelectTutorialFromDashboard = (paperId: string) => {
    const manifestItem = manifest.find((item) => item.id === paperId);
    const tutorialId = manifestItem?.tutorialId || `${paperId}_tutorial`;
    
    fetch(`/server-data/tutorials/${tutorialId}.json`)
      .then((res) => (res.ok ? res.json() : null))
      .then((data: ExamTutorial | null) => {
        if (data && data.modules) {
          setActiveTutorial(data);
          setCurrentView('tutorial');
        } else {
          alert('該試卷的主題式備考教學載入失敗或尚在編寫中');
        }
      })
      .catch((e) => {
        console.error('Failed to load tutorial:', e);
        alert('主題式備考教學載入失敗');
      });
  };

  // Filtered Questions in Active Exam
  const isEffectiveSubmitted = attemptState.isSubmitted || studyMode === 'work';

  const filteredQuestions = currentPaper.questions.filter((q) => {
    if (filterMode === 'disputed') {
      return q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED');
    }
    if (filterMode === 'wrong') {
      const userAns = attemptState.answers[q.id];
      return q.sourceProvidedAnswer && userAns && userAns !== q.sourceProvidedAnswer;
    }
    return true;
  });

  const activeQuestion = filteredQuestions[currentIndex] || currentPaper.questions[0];

  // Actions
  const handleSelectOption = (optId: OptionId) => {
    if (isEffectiveSubmitted && studyMode !== 'work') return;
    setAttemptState((prev) => ({
      ...prev,
      answers: {
        ...prev.answers,
        [activeQuestion.id]: optId,
      },
    }));
  };

  const handleToggleFlag = useCallback(() => {
    if (!activeQuestion) return;
    setAttemptState((prev) => ({
      ...prev,
      flagged: {
        ...prev.flagged,
        [activeQuestion.id]: !prev.flagged[activeQuestion.id],
      },
    }));
  }, [activeQuestion]);

  const handleSubmitExam = () => {
    setAttemptState((prev) => ({
      ...prev,
      isSubmitted: true,
      submittedAt: Date.now(),
    }));
  };

  const handleReset = () => {
    if (window.confirm('確定要重新開始此試卷答題嗎？')) {
      const newState: UserAttemptState = {
        paperId: selectedPaperId,
        answers: {},
        flagged: {},
        startTime: Date.now(),
        elapsedSeconds: 0,
        isSubmitted: false,
        submittedAt: null,
      };
      setAttemptState(newState);
      setCurrentIndex(0);
      setFilterMode('all');
    }
  };

  // Score computation
  let scoreCorrect = 0;
  currentPaper.questions.forEach((q) => {
    if (q.sourceProvidedAnswer) {
      if (attemptState.answers[q.id] === q.sourceProvidedAnswer || studyMode === 'work') {
        scoreCorrect++;
      }
    }
  });

  const activeDisputedCount = currentPaper.questions.filter((q) =>
    q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED')
  ).length;

  const answeredCount = Object.keys(attemptState.answers).length;

  // Keyboard Shortcuts: t = flag, z = prev, v = next, a-e = select
  const handleKeyDown = useCallback(
    (e: KeyboardEvent) => {
      if (currentView !== 'exam') return;
      const key = e.key.toLowerCase();

      if (key === 't') {
        e.preventDefault();
        handleToggleFlag();
      } else if (key === 'z' || e.key === 'ArrowLeft') {
        e.preventDefault();
        setCurrentIndex((prev) => Math.max(0, prev - 1));
      } else if (key === 'v' || e.key === 'ArrowRight') {
        e.preventDefault();
        setCurrentIndex((prev) => Math.min(filteredQuestions.length - 1, prev + 1));
      } else if (activeQuestion && !attemptState.isSubmitted && ['a', 'b', 'c', 'd', 'e'].includes(key)) {
        const opt = key.toUpperCase() as OptionId;
        if (activeQuestion.options.some((o) => o.id === opt)) {
          handleSelectOption(opt);
        }
      }
    },
    [currentView, filteredQuestions.length, attemptState.isSubmitted, activeQuestion, handleToggleFlag]
  );

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  return (
    <div className={`min-h-screen flex flex-col font-sans transition-colors ${
      themeMode === 'light' ? 'bg-slate-50 text-slate-900' : 'bg-slate-950 text-slate-100'
    }`}>
      {/* Top Navigation Header */}
      <Header
        manifest={manifest}
        selectedPaperId={selectedPaperId}
        onSelectPaper={(id) => setSelectedPaperId(id)}
        elapsedSeconds={attemptState.elapsedSeconds}
        totalQuestions={currentPaper.questions.length}
        answeredCount={answeredCount}
        isSubmitted={isEffectiveSubmitted}
        scoreCorrect={scoreCorrect}
        disputedCount={activeDisputedCount}
        filterMode={filterMode}
        onFilterChange={setFilterMode}
        onReset={handleReset}
        onSubmitExam={handleSubmitExam}
        currentView={currentView}
        onNavigateView={setCurrentView}
        themeMode={themeMode}
        onToggleTheme={() => setThemeMode((prev) => (prev === 'light' ? 'dark' : 'light'))}
        studyMode={studyMode}
        onToggleStudyMode={() => setStudyMode((prev) => (prev === 'practice' ? 'work' : 'practice'))}
      />

      {/* Main View Switcher */}
      {currentView === 'dashboard' ? (
        <main className="flex-1">
          <DashboardView
            manifest={manifest}
            stats={globalStats}
            onSelectPaper={handleSelectPaperFromDashboard}
            onSelectTutorial={handleSelectTutorialFromDashboard}
            onStartCustomPractice={handleStartCustomPractice}
            paperProgressMap={paperProgressMap}
            themeMode={themeMode}
          />
        </main>
      ) : currentView === 'tutorial' && activeTutorial ? (
        <main className="flex-1">
          <TutorialReaderView
            tutorial={activeTutorial}
            themeMode={themeMode}
            onBack={() => setCurrentView('dashboard')}
            onStartExam={handleSelectPaperFromDashboard}
          />
        </main>
      ) : (
        <main className="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 flex flex-col md:flex-row gap-6">
          {/* Left Panel: Matrix Grid */}
          <QuestionMatrix
            questions={filteredQuestions}
            currentIndex={currentIndex}
            onSelectIndex={(idx) => setCurrentIndex(idx)}
            userAnswers={attemptState.answers}
            flagged={attemptState.flagged}
            isSubmitted={isEffectiveSubmitted}
            themeMode={themeMode}
          />

          {/* Right Panel: Active Question & Explanation */}
          <div className="flex-1 flex flex-col">
            {activeQuestion ? (
              <>
                <QuestionPanel
                  question={activeQuestion}
                  currentIndex={currentIndex}
                  totalQuestions={filteredQuestions.length}
                  selectedOption={attemptState.answers[activeQuestion.id]}
                  onSelectOption={handleSelectOption}
                  isFlagged={!!attemptState.flagged[activeQuestion.id]}
                  onToggleFlag={handleToggleFlag}
                  onPrev={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
                  onNext={() => setCurrentIndex((prev) => Math.min(filteredQuestions.length - 1, prev + 1))}
                  isSubmitted={isEffectiveSubmitted}
                  themeMode={themeMode}
                  onOpenAttachedImage={(img) => setModalImage(img)}
                />

                {/* Show Explanation Panel in Work Mode or post-submission */}
                {isEffectiveSubmitted && (
                  <ExplanationPanel
                    question={activeQuestion}
                    onOpenImage={(img) => setModalImage(img)}
                    themeMode={themeMode}
                  />
                )}
              </>
            ) : (
              <div className={`glass-panel rounded-2xl p-12 text-center text-slate-500 ${
                themeMode === 'light' ? 'bg-white border-slate-200' : 'bg-slate-900 border-slate-800'
              }`}>
                篩選條件下無符合的題目
              </div>
            )}
          </div>
        </main>
      )}

      {/* Image Modal Lightbox */}
      <ImageModal image={modalImage} onClose={() => setModalImage(null)} />
    </div>
  );
};

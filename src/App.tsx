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
  TutorialModule,
  TutorialSection,
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

const sanitizeManifestItem = (raw: any): ExamManifestItem => {
  if (!raw || typeof raw !== 'object') {
    return {
      id: 'unknown',
      title: '未命名試卷',
      sourceCategory: '未分類',
      questionCount: 0,
      year: 2026,
    };
  }
  const id = raw.id || raw.paperId || 'unknown_paper';
  const title = raw.title || raw.name || raw.paperTitle || id;
  const sourceCategory = raw.sourceCategory || raw.category || '2026 年主題練習';
  const questionCount = typeof raw.questionCount === 'number' ? raw.questionCount : (raw.totalQuestions || 0);
  const year = raw.year || 2026;
  const filename = raw.filename || `${id}.json`;

  return {
    ...raw,
    id,
    title,
    sourceCategory,
    questionCount,
    year,
    filename,
  };
};

const normalizePaperData = (paperData: any, itemOrId: string | ExamManifestItem): ExamPaper => {
  const itemId = typeof itemOrId === 'string' ? itemOrId : itemOrId.id;
  const itemTitle = typeof itemOrId === 'string' ? itemOrId : itemOrId.title;
  const itemCategory = typeof itemOrId === 'string' ? '' : itemOrId.sourceCategory;
  const itemYear = typeof itemOrId === 'string' ? 2026 : itemOrId.year;

  const rawQuestions = Array.isArray(paperData) ? paperData : (paperData.questions || []);
  const questions = rawQuestions.map((q: any, qIdx: number) => ({
    ...q,
    number: q.number || qIdx + 1,
    options: (q.options || []).map((opt: any, optIdx: number) => {
      if (typeof opt === 'string') {
        const letters: OptionId[] = ['A', 'B', 'C', 'D', 'E'];
        return { id: letters[optIdx] || 'A', text: opt };
      }
      return opt;
    }),
  }));

  return {
    id: paperData.id || paperData.paperId || itemId,
    title: paperData.title || paperData.paperTitle || itemTitle,
    rawTitle: paperData.rawTitle || paperData.paperTitle || itemTitle,
    sourceCategory: paperData.sourceCategory || paperData.category || itemCategory,
    year: paperData.year || itemYear || 2026,
    questionCount: paperData.questionCount || paperData.totalQuestions || questions.length,
    createdAt: paperData.createdAt || new Date().toISOString(),
    questions,
  };
};

  // Load Manifest & Preload All Paper JSONs for Global Analytics
  useEffect(() => {
    fetch('/server-data/exams_manifest.json')
      .then((res) => (res.ok ? res.json() : null))
      .then(async (manifestData: ExamManifestItem[]) => {
        if (manifestData && Array.isArray(manifestData) && manifestData.length > 0) {
          const sanitizedManifest = manifestData.map(sanitizeManifestItem);
          setManifest(sanitizedManifest);

          // Preload paper JSONs
          const loadedMap: Record<string, ExamPaper> = {};
          await Promise.all(
            sanitizedManifest.map((item) => {
              if (!item || !item.id) return Promise.resolve();
              const filename = item.filename || `${item.id}.json`;
              const url = filename.startsWith('/') ? filename : `/server-data/${filename}`;
              return fetch(url)
                .then((r) => (r.ok ? r.json() : fetch(`/server-data/${item.id}.json`).then((r2) => (r2.ok ? r2.json() : null))))
                .then((paperData: any) => {
                  if (paperData) {
                    const normalizedPaper = normalizePaperData(paperData, item);
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
        const parsed = JSON.parse(saved);
        if (parsed && typeof parsed === 'object' && parsed.answers && typeof parsed.answers === 'object') {
          setAttemptState({
            paperId: parsed.paperId || selectedPaperId,
            answers: parsed.answers || {},
            flagged: parsed.flagged || {},
            startTime: parsed.startTime || Date.now(),
            elapsedSeconds: parsed.elapsedSeconds || 0,
            isSubmitted: !!parsed.isSubmitted,
            submittedAt: parsed.submittedAt || null,
          });
          return;
        }
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
    if (attemptState && attemptState.paperId === selectedPaperId) {
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

  // On-demand paper loader helper
  const ensurePaperLoaded = useCallback(
    async (paperId: string): Promise<ExamPaper | null> => {
      if (!paperId) return null;
      if (allPapersMap[paperId]) {
        return allPapersMap[paperId];
      }
      try {
        const manifestItem = manifest.find((m) => m.id === paperId || (m as any).paperId === paperId);
        const filename = manifestItem?.filename || `${paperId}.json`;
        const url = filename.startsWith('/') ? filename : `/server-data/${filename}`;
        let res = await fetch(url);
        if (!res.ok) {
          res = await fetch(`/server-data/${paperId}.json`);
          if (!res.ok) return null;
        }
        const data = await res.json();
        const normalized = normalizePaperData(data, manifestItem || paperId);
        setAllPapersMap((prev) => ({ ...prev, [paperId]: normalized }));
        return normalized;
      } catch (e) {
        console.error('Failed to load paper on demand:', e);
        return null;
      }
    },
    [allPapersMap, manifest]
  );

  // Unified Select Paper Handler
  const handleSelectPaper = useCallback(
    async (paperId: string) => {
      if (!paperId) return;
      setSelectedPaperId(paperId);
      setFilterMode('all');
      setCurrentIndex(0);

      let paper = allPapersMap[paperId];
      if (!paper) {
        paper = (await ensurePaperLoaded(paperId)) || currentPaper;
      }
      if (paper) {
        setCurrentPaper(paper);
      }
      setCurrentView('exam');
    },
    [allPapersMap, currentPaper, ensurePaperLoaded]
  );

  // Handle Paper Selection Change & Fallback Load
  useEffect(() => {
    if (!selectedPaperId) return;
    const paper = allPapersMap[selectedPaperId];
    if (paper) {
      setCurrentPaper(paper);
      setCurrentIndex(0);
      setFilterMode('all');
    } else {
      ensurePaperLoaded(selectedPaperId).then((loaded) => {
        if (loaded) {
          setCurrentPaper(loaded);
          setCurrentIndex(0);
          setFilterMode('all');
        }
      });
    }
  }, [selectedPaperId, allPapersMap, ensurePaperLoaded]);

  // Select Tutorial from Dashboard
  const handleSelectTutorialFromDashboard = (paperId: string) => {
    if (!paperId) return;
    const manifestItem = manifest.find((item) => item.id === paperId || (item as any).paperId === paperId);
    
    // Build candidate fetch URLs in order of specificity
    const candidates: string[] = [];
    if (manifestItem?.tutorialPath) {
      candidates.push(
        manifestItem.tutorialPath.startsWith('/')
          ? manifestItem.tutorialPath
          : `/${manifestItem.tutorialPath}`
      );
    }
    if (manifestItem?.tutorialFilename) {
      const fn = manifestItem.tutorialFilename;
      candidates.push(fn.startsWith('/') ? fn : `/server-data/${fn}`);
    }
    if (manifestItem?.tutorialId) {
      const tutId = manifestItem.tutorialId;
      if (tutId.endsWith('.json')) {
        candidates.push(`/server-data/tutorials/${tutId}`);
      } else if (tutId.endsWith('_tutorial')) {
        candidates.push(`/server-data/tutorials/${tutId}.json`);
      } else {
        candidates.push(`/server-data/tutorials/${tutId}_tutorial.json`);
        candidates.push(`/server-data/tutorials/${tutId}.json`);
      }
    }

    // Standard fallbacks
    candidates.push(`/server-data/tutorials/${paperId}_tutorial.json`);
    candidates.push(`/server-data/tutorials/${paperId}.json`);

    const uniqueCandidates = Array.from(new Set(candidates));

    const tryFetch = async (urls: string[]): Promise<any | null> => {
      for (const url of urls) {
        try {
          const res = await fetch(url);
          if (res.ok) {
            const json = await res.json();
            if (json) return json;
          }
        } catch (e) {
          /* ignore & continue */
        }
      }
      return null;
    };

    tryFetch(uniqueCandidates)
      .then((data: any) => {
        if (!data) {
          alert('該試卷的主題式備考教學載入失敗或尚在編寫中');
          return;
        }

        // Normalize tutorial modules / sections into unified TutorialModule[] format
        const rawModules = data.modules || data.sections || [];
        if (!Array.isArray(rawModules) || rawModules.length === 0) {
          alert('該試卷的主題式備考教學載入失敗或尚在編寫中');
          return;
        }

        const normalizedModules: TutorialModule[] = rawModules.map((mod: any, idx: number) => {
          const modId = mod.moduleId || mod.id || `module-${idx + 1}`;
          const modTitle = mod.moduleTitle || mod.title || `Module ${idx + 1}`;
          const studyGuide = mod.studyGuide || mod.description || '';
          const diagrams = mod.diagrams || [];

          let sections: TutorialSection[] = [];
          if (mod.sections && Array.isArray(mod.sections) && mod.sections.length > 0) {
            sections = mod.sections;
          } else if (mod.content) {
            sections = [
              {
                heading: mod.title || modTitle,
                content: mod.content,
                diagrams: mod.diagrams || [],
              },
            ];
          }

          return {
            moduleId: modId,
            moduleTitle: modTitle,
            studyGuide,
            diagrams,
            sections,
            relatedQuestionIds: mod.relatedQuestionIds || [],
          };
        });

        const normalizedTutorial: ExamTutorial = {
          id: data.id || paperId,
          paperId: data.paperId || paperId,
          title: data.title || manifestItem?.title || paperId,
          sourceCategory: data.sourceCategory || manifestItem?.sourceCategory || '主題式備考教學',
          year: data.year || manifestItem?.year || 2026,
          updatedAt: data.updatedAt || new Date().toISOString(),
          modules: normalizedModules,
        };

        setActiveTutorial(normalizedTutorial);
        setCurrentView('tutorial');
      })
      .catch((e) => {
        console.error('Failed to load tutorial:', e);
        alert('主題式備考教學載入失敗');
      });
  };

  // Filtered Questions in Active Exam & Defensive Fallbacks
  const safeQuestions = Array.isArray(currentPaper?.questions) ? currentPaper.questions : [];
  const safeAnswers = attemptState?.answers || {};
  const safeFlagged = attemptState?.flagged || {};
  const isEffectiveSubmitted = !!attemptState?.isSubmitted || studyMode === 'work';

  const filteredQuestions = safeQuestions.filter((q) => {
    if (!q) return false;
    if (filterMode === 'disputed') {
      return q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED');
    }
    if (filterMode === 'wrong') {
      const userAns = safeAnswers[q.id];
      return q.sourceProvidedAnswer && userAns && userAns !== q.sourceProvidedAnswer;
    }
    return true;
  });

  const activeQuestion = filteredQuestions[currentIndex] || safeQuestions[0];

  // Actions
  const handleSelectOption = (optId: OptionId) => {
    if (attemptState?.isSubmitted || !activeQuestion) return;
    setAttemptState((prev) => ({
      ...prev,
      paperId: selectedPaperId,
      answers: {
        ...(prev?.answers || {}),
        [activeQuestion.id]: optId,
      },
      flagged: prev?.flagged || {},
      startTime: prev?.startTime || Date.now(),
      elapsedSeconds: prev?.elapsedSeconds || 0,
      isSubmitted: !!prev?.isSubmitted,
      submittedAt: prev?.submittedAt || null,
    }));
  };

  const handleToggleFlag = useCallback(() => {
    if (!activeQuestion) return;
    setAttemptState((prev) => ({
      ...prev,
      paperId: selectedPaperId,
      answers: prev?.answers || {},
      flagged: {
        ...(prev?.flagged || {}),
        [activeQuestion.id]: !(prev?.flagged || {})[activeQuestion.id],
      },
      startTime: prev?.startTime || Date.now(),
      elapsedSeconds: prev?.elapsedSeconds || 0,
      isSubmitted: !!prev?.isSubmitted,
      submittedAt: prev?.submittedAt || null,
    }));
  }, [activeQuestion, selectedPaperId]);

  const handleSubmitExam = () => {
    setAttemptState((prev) => ({
      paperId: selectedPaperId,
      answers: prev?.answers || {},
      flagged: prev?.flagged || {},
      startTime: prev?.startTime || Date.now(),
      elapsedSeconds: prev?.elapsedSeconds || 0,
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
  safeQuestions.forEach((q) => {
    if (q && q.sourceProvidedAnswer) {
      if (safeAnswers[q.id] === q.sourceProvidedAnswer || studyMode === 'work') {
        scoreCorrect++;
      }
    }
  });

  const activeDisputedCount = safeQuestions.filter((q) =>
    q && q.reconciliationStatus && q.reconciliationStatus.startsWith('DISPUTED')
  ).length;

  const answeredCount = Object.keys(safeAnswers).length;

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
        onSelectPaper={(id) => handleSelectPaper(id)}
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
            onSelectPaper={handleSelectPaper}
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
            onStartExam={handleSelectPaper}
          />
        </main>
      ) : (
        <main className="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 flex flex-col md:flex-row gap-6">
          {/* Left Panel: Matrix Grid */}
          <QuestionMatrix
            questions={filteredQuestions}
            currentIndex={currentIndex}
            onSelectIndex={(idx) => setCurrentIndex(idx)}
            userAnswers={safeAnswers}
            flagged={safeFlagged}
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
                  selectedOption={safeAnswers[activeQuestion.id]}
                  onSelectOption={handleSelectOption}
                  isFlagged={!!safeFlagged[activeQuestion.id]}
                  onToggleFlag={handleToggleFlag}
                  onPrev={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
                  onNext={() => setCurrentIndex((prev) => Math.min(filteredQuestions.length - 1, prev + 1))}
                  isSubmitted={!!attemptState?.isSubmitted}
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

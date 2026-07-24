import React, { useEffect, useState, useCallback } from 'react';
import { Header } from './components/Header';
import { QuestionMatrix } from './components/QuestionMatrix';
import { QuestionPanel } from './components/QuestionPanel';
import { ExplanationPanel } from './components/ExplanationPanel';
import { ImageModal } from './components/ImageModal';
import { ExamManifestItem, ExamPaper, ExamQuestion, OptionId, ResolvedImage, UserAttemptState } from './types/exam';

// Sample Fallback Exam Paper for Initial Demonstration
const MOCK_MANIFEST: ExamManifestItem[] = [
  {
    id: 'demo_2025_zhongshan',
    title: '2025 114出題表格_傳統題_中山吳勝文',
    sourceCategory: 'TSN 歷年交換題/2025 年交換題',
    questionCount: 3,
    year: 2025,
  },
];

const MOCK_PAPER: ExamPaper = {
  id: 'demo_2025_zhongshan',
  title: '2025 114出題表格_傳統題_中山吳勝文',
  rawTitle: '2025 114出題表格_傳統題_中山吳勝文 - 原檔',
  sourceCategory: 'TSN 歷年交換題/2025 年交換題',
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
        {
          notebookTitle: 'TSN：出題 (2-3)',
          notebookId: 'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
          accountProfile: 'sandbox0505',
          selectedOption: 'C',
          rawResponse: '1. Answer: (C) Lupus nephritis.\n2. Detailed Explanation: TTP, recurrent FSGS, and severe ANCA vasculitis with dialysis are classic primary indications for TPE, whereas LN is not standard primary therapy.\n3. Citations: Brenner 11e Chap 64.',
          citations: [{ chapter: 'Chap 64', page: '2133' }],
          figureMentions: [],
          databaseSufficiency: 'SUFFICIENT',
          error: null,
        },
      ],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '原始答案 (C) 與兩組 NotebookLM 檢索結果完全一致。',
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
      nlmResponses: [
        {
          notebookTitle: 'TSN：出題 (3-[1-5])',
          notebookId: 'b92401024-nb1',
          accountProfile: 'b92401024',
          selectedOption: 'C',
          rawResponse: '1. Answer: (C).\n2. Detailed Explanation: Clearance of large molecules is membrane-limited rather than flow-limited. Blood or dialysate flow rates mostly affect small molecule clearance.\n3. Citations: Brenner Chap 63 pg.2052-2054.',
          citations: [{ chapter: 'Chap 63', page: '2052-2054' }],
          figureMentions: [],
          databaseSufficiency: 'SUFFICIENT',
          error: null,
        },
      ],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '原始答案 (C) 與 NotebookLM 回答一致。',
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
      nlmResponses: [
        {
          notebookTitle: 'TSN：出題 (4-2)',
          notebookId: 'mudkaku-nb2',
          accountProfile: 'mudkaku',
          selectedOption: 'D',
          rawResponse: '1. Answer: (D).\n2. Detailed Explanation: Inadequate access, tubing kinking, and needle against wall increase resistance/suction causing excessively negative (low) arterial pressure, whereas dialyzer blood leak does not directly cause low pre-pump arterial pressure.\n3. Citations: Brenner 11e Chap 63.',
          citations: [{ chapter: 'Chap 63' }],
          figureMentions: [],
          databaseSufficiency: 'SUFFICIENT',
          error: null,
        },
      ],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '原始答案 (D) 與 NotebookLM 檢索一致。',
      resolvedImages: [],
    },
  ],
};

export const App: React.FC = () => {
  const [manifest, setManifest] = useState<ExamManifestItem[]>(MOCK_MANIFEST);
  const [selectedPaperId, setSelectedPaperId] = useState<string>(MOCK_PAPER.id);
  const [currentPaper, setCurrentPaper] = useState<ExamPaper>(MOCK_PAPER);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [filterMode, setFilterMode] = useState<'all' | 'disputed' | 'wrong'>('all');
  const [modalImage, setModalImage] = useState<ResolvedImage | null>(null);

  // User Attempt State (LocalStorage persisted)
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

  // Load Manifest
  useEffect(() => {
    fetch('/server-data/exams_manifest.json')
      .then((res) => (res.ok ? res.json() : null))
      .then((data) => {
        if (data && Array.isArray(data) && data.length > 0) {
          setManifest(data);
          if (!data.some((item: ExamManifestItem) => item.id === selectedPaperId)) {
            setSelectedPaperId(data[0].id);
          }
        }
      })
      .catch(() => {
        /* fallback to mock manifest */
      });
  }, []);

  // Load Selected Paper JSON
  useEffect(() => {
    if (selectedPaperId === MOCK_PAPER.id) {
      setCurrentPaper(MOCK_PAPER);
      return;
    }
    fetch(`/server-data/${selectedPaperId}.json`)
      .then((res) => (res.ok ? res.json() : null))
      .then((data: ExamPaper) => {
        if (data && data.questions) {
          setCurrentPaper(data);
          setCurrentIndex(0);
        }
      })
      .catch((err) => {
        console.warn('Could not load paper JSON, using mock fallback', err);
      });
  }, [selectedPaperId]);

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
    localStorage.setItem(`attempt_${selectedPaperId}`, JSON.stringify(attemptState));
  }, [attemptState, selectedPaperId]);

  // Timer Effect (Elapsed正計時)
  useEffect(() => {
    if (attemptState.isSubmitted) return;
    const timer = setInterval(() => {
      setAttemptState((prev) => ({
        ...prev,
        elapsedSeconds: prev.elapsedSeconds + 1,
      }));
    }, 1000);
    return () => clearInterval(timer);
  }, [attemptState.isSubmitted]);

  // Derived filtered questions list
  const filteredQuestions = currentPaper.questions.filter((q) => {
    if (filterMode === 'disputed') {
      return q.reconciliationStatus.startsWith('DISPUTED');
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
    if (attemptState.isSubmitted) return;
    setAttemptState((prev) => ({
      ...prev,
      answers: {
        ...prev.answers,
        [activeQuestion.id]: optId,
      },
    }));
  };

  const handleToggleFlag = () => {
    setAttemptState((prev) => ({
      ...prev,
      flagged: {
        ...prev.flagged,
        [activeQuestion.id]: !prev.flagged[activeQuestion.id],
      },
    }));
  };

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

  // Compute Score
  let scoreCorrect = 0;
  currentPaper.questions.forEach((q) => {
    if (q.sourceProvidedAnswer && attemptState.answers[q.id] === q.sourceProvidedAnswer) {
      scoreCorrect++;
    }
  });

  const disputedCount = currentPaper.questions.filter((q) =>
    q.reconciliationStatus.startsWith('DISPUTED')
  ).length;

  const answeredCount = Object.keys(attemptState.answers).length;

  // Keyboard Shortcuts
  const handleKeyDown = useCallback(
    (e: KeyboardEvent) => {
      if (e.key === 'ArrowLeft') {
        setCurrentIndex((prev) => Math.max(0, prev - 1));
      } else if (e.key === 'ArrowRight') {
        setCurrentIndex((prev) => Math.min(filteredQuestions.length - 1, prev + 1));
      } else if (!attemptState.isSubmitted && ['a', 'b', 'c', 'd', 'e'].includes(e.key.toLowerCase())) {
        const opt = e.key.toUpperCase() as OptionId;
        if (activeQuestion.options.some((o) => o.id === opt)) {
          handleSelectOption(opt);
        }
      }
    },
    [filteredQuestions.length, attemptState.isSubmitted, activeQuestion]
  );

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 font-sans selection:bg-cyan-500 selection:text-slate-950">
      {/* Top Header */}
      <Header
        manifest={manifest}
        selectedPaperId={selectedPaperId}
        onSelectPaper={(id) => setSelectedPaperId(id)}
        elapsedSeconds={attemptState.elapsedSeconds}
        totalQuestions={currentPaper.questions.length}
        answeredCount={answeredCount}
        isSubmitted={attemptState.isSubmitted}
        scoreCorrect={scoreCorrect}
        disputedCount={disputedCount}
        filterMode={filterMode}
        onFilterChange={setFilterMode}
        onReset={handleReset}
        onSubmitExam={handleSubmitExam}
      />

      {/* Main Body */}
      <main className="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 flex flex-col md:flex-row gap-6">
        {/* Left Panel: Matrix Grid */}
        <QuestionMatrix
          questions={filteredQuestions}
          currentIndex={currentIndex}
          onSelectIndex={(idx) => setCurrentIndex(idx)}
          userAnswers={attemptState.answers}
          flagged={attemptState.flagged}
          isSubmitted={attemptState.isSubmitted}
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
                isSubmitted={attemptState.isSubmitted}
              />

              {/* Show Explanation Panel after Submission or in Review */}
              {attemptState.isSubmitted && (
                <ExplanationPanel
                  question={activeQuestion}
                  onOpenImage={(img) => setModalImage(img)}
                />
              )}
            </>
          ) : (
            <div className="glass-panel rounded-2xl p-12 text-center text-slate-400">
              篩選條件下無符合的題目
            </div>
          )}
        </div>
      </main>

      {/* Image Modal Lightbox */}
      <ImageModal image={modalImage} onClose={() => setModalImage(null)} />
    </div>
  );
};

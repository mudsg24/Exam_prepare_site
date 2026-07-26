export type OptionId = 'A' | 'B' | 'C' | 'D' | 'E';

export interface QuestionOption {
  id: OptionId;
  text: string;
}

export interface NlmCitation {
  chapter?: string;
  page?: string;
  figureOrTable?: string;
  textSnippet?: string;
}

export interface NlmResponseItem {
  notebookTitle: string;
  notebookId: string;
  accountProfile: string;
  selectedOption: string | null;
  rawResponse: string;
  formattedResponse?: string;
  citations: NlmCitation[];
  figureMentions: string[];
  databaseSufficiency: 'SUFFICIENT' | 'INSUFFICIENT';
  error: string | null;
}

export type DisputeStatus = 
  | 'HIGH_CONFIDENCE'              // Source & 2 NLMs agree
  | 'DISPUTED_SOURCE_VS_NLM'        // Source differs from NLM
  | 'DISPUTED_NLM_VS_NLM'          // NLM 1 differs from NLM 2
  | 'UNVERIFIED'                   // No source answer & NLM insufficient
  | 'INSUFFICIENT_EVIDENCE';       // NLM evidence insufficient

export interface ResolvedImage {
  id: string;
  title: string;
  bookSource: 'KDIGO' | 'Brenner 11e';
  relPath: string;
  absPath: string;
}

export interface AttachedImage {
  id: string;
  fileName: string;
  relPath: string;
  caption?: string;
}

export interface CodexExplanation {
  explanationZh?: string;
  optionAnalysisZh?: Record<string, string>;
  authorityEvidence?: Array<{
    source: string;
    locator: string;
    note_zh?: string;
  }>;
  sourceNotesZh?: string;
}

export interface ExamQuestion {
  id: string;
  number: number;
  stem: string;
  options: QuestionOption[];
  sourceAnswerStatus: 'provided' | 'absent' | 'ambiguous' | 'synthetic_tonks';
  sourceProvidedAnswer: OptionId | null;
  sourceExplanation?: string | null;
  codexExplanation?: CodexExplanation;
  nlmResponses: NlmResponseItem[];
  reconciliationStatus: DisputeStatus;
  reconciliationNotes: string;
  resolvedImages: ResolvedImage[];
  attachedImages?: AttachedImage[];
}

export interface ExamPaper {
  id: string;
  title: string;
  rawTitle: string;
  sourceCategory: string;
  year: number;
  questionCount: number;
  createdAt: string;
  questions: ExamQuestion[];
}

export interface ExamManifestItem {
  id: string;
  title: string;
  sourceCategory: string;
  questionCount: number;
  year: number;
}

export interface UserAttemptState {
  paperId: string;
  answers: Record<string, OptionId>; // questionId -> optionId
  flagged: Record<string, boolean>;  // questionId -> isFlagged
  startTime: number;
  elapsedSeconds: number;
  isSubmitted: boolean;
  submittedAt: number | null;
}

export type ThemeMode = 'light' | 'dark';
export type AppView = 'dashboard' | 'exam';
export type StudyMode = 'practice' | 'work';

export interface GlobalPracticeStats {
  totalQuestions: number;
  completedQuestions: number;
  correctCount: number;
  wrongCount: number;
  unattemptedCount: number;
  disputedCount: number;
}

export type CustomPracticeType = 'unattempted' | 'wrong' | 'disputed' | 'paper';



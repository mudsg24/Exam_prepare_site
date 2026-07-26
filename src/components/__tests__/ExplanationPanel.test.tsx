import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ExplanationPanel } from '../ExplanationPanel';
import { ExamQuestion } from '../../types/exam';
import { marked } from 'marked';

describe('ExplanationPanel Component', () => {
  const mockQuestion: ExamQuestion = {
    id: 'q1',
    number: 1,
    stem: 'IgAN Test Question',
    options: [
      { id: 'A', text: 'Option A' },
      { id: 'B', text: 'Option B' },
    ],
    sourceAnswerStatus: 'provided',
    sourceProvidedAnswer: 'B',
    codexExplanation: {
      explanationZh: 'Codex 核心解析內容',
      optionAnalysisZh: {
        A: '選項 A 錯誤解析',
        B: '選項 B 正確解析',
      },
      authorityEvidence: [
        { source: 'KDIGO 2024', locator: 'Chapter 12, S120', note_zh: '考點依據' },
      ],
    },
    nlmResponses: [
      {
        notebookTitle: 'KDIGO Notebook',
        notebookId: 'nb_1',
        accountProfile: 'Profile 1',
        selectedOption: 'B',
        rawResponse: 'AskResult(answer="## 1. 診斷\\n選項 B 正確。\\n## 2. 治療\\nSGLT2i 為首選。", turn_number=1, raw_response="raw")',
        formattedResponse: '## 1. 診斷\n選項 B 正確。\n## 2. 治療\nSGLT2i 為首選。',
        citations: [{ chapter: 'IgAN', page: '120' }],
        figureMentions: [],
        databaseSufficiency: 'SUFFICIENT',
        error: null,
      },
      {
        notebookTitle: 'Brenner Notebook',
        notebookId: 'nb_2',
        accountProfile: 'Profile 2',
        selectedOption: 'B',
        rawResponse: 'Single paragraph response without headers.',
        citations: [],
        figureMentions: [],
        databaseSufficiency: 'SUFFICIENT',
        error: null,
      },
    ],
    reconciliationStatus: 'HIGH_CONFIDENCE',
    reconciliationNotes: '三方答案一致 (B)',
    resolvedImages: [
      {
        id: 'res_1',
        title: 'KDIGO Figure 12',
        bookSource: 'KDIGO',
        relPath: 'KDIGO/fig12.png',
        absPath: '/abs/fig12.png',
      },
    ],
  };

  const defaultProps = {
    question: mockQuestion,
    onOpenImage: vi.fn(),
    themeMode: 'light' as const,
  };

  it('should render ground truth banner, Codex rationale, NLM tabs, and reference images', () => {
    render(<ExplanationPanel {...defaultProps} />);

    expect(screen.getByText('答案選項 (B)')).toBeInTheDocument();
    expect(screen.getByText('三方答案一致 (B)')).toBeInTheDocument();
    expect(screen.getByText('🏆 腎專聯合研析組 Codex 正式解析與選項剖析', { exact: false })).toBeInTheDocument();
    expect(screen.getByText('Codex 核心解析內容')).toBeInTheDocument();
    expect(screen.getByText('KDIGO Notebook (NLM選 B)')).toBeInTheDocument();
    expect(screen.getByText('KDIGO Figure 12')).toBeInTheDocument();
  });

  it('should clean AskResult raw text format correctly', () => {
    const askResultQuestion: ExamQuestion = {
      ...mockQuestion,
      nlmResponses: [
        {
          notebookTitle: 'Clean Test',
          notebookId: 'nb_clean',
          accountProfile: 'Profile 1',
          selectedOption: 'A',
          rawResponse: 'AskResult(answer="Answer content here", turn_number=1, raw_response="raw")',
          formattedResponse: 'AskResult(answer="Answer content here", turn_number=1, raw_response="raw")',
          citations: [],
          figureMentions: [],
          databaseSufficiency: 'SUFFICIENT',
          error: null,
        },
      ],
    };
    render(<ExplanationPanel {...defaultProps} question={askResultQuestion} />);
    expect(screen.getByText('Answer content here')).toBeInTheDocument();
  });

  it('should handle synthetic tonks answer banner', () => {
    const syntheticQuestion: ExamQuestion = {
      ...mockQuestion,
      sourceAnswerStatus: 'synthetic_tonks',
      sourceProvidedAnswer: 'A',
    };
    render(<ExplanationPanel {...defaultProps} question={syntheticQuestion} />);
    expect(screen.getByText('Tonks 擬真命題正解')).toBeInTheDocument();
  });

  it('should handle absent source answer banner', () => {
    const absentQuestion: ExamQuestion = {
      ...mockQuestion,
      sourceAnswerStatus: 'absent',
      sourceProvidedAnswer: null,
    };
    render(<ExplanationPanel {...defaultProps} question={absentQuestion} />);
    expect(screen.getByText('原始檔案未標記解答 (無 Ground Truth)')).toBeInTheDocument();
  });

  it('should switch active NLM tab when clicking tab buttons', () => {
    render(<ExplanationPanel {...defaultProps} />);

    const brennerTab = screen.getByText('Brenner Notebook (NLM選 B)');
    fireEvent.click(brennerTab);

    expect(screen.getByText('Single paragraph response without headers.')).toBeInTheDocument();
  });

  it('should toggle accordion sections in NLM response', () => {
    render(<ExplanationPanel {...defaultProps} />);

    const sectionHeader = screen.getByText('1. 診斷');
    fireEvent.click(sectionHeader); // collapse
    fireEvent.click(sectionHeader); // expand again
  });

  it('should trigger onOpenImage when clicking reference image card', () => {
    render(<ExplanationPanel {...defaultProps} />);

    const imgBtn = screen.getByText('KDIGO Figure 12');
    fireEvent.click(imgBtn);

    expect(defaultProps.onOpenImage).toHaveBeenCalledWith(mockQuestion.resolvedImages[0]);
  });

  it('should render fallback when nlmResponses is empty', () => {
    const noNlmQuestion: ExamQuestion = {
      ...mockQuestion,
      nlmResponses: [],
    };
    render(<ExplanationPanel {...defaultProps} question={noNlmQuestion} />);
    expect(screen.getByText('尚無 NotebookLM 的回答資料')).toBeInTheDocument();
  });

  it('should handle markdown parser error gracefully in renderFormattedMarkdown', () => {
    const spy = vi.spyOn(marked, 'parse').mockImplementation(() => {
      throw new Error('Markdown error');
    });

    render(<ExplanationPanel {...defaultProps} />);
    expect(screen.getByText('答案選項 (B)')).toBeInTheDocument();

    spy.mockRestore();
  });

  it('should render Gemini official rationale for synthetic_tonks question with sourceExplanation', () => {
    const syntheticTonksQuestion: ExamQuestion = {
      ...mockQuestion,
      sourceAnswerStatus: 'synthetic_tonks',
      sourceExplanation: 'Gemini 專責極度詳細病理機轉解析內容',
    };

    render(<ExplanationPanel {...defaultProps} question={syntheticTonksQuestion} />);

    expect(screen.getByText('✨ Gemini 專責正式解析')).toBeInTheDocument();
    expect(screen.getByText('Gemini Official Rationale')).toBeInTheDocument();
    expect(screen.getByText('Gemini 專責極度詳細病理機轉解析內容')).toBeInTheDocument();
  });

  it('should render source explanation note for traditional paper with sourceExplanation', () => {
    const sourceExpQuestion: ExamQuestion = {
      ...mockQuestion,
      sourceAnswerStatus: 'provided',
      sourceExplanation: 'The Kidney Brenner 11th Chap 64 page 2133',
    };

    render(<ExplanationPanel {...defaultProps} question={sourceExpQuestion} />);

    expect(screen.getByText('📖 原始考題解析／出處備註')).toBeInTheDocument();
    expect(screen.getByText('Source Explanation')).toBeInTheDocument();
    expect(screen.getByText('The Kidney Brenner 11th Chap 64 page 2133')).toBeInTheDocument();
  });
});

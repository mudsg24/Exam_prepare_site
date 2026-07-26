import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { QuestionPanel } from '../QuestionPanel';
import { ExamQuestion } from '../../types/exam';
import { marked } from 'marked';

describe('QuestionPanel Component', () => {
  const mockQuestion: ExamQuestion = {
    id: 'q1',
    number: 1,
    stem: '關於 <strong>IgAN</strong> 的敘述，<em>何者正確</em>？ $[x^2]$ ![figure](fig.png)',
    options: [
      { id: 'A', text: '選項 A 內容' },
      { id: 'B', text: '選項 B 內容' },
    ],
    sourceAnswerStatus: 'provided',
    sourceProvidedAnswer: 'A',
    nlmResponses: [],
    reconciliationStatus: 'HIGH_CONFIDENCE',
    reconciliationNotes: 'Matched',
    resolvedImages: [],
    attachedImages: [
      { id: 'img_1', fileName: 'sample.png', relPath: 'sample.png', caption: '附圖標題' },
      // @ts-expect-error test string fallback normalization
      'attached/legacy_string_image.png',
    ],
  };

  const defaultProps = {
    question: mockQuestion,
    currentIndex: 0,
    totalQuestions: 5,
    selectedOption: undefined,
    onSelectOption: vi.fn(),
    isFlagged: false,
    onToggleFlag: vi.fn(),
    onPrev: vi.fn(),
    onNext: vi.fn(),
    isSubmitted: false,
    themeMode: 'light' as const,
    onOpenAttachedImage: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render question number, stem text, options, and navigation buttons', () => {
    render(<QuestionPanel {...defaultProps} />);

    expect(screen.getByText('第 1 題')).toBeInTheDocument();
    expect(screen.getByText('選項 A 內容')).toBeInTheDocument();
    expect(screen.getByText('選項 B 內容')).toBeInTheDocument();
    expect(screen.getByText('上一題')).toBeInTheDocument();
    expect(screen.getByText('下一題')).toBeInTheDocument();
  });

  it('should trigger onSelectOption when clicking an option prior to submission', () => {
    render(<QuestionPanel {...defaultProps} />);

    const optA = screen.getByText('選項 A 內容');
    fireEvent.click(optA);
    expect(defaultProps.onSelectOption).toHaveBeenCalledWith('A');
  });

  it('should disable options and display correct answer badge when submitted', () => {
    render(<QuestionPanel {...defaultProps} isSubmitted={true} selectedOption="B" />);

    expect(screen.getByText('正確答案')).toBeInTheDocument();
    expect(screen.getByText('高信心 (三方一致)')).toBeInTheDocument();

    const optA = screen.getByText('選項 A 內容');
    fireEvent.click(optA);
    expect(defaultProps.onSelectOption).not.toHaveBeenCalled();
  });

  it('should render selected option styling when sourceProvidedAnswer is missing and submitted', () => {
    const noAnswerQuestion: ExamQuestion = {
      ...mockQuestion,
      sourceProvidedAnswer: null,
      sourceAnswerStatus: 'absent',
    };
    render(<QuestionPanel {...defaultProps} question={noAnswerQuestion} isSubmitted={true} selectedOption="A" />);

    expect(screen.getByText('選項 A 內容')).toBeInTheDocument();
  });

  it('should handle toggle flag button click', () => {
    const { rerender } = render(<QuestionPanel {...defaultProps} isFlagged={false} />);
    const flagBtn = screen.getByText('標記此題');
    fireEvent.click(flagBtn);
    expect(defaultProps.onToggleFlag).toHaveBeenCalled();

    rerender(<QuestionPanel {...defaultProps} isFlagged={true} />);
    expect(screen.getByText('已標記')).toBeInTheDocument();
  });

  it('should trigger onPrev and onNext button clicks', () => {
    render(<QuestionPanel {...defaultProps} currentIndex={1} totalQuestions={5} />);

    const prevBtn = screen.getByText('上一題');
    fireEvent.click(prevBtn);
    expect(defaultProps.onPrev).toHaveBeenCalled();

    const nextBtn = screen.getByText('下一題');
    fireEvent.click(nextBtn);
    expect(defaultProps.onNext).toHaveBeenCalled();
  });

  it('should disable prev button on first question and next button on last question', () => {
    const { rerender } = render(<QuestionPanel {...defaultProps} currentIndex={0} totalQuestions={5} />);
    expect(screen.getByText('上一題').closest('button')).toBeDisabled();

    rerender(<QuestionPanel {...defaultProps} currentIndex={4} totalQuestions={5} />);
    expect(screen.getByText('下一題').closest('button')).toBeDisabled();
  });

  it('should trigger onOpenAttachedImage when clicking attached image thumbnail', () => {
    render(<QuestionPanel {...defaultProps} />);

    const attachedImgBtn = screen.getByText('附圖標題');
    fireEvent.click(attachedImgBtn);
    expect(defaultProps.onOpenAttachedImage).toHaveBeenCalled();
  });

  it('should handle markdown parser error in renderFormattedText gracefully', () => {
    const spy = vi.spyOn(marked, 'parse').mockImplementation(() => {
      throw new Error('Markdown parse error');
    });

    render(<QuestionPanel {...defaultProps} />);
    expect(screen.getByText('第 1 題')).toBeInTheDocument();

    spy.mockRestore();
  });
});

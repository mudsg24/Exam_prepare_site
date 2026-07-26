import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { QuestionMatrix } from '../QuestionMatrix';
import { ExamQuestion } from '../../types/exam';

describe('QuestionMatrix Component', () => {
  const mockQuestions: ExamQuestion[] = [
    {
      id: 'q1',
      number: 1,
      stem: 'Question 1',
      options: [{ id: 'A', text: 'Opt A' }, { id: 'B', text: 'Opt B' }],
      sourceAnswerStatus: 'provided',
      sourceProvidedAnswer: 'A',
      nlmResponses: [],
      reconciliationStatus: 'HIGH_CONFIDENCE',
      reconciliationNotes: '',
      resolvedImages: [],
    },
    {
      id: 'q2',
      number: 2,
      stem: 'Question 2',
      options: [{ id: 'A', text: 'Opt A' }, { id: 'B', text: 'Opt B' }],
      sourceAnswerStatus: 'provided',
      sourceProvidedAnswer: 'B',
      nlmResponses: [],
      reconciliationStatus: 'DISPUTED_SOURCE_VS_NLM',
      reconciliationNotes: '',
      resolvedImages: [],
    },
    {
      id: 'q3',
      number: 3,
      stem: 'Question 3',
      options: [{ id: 'A', text: 'Opt A' }, { id: 'B', text: 'Opt B' }],
      sourceAnswerStatus: 'absent',
      sourceProvidedAnswer: null,
      nlmResponses: [],
      reconciliationStatus: 'UNVERIFIED',
      reconciliationNotes: '',
      resolvedImages: [],
    },
  ];

  it('should render questions grid and total count', () => {
    render(
      <QuestionMatrix
        questions={mockQuestions}
        currentIndex={0}
        onSelectIndex={vi.fn()}
        userAnswers={{}}
        flagged={{}}
        isSubmitted={false}
        themeMode="light"
      />
    );

    expect(screen.getByText('題目列表')).toBeInTheDocument();
    expect(screen.getByText('(3 題)')).toBeInTheDocument();
    expect(screen.getByText('1')).toBeInTheDocument();
    expect(screen.getByText('2')).toBeInTheDocument();
    expect(screen.getByText('3')).toBeInTheDocument();
  });

  it('should invoke onSelectIndex when clicking a question box', () => {
    const onSelectIndexMock = vi.fn();
    render(
      <QuestionMatrix
        questions={mockQuestions}
        currentIndex={0}
        onSelectIndex={onSelectIndexMock}
        userAnswers={{}}
        flagged={{}}
        isSubmitted={false}
        themeMode="light"
      />
    );

    fireEvent.click(screen.getByText('2'));
    expect(onSelectIndexMock).toHaveBeenCalledWith(1);
  });

  it('should render flagged icon when question is flagged', () => {
    const { container } = render(
      <QuestionMatrix
        questions={mockQuestions}
        currentIndex={0}
        onSelectIndex={vi.fn()}
        userAnswers={{}}
        flagged={{ q1: true }}
        isSubmitted={false}
        themeMode="light"
      />
    );

    const button1 = screen.getByText('1').closest('button');
    expect(button1?.querySelector('.fill-amber-500')).toBeInTheDocument();
  });

  it('should render correct/wrong icons and disputed alerts when submitted', () => {
    render(
      <QuestionMatrix
        questions={mockQuestions}
        currentIndex={0}
        onSelectIndex={vi.fn()}
        userAnswers={{ q1: 'A', q2: 'A', q3: 'B' }} // q1 correct, q2 wrong (answer B), q3 answered but no source answer
        flagged={{}}
        isSubmitted={true}
        themeMode="dark"
      />
    );

    expect(screen.getByTitle('此題有爭議')).toBeInTheDocument();
    expect(screen.getByText('答對')).toBeInTheDocument();
    expect(screen.getByText('答錯')).toBeInTheDocument();
  });
});

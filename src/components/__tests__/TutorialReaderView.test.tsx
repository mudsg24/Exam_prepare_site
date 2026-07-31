import React from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import { TutorialReaderView } from '../TutorialReaderView';
import { ExamTutorial } from '../../types/exam';

describe('TutorialReaderView Keyboard Shortcuts', () => {
  const mockTutorial: ExamTutorial = {
    id: 'tut_1',
    paperId: 'paper_1',
    title: '電解質異常講堂',
    sourceCategory: '2026 年考訊重點',
    year: 2026,
    updatedAt: '2026-07-31',
    modules: [
      {
        moduleId: 'mod_1',
        moduleTitle: '第一章：高血鉀機轉',
        studyGuide: '摘要 1',
        diagrams: [],
        sections: [
          {
            heading: 'Section 1 Title',
            content: 'Section 1 content body',
          },
        ],
      },
      {
        moduleId: 'mod_2',
        moduleTitle: '第二章：低血鉀機轉',
        studyGuide: '摘要 2',
        diagrams: [],
        sections: [
          {
            heading: 'Section 2 Title',
            content: 'Section 2 content body',
          },
        ],
      },
    ],
  };

  const defaultProps = {
    tutorial: mockTutorial,
    onBack: vi.fn(),
    onStartExam: vi.fn(),
    themeMode: 'light' as const,
    onOpenImageModal: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render tutorial title and initial module content', () => {
    render(<TutorialReaderView {...defaultProps} />);

    expect(screen.getByText('電解質異常講堂')).toBeInTheDocument();
    expect(screen.getAllByText('第一章：高血鉀機轉').length).toBeGreaterThan(0);
    expect(screen.getByText('Section 1 Title')).toBeInTheDocument();
  });

  it('should navigate modules using v / ArrowRight and z / ArrowLeft equivalents', () => {
    render(<TutorialReaderView {...defaultProps} />);

    // Press 'v' to move to module 2
    act(() => {
      fireEvent.keyDown(window, { key: 'v' });
    });
    expect(screen.getByText('Section 2 Title')).toBeInTheDocument();

    // Press 'z' to move back to module 1
    act(() => {
      fireEvent.keyDown(window, { key: 'z' });
    });
    expect(screen.getByText('Section 1 Title')).toBeInTheDocument();

    // Press 'ArrowRight' to move to module 2
    act(() => {
      fireEvent.keyDown(window, { key: 'ArrowRight' });
    });
    expect(screen.getByText('Section 2 Title')).toBeInTheDocument();

    // Press 'ArrowLeft' to move back to module 1
    act(() => {
      fireEvent.keyDown(window, { key: 'ArrowLeft' });
    });
    expect(screen.getByText('Section 1 Title')).toBeInTheDocument();
  });
});

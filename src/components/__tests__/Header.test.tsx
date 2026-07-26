import React from 'react';
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import { Header } from '../Header';
import { ExamManifestItem } from '../../types/exam';

describe('Header Component', () => {
  const mockManifest: ExamManifestItem[] = [
    {
      id: 'paper_2026_1',
      title: '2026 年專科試卷 (重點轉化)',
      sourceCategory: '2026 年重點轉化',
      questionCount: 50,
      year: 2026,
    },
    {
      id: 'paper_2025_1',
      title: '2025 年歷年試卷',
      sourceCategory: '歷年考題',
      questionCount: 100,
      year: 2025,
    },
  ];

  const defaultProps = {
    manifest: mockManifest,
    selectedPaperId: 'paper_2026_1',
    onSelectPaper: vi.fn(),
    elapsedSeconds: 125, // 02:05
    totalQuestions: 50,
    answeredCount: 20,
    isSubmitted: false,
    scoreCorrect: null,
    disputedCount: 3,
    filterMode: 'all' as const,
    onFilterChange: vi.fn(),
    onReset: vi.fn(),
    onSubmitExam: vi.fn(),
    currentView: 'exam' as const,
    onNavigateView: vi.fn(),
    themeMode: 'dark' as const,
    onToggleTheme: vi.fn(),
    studyMode: 'practice' as const,
    onToggleStudyMode: vi.fn(),
  };

  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it('should render brand title and update current time', () => {
    render(<Header {...defaultProps} />);
    expect(screen.getByText('TSN 腎臟專科刷題站')).toBeInTheDocument();
    expect(screen.getByText(/時間:/)).toBeInTheDocument();
    
    // Advance timers by 1 second inside act
    act(() => {
      vi.advanceTimersByTime(1000);
    });
  });

  it('should trigger navigation view callback', () => {
    render(<Header {...defaultProps} />);
    const homeBtn = screen.getByText('首頁入口');
    fireEvent.click(homeBtn);
    expect(defaultProps.onNavigateView).toHaveBeenCalledWith('dashboard');

    const examBtn = screen.getByText('答題測驗室');
    fireEvent.click(examBtn);
    expect(defaultProps.onNavigateView).toHaveBeenCalledWith('exam');
  });

  it('should handle paper selection dropdown', () => {
    render(<Header {...defaultProps} />);
    const select = screen.getByRole('combobox');
    fireEvent.change(select, { target: { value: 'paper_2025_1' } });
    expect(defaultProps.onSelectPaper).toHaveBeenCalledWith('paper_2025_1');
  });

  it('should handle empty manifest state', () => {
    render(<Header {...defaultProps} manifest={[]} />);
    expect(screen.getByText('載入試卷中...')).toBeInTheDocument();
  });

  it('should toggle study mode button', () => {
    render(<Header {...defaultProps} />);
    const modeBtn = screen.getByText('練習測驗中');
    fireEvent.click(modeBtn);
    expect(defaultProps.onToggleStudyMode).toHaveBeenCalled();
  });

  it('should render timer in practice mode', () => {
    render(<Header {...defaultProps} elapsedSeconds={125} />);
    expect(screen.getByText('02:05')).toBeInTheDocument();
  });

  it('should trigger reset and submit exam buttons', () => {
    render(<Header {...defaultProps} />);
    const resetBtn = screen.getByTitle('重新開始答題');
    fireEvent.click(resetBtn);
    expect(defaultProps.onReset).toHaveBeenCalled();

    const submitBtn = screen.getByText('送出看解答');
    fireEvent.click(submitBtn);
    expect(defaultProps.onSubmitExam).toHaveBeenCalled();
  });

  it('should render post-submission score and filter buttons when submitted', () => {
    render(
      <Header
        {...defaultProps}
        isSubmitted={true}
        scoreCorrect={42}
        disputedCount={5}
        filterMode="all"
      />
    );
    expect(screen.getByText('正解數: 42/50')).toBeInTheDocument();

    const disputedFilter = screen.getByText(/爭議 \(5\)/);
    fireEvent.click(disputedFilter);
    expect(defaultProps.onFilterChange).toHaveBeenCalledWith('disputed');

    const wrongFilter = screen.getByText('錯題');
    fireEvent.click(wrongFilter);
    expect(defaultProps.onFilterChange).toHaveBeenCalledWith('wrong');
  });

  it('should handle light theme rendering and toggle theme button', () => {
    render(<Header {...defaultProps} themeMode="light" />);
    const themeBtn = screen.getByTitle('切換至深色主題');
    fireEvent.click(themeBtn);
    expect(defaultProps.onToggleTheme).toHaveBeenCalled();
  });

  it('should handle dark theme rendering and toggle theme button', () => {
    render(<Header {...defaultProps} themeMode="dark" />);
    const themeBtn = screen.getByTitle('切換至明亮主題');
    fireEvent.click(themeBtn);
    expect(defaultProps.onToggleTheme).toHaveBeenCalled();
  });
});

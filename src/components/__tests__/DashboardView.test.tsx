import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import {
  DashboardView,
  sanitizePaperTitle,
  isKeyPointTransformationPaper,
} from '../DashboardView';
import { ExamManifestItem, GlobalPracticeStats } from '../../types/exam';

describe('DashboardView Component & Helpers', () => {
  describe('Helper Functions', () => {
    it('sanitizePaperTitle should strip "(重點轉化)" from title', () => {
      expect(sanitizePaperTitle('2026 大林 (重點轉化)')).toBe('2026 大林');
      expect(sanitizePaperTitle('Standard Title')).toBe('Standard Title');
      expect(sanitizePaperTitle('')).toBe('');
    });

    it('isKeyPointTransformationPaper should correctly identify key point papers', () => {
      const kp1: ExamManifestItem = { id: 'p1', title: '重點轉化 1', sourceCategory: '', questionCount: 10, year: 2026 };
      const kp2: ExamManifestItem = { id: 'p2', title: 'Paper 2', sourceCategory: '2026 重點轉化', questionCount: 10, year: 2026 };
      const kp3: ExamManifestItem = { id: 'p3_重點轉化', title: 'Paper 3', sourceCategory: '', questionCount: 10, year: 2026 };
      const std: ExamManifestItem = { id: 'p4', title: 'Standard Paper', sourceCategory: '歷年考題', questionCount: 10, year: 2025 };

      expect(isKeyPointTransformationPaper(kp1)).toBe(true);
      expect(isKeyPointTransformationPaper(kp2)).toBe(true);
      expect(isKeyPointTransformationPaper(kp3)).toBe(true);
      expect(isKeyPointTransformationPaper(std)).toBe(false);
    });
  });

  describe('DashboardView Rendering & Interaction', () => {
    const mockManifest: ExamManifestItem[] = [
      {
        id: 'paper_2026_kp1',
        title: '2026 重點轉化 B (重點轉化)',
        sourceCategory: '2026 年重點轉化',
        questionCount: 20,
        year: 2026,
      },
      {
        id: 'paper_2026_kp2',
        title: '2026 重點轉化 A (重點轉化)',
        sourceCategory: '2026 年重點轉化',
        questionCount: 15,
        year: 2026,
      },
      {
        id: 'paper_2025_std1',
        title: '2025 歷年考古題 B',
        sourceCategory: '歷年考題',
        questionCount: 50,
        year: 2025,
      },
      {
        id: 'paper_2025_std2',
        title: '2025 歷年考古題 A',
        sourceCategory: '歷年考題',
        questionCount: 40,
        year: 2025,
      },
    ];

    const mockStats: GlobalPracticeStats = {
      totalQuestions: 125,
      completedQuestions: 35,
      correctCount: 28,
      wrongCount: 7,
      unattemptedCount: 90,
      disputedCount: 5,
    };

    const mockPaperProgress = {
      paper_2026_kp1: { total: 20, answered: 20, correct: 18 },
      paper_2025_std1: { total: 50, answered: 15, correct: 10 },
    };

    const defaultProps = {
      manifest: mockManifest,
      stats: mockStats,
      onSelectPaper: vi.fn(),
      onStartCustomPractice: vi.fn(),
      paperProgressMap: mockPaperProgress,
      themeMode: 'light' as const,
    };

    it('should render global statistics correctly', () => {
      render(<DashboardView {...defaultProps} />);

      expect(screen.getByText('全站題庫總數')).toBeInTheDocument();
      expect(screen.getByText('80%')).toBeInTheDocument(); // 28 / 35 = 80%
      expect(screen.getAllByText(/35/).length).toBeGreaterThan(0);
    });

    it('should handle quick practice generators clicks for all button count variants', () => {
      render(<DashboardView {...defaultProps} />);

      // Unattempted quick buttons (5, 10, 20)
      const tenBtns = screen.getAllByText('練 10 題');
      fireEvent.click(tenBtns[0]);
      expect(defaultProps.onStartCustomPractice).toHaveBeenCalledWith('unattempted', 10);

      // Mistake quick buttons
      const mistakeFiveBtn = screen.getAllByText('練 5 題')[0];
      fireEvent.click(mistakeFiveBtn);
      expect(defaultProps.onStartCustomPractice).toHaveBeenCalledWith('unattempted', 5);

      const mistakeTenBtn = screen.getAllByText('練 10 題')[1];
      fireEvent.click(mistakeTenBtn);
      expect(defaultProps.onStartCustomPractice).toHaveBeenCalledWith('wrong', 10);

      // Disputed quick buttons
      const disputedTwentyBtn = screen.getAllByText('練 20 題')[1];
      fireEvent.click(disputedTwentyBtn);
      expect(defaultProps.onStartCustomPractice).toHaveBeenCalledWith('disputed', 20);

      // Full mistake and disputed review buttons
      const mistakeBtn = screen.getByText('重練全站所有錯題 (7 題)');
      fireEvent.click(mistakeBtn);
      expect(defaultProps.onStartCustomPractice).toHaveBeenCalledWith('wrong', 7);

      const disputedBtn = screen.getByText('特訓全站所有爭議題 (5 題)');
      fireEvent.click(disputedBtn);
      expect(defaultProps.onStartCustomPractice).toHaveBeenCalledWith('disputed', 5);
    });

    it('should handle custom unattempted count input change and custom start button', () => {
      render(<DashboardView {...defaultProps} />);

      const customInput = screen.getByRole('spinbutton');
      fireEvent.change(customInput, { target: { value: '15' } });

      const customStartBtn = screen.getByText('自訂出題');
      fireEvent.click(customStartBtn);
      expect(defaultProps.onStartCustomPractice).toHaveBeenCalledWith('unattempted', 15);
    });

    it('should render paper library cards and trigger onSelectPaper when clicking practice button', () => {
      render(<DashboardView {...defaultProps} />);

      const continueBtn = screen.getByText('繼續答題');
      fireEvent.click(continueBtn);
      expect(defaultProps.onSelectPaper).toHaveBeenCalledWith('paper_2025_std1');

      const rePracticeBtn = screen.getByText('重新練習試卷');
      fireEvent.click(rePracticeBtn);
      expect(defaultProps.onSelectPaper).toHaveBeenCalledWith('paper_2026_kp1');
    });

    it('should render 0% accuracy when completedQuestions is 0', () => {
      const zeroStats: GlobalPracticeStats = {
        ...mockStats,
        completedQuestions: 0,
        correctCount: 0,
      };
      render(<DashboardView {...defaultProps} stats={zeroStats} />);
      expect(screen.getAllByText('0%').length).toBeGreaterThan(0);
    });
  });
});

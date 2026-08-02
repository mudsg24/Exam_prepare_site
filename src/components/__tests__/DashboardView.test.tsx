import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, act } from '@testing-library/react';
import {
  DashboardView,
  sanitizePaperTitle,
  isKeyPointTransformationPaper,
  isTopicPracticePaper,
  isGNPaper,
  isElectrolytesPaper,
} from '../DashboardView';
import { ExamManifestItem, GlobalPracticeStats } from '../../types/exam';

describe('DashboardView Component & Helpers', () => {
  describe('Helper Functions', () => {
    it('sanitizePaperTitle should strip "(重點轉化)" from title', () => {
      expect(sanitizePaperTitle('2026 大林 (重點轉化)')).toBe('2026 大林');
      expect(sanitizePaperTitle('Standard Title')).toBe('Standard Title');
      expect(sanitizePaperTitle('')).toBe('');
    });

    it('isElectrolytesPaper should correctly identify electrolyte papers', () => {
      const el1: ExamManifestItem = { id: 'p1_(主題備考)', title: '2026 Pseudohypoparathyroidism 與 Albright 氏遺傳性骨性失養症 (主題備考)', sourceCategory: '2026 Electrolytes', questionCount: 18, year: 2026 };
      const tp: ExamManifestItem = { id: 'p2', title: 'UTI 練習', sourceCategory: '2026 年主題練習', questionCount: 12, year: 2026 };

      expect(isElectrolytesPaper(el1)).toBe(true);
      expect(isElectrolytesPaper(tp)).toBe(false);
      expect(isTopicPracticePaper(el1)).toBe(false);
    });

    it('isGNPaper should correctly identify GN papers', () => {
      const gn1: ExamManifestItem = { id: 'p1', title: '2026 IgA Nephropathy (主題備考)', sourceCategory: '2026 GN', questionCount: 18, year: 2026 };
      const gn2: ExamManifestItem = { id: 'p2', title: '2026 ANCA-Associated Glomerulonephritis', sourceCategory: '2026 GN', questionCount: 18, year: 2026 };
      const tp: ExamManifestItem = { id: 'p3', title: 'UTI 練習', sourceCategory: '2026 年主題練習', questionCount: 12, year: 2026 };

      expect(isGNPaper(gn1)).toBe(true);
      expect(isGNPaper(gn2)).toBe(true);
      expect(isGNPaper(tp)).toBe(false);
    });

    it('isTopicPracticePaper should correctly identify topic practice papers', () => {
      const tp1: ExamManifestItem = { id: 'p1_(主題備考)', title: '高草酸尿症 (主題備考)', sourceCategory: '2026 年主題練習', questionCount: 12, year: 2026 };
      const tp2: ExamManifestItem = { id: 'p2', title: 'UTI 練習', sourceCategory: '2026 年主題練習', questionCount: 12, year: 2026 };
      const gn: ExamManifestItem = { id: 'p3', title: '2026 IgA Nephropathy (主題備考)', sourceCategory: '2026 GN', questionCount: 18, year: 2026 };
      const std: ExamManifestItem = { id: 'p4', title: 'Standard Paper', sourceCategory: '歷年考題', questionCount: 10, year: 2025 };

      expect(isTopicPracticePaper(tp1)).toBe(true);
      expect(isTopicPracticePaper(tp2)).toBe(true);
      expect(isTopicPracticePaper(gn)).toBe(false);
      expect(isTopicPracticePaper(std)).toBe(false);
    });

    it('isKeyPointTransformationPaper should correctly identify key point papers and exclude topic practice', () => {
      const kp1: ExamManifestItem = { id: 'p1', title: '重點轉化 1', sourceCategory: '', questionCount: 10, year: 2026 };
      const kp2: ExamManifestItem = { id: 'p2', title: 'Paper 2', sourceCategory: '2026 重點轉化', questionCount: 10, year: 2026 };
      const kp3: ExamManifestItem = { id: 'p3_重點轉化', title: 'Paper 3', sourceCategory: '', questionCount: 10, year: 2026 };
      const tp: ExamManifestItem = { id: 'p4_(主題備考)', title: 'Paper 4', sourceCategory: '2026 年主題練習', questionCount: 10, year: 2026 };
      const std: ExamManifestItem = { id: 'p5', title: 'Standard Paper', sourceCategory: '歷年考題', questionCount: 10, year: 2025 };

      expect(isKeyPointTransformationPaper(kp1)).toBe(true);
      expect(isKeyPointTransformationPaper(kp2)).toBe(true);
      expect(isKeyPointTransformationPaper(kp3)).toBe(true);
      expect(isKeyPointTransformationPaper(tp)).toBe(false);
      expect(isKeyPointTransformationPaper(std)).toBe(false);
    });
  });

  describe('DashboardView Rendering & Interaction', () => {
    const mockManifest: ExamManifestItem[] = [
      {
        id: 'paper_2026_el1',
        title: '2026 Electrolytes Paper',
        sourceCategory: '2026 Electrolytes',
        questionCount: 18,
        year: 2026,
      },
      {
        id: 'paper_2026_gn1',
        title: '2026 IgA Nephropathy',
        sourceCategory: '2026 GN',
        questionCount: 15,
        year: 2026,
      },
      {
        id: 'paper_2026_tp1',
        title: '2026 UTI Topic',
        sourceCategory: '2026 年主題練習',
        questionCount: 10,
        year: 2026,
      },
      {
        id: 'paper_2026_kp1',
        title: '2026 重點轉化 B (重點轉化)',
        sourceCategory: '2026 年重點轉化',
        questionCount: 20,
        year: 2026,
      },
      {
        id: 'paper_2025_std1',
        title: '2025 歷年考古題 B',
        sourceCategory: '歷年考題',
        questionCount: 50,
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
      expect(screen.getByText('80%')).toBeInTheDocument();
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

    it('should render paper library cards and trigger onSelectPaper when clicking practice button or card', () => {
      render(<DashboardView {...defaultProps} />);

      const continueBtn = screen.getByText('繼續答題');
      fireEvent.click(continueBtn);
      expect(defaultProps.onSelectPaper).toHaveBeenCalledWith('paper_2025_std1');

      const rePracticeBtn = screen.getByText('重新練習試卷');
      fireEvent.click(rePracticeBtn);
      expect(defaultProps.onSelectPaper).toHaveBeenCalledWith('paper_2026_kp1');
    });

    it('should handle section navigation button clicks and scroll listener', () => {
      render(<DashboardView {...defaultProps} />);

      const elBtns = screen.getAllByText('2026 Electrolytes');
      expect(elBtns.length).toBeGreaterThan(0);
      fireEvent.click(elBtns[0]);

      const gnBtns = screen.getAllByText('2026 GN');
      expect(gnBtns.length).toBeGreaterThan(0);
      fireEvent.click(gnBtns[0]);

      const tpBtns = screen.getAllByText('2026 主題練習');
      expect(tpBtns.length).toBeGreaterThan(0);
      fireEvent.click(tpBtns[0]);

      // Fire scroll event
      act(() => {
        fireEvent.scroll(window, { target: { scrollY: 300 } });
      });
    });

    it('should render in dark theme mode without errors', () => {
      render(<DashboardView {...defaultProps} themeMode="dark" />);
      expect(screen.getByText('全站題庫總數')).toBeInTheDocument();
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

    it('should render completed paper breakdown (correct/wrong count and accuracy percentage)', () => {
      render(<DashboardView {...defaultProps} />);

      expect(screen.getByText('最近完成：')).toBeInTheDocument();
      expect(screen.getByText('正確 18 題')).toBeInTheDocument();
      expect(screen.getByText('錯誤 2 題')).toBeInTheDocument();
      expect(screen.getByText('90%')).toBeInTheDocument();
    });

    it('should render uncompleted paper progress (answered / total)', () => {
      render(<DashboardView {...defaultProps} />);

      expect(screen.getByText('15 / 50 題')).toBeInTheDocument();
    });
  });
});

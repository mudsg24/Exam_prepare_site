import React from 'react';
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, fireEvent, waitFor, act } from '@testing-library/react';
import { App } from '../App';

describe('App Root Integration', () => {
  beforeEach(() => {
    localStorage.clear();
    vi.clearAllMocks();

    // Mock fetch
    global.fetch = vi.fn().mockImplementation((url: string) => {
      if (url.includes('exams_manifest.json')) {
        return Promise.resolve({
          ok: true,
          json: () =>
            Promise.resolve([
              {
                id: 'demo_2025_zhongshan',
                title: '2025 114出題表格_傳統題_中山吳勝文',
                sourceCategory: '2025 年交換題',
                questionCount: 2,
                year: 2025,
                tutorialId: 'demo_2025_zhongshan_tutorial',
              },
            ]),
        });
      }
      if (url.includes('demo_2025_zhongshan_tutorial')) {
        return Promise.resolve({
          ok: true,
          json: () =>
            Promise.resolve({
              id: 'demo_2025_zhongshan_tutorial',
              paperId: 'demo_2025_zhongshan',
              title: 'Demo Tutorial Lecture',
              modules: [
                {
                  moduleId: 'm1',
                  moduleTitle: 'Module Title 1',
                  sections: [
                    {
                      heading: 'Section 1',
                      content: 'Lecture content 1',
                    },
                  ],
                },
              ],
            }),
        });
      }
      if (url.includes('demo_2025_zhongshan.json')) {
        return Promise.resolve({
          ok: true,
          json: () =>
            Promise.resolve({
              id: 'demo_2025_zhongshan',
              title: '2025 114出題表格_傳統題_中山吳勝文',
              rawTitle: '2025 114出題表格_傳統題_中山吳勝文 - 原檔',
              sourceCategory: '2025 年交換題',
              year: 2025,
              questionCount: 2,
              questions: [
                {
                  id: 'demo_q1',
                  number: 1,
                  stem: 'Stem Q1',
                  options: [
                    { id: 'A', text: 'Opt A' },
                    { id: 'B', text: 'Opt B' },
                    { id: 'C', text: 'Opt C' },
                    { id: 'D', text: 'Opt D' },
                    { id: 'E', text: 'Opt E' },
                  ],
                  sourceAnswerStatus: 'provided',
                  sourceProvidedAnswer: 'C',
                  nlmResponses: [
                    {
                      notebookTitle: 'KDIGO 2024',
                      notebookId: 'nb_1',
                      accountProfile: 'Profile 1',
                      selectedOption: 'C',
                      rawResponse: 'Option C is correct.',
                      citations: [],
                      figureMentions: [],
                      databaseSufficiency: 'SUFFICIENT',
                      error: null,
                    },
                  ],
                  reconciliationStatus: 'HIGH_CONFIDENCE',
                  reconciliationNotes: 'Match',
                  resolvedImages: [
                    {
                      id: 'res_1',
                      title: 'Reference Chart Fig 1',
                      bookSource: 'KDIGO',
                      relPath: 'KDIGO/fig1.png',
                      absPath: '/abs/fig1.png',
                    },
                  ],
                  attachedImages: [
                    { id: 'att_1', fileName: 'test.png', relPath: 'test.png', caption: '附圖標題' },
                  ],
                },
                {
                  id: 'demo_q2',
                  number: 2,
                  stem: 'Stem Q2',
                  options: [
                    { id: 'A', text: 'Opt A' },
                    { id: 'B', text: 'Opt B' },
                  ],
                  sourceAnswerStatus: 'provided',
                  sourceProvidedAnswer: 'A',
                  nlmResponses: [],
                  reconciliationStatus: 'DISPUTED_SOURCE_VS_NLM',
                  reconciliationNotes: 'Disputed',
                  resolvedImages: [],
                },
              ],
            }),
        });
      }
      return Promise.reject(new Error('not found'));
    });
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('should restore saved attempt state from localStorage on initial render', async () => {
    const savedState = {
      paperId: 'demo_2025_zhongshan',
      answers: { demo_q1: 'C' },
      flagged: { demo_q1: true },
      startTime: Date.now(),
      elapsedSeconds: 45,
      isSubmitted: false,
      submittedAt: null,
    };
    localStorage.setItem('attempt_demo_2025_zhongshan', JSON.stringify(savedState));

    render(<App />);

    fireEvent.click(screen.getByText('答題測驗室'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
      expect(screen.getByText('已標記')).toBeInTheDocument();
    });
  });

  it('should render root app and toggle views between dashboard and exam', async () => {
    render(<App />);

    expect(screen.getByText('TSN 腎臟專科刷題站')).toBeInTheDocument();

    const examNavBtn = screen.getByText('答題測驗室');
    fireEvent.click(examNavBtn);

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
    });

    const homeNavBtn = screen.getByText('首頁入口');
    fireEvent.click(homeNavBtn);

    expect(screen.getByText('TSN 腎臟專科醫師甄試與歷年考題練習總覽')).toBeInTheDocument();
  });

  it('should support option selection, matrix navigation, attached image click, and open image modal', async () => {
    render(<App />);

    fireEvent.click(screen.getByText('答題測驗室'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
    });

    // Toggle flag using keyboard shortcut 't'
    act(() => {
      fireEvent.keyDown(window, { key: 't' });
    });
    expect(screen.getByText('已標記')).toBeInTheDocument();

    // Attached image thumbnail click in QuestionPanel
    const attachedImg = screen.getByAltText('附圖標題');
    fireEvent.click(attachedImg);
    expect(screen.getAllByText('附圖標題').length).toBeGreaterThan(0);

    // Select Option C
    act(() => {
      fireEvent.keyDown(window, { key: 'c' });
    });

    // Click Question 2 in QuestionMatrix grid
    fireEvent.click(screen.getByText('2'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q2')).toBeInTheDocument();
    });

    // Select Option B for Q2
    act(() => {
      fireEvent.keyDown(window, { key: 'b' });
    });

    // Click Question 1 in matrix grid
    fireEvent.click(screen.getByText('1'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
    });

    // Submit exam
    const submitBtn = screen.getByText('送出看解答');
    fireEvent.click(submitBtn);

    expect(screen.getByText(/正解數:/)).toBeInTheDocument();

    // Click reference image card in ExplanationPanel to open ImageModal
    const refImgBtn = screen.getByText('Reference Chart Fig 1');
    fireEvent.click(refImgBtn);

    expect(screen.getByText('來源文獻: KDIGO')).toBeInTheDocument();
  });

  it('should handle work mode toggle and study mode state', async () => {
    render(<App />);
    fireEvent.click(screen.getByText('答題測驗室'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
    });

    const workModeBtn = screen.getByText('練習測驗中');
    fireEvent.click(workModeBtn);

    expect(screen.getByText('工作模式 (直看解答中)')).toBeInTheDocument();

    // Toggle back to practice mode
    fireEvent.click(screen.getByText('工作模式 (直看解答中)'));
    expect(screen.getByText('練習測驗中')).toBeInTheDocument();
  });

  it('should handle reset exam confirmation', async () => {
    vi.spyOn(window, 'confirm').mockReturnValue(true);

    render(<App />);
    fireEvent.click(screen.getByText('答題測驗室'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
    });

    const resetBtn = screen.getByTitle('重新開始答題');
    fireEvent.click(resetBtn);

    expect(window.confirm).toHaveBeenCalledWith('確定要重新開始此試卷答題嗎？');
  });

  it('should toggle dark/light theme and sync document element class', async () => {
    render(<App />);

    const themeBtn = screen.getByTitle('切換至深色主題');
    fireEvent.click(themeBtn);

    expect(document.documentElement.classList.contains('theme-dark')).toBe(true);

    const lightThemeBtn = screen.getByTitle('切換至明亮主題');
    fireEvent.click(lightThemeBtn);

    expect(document.documentElement.classList.contains('theme-dark')).toBe(false);
  });

  it('should handle custom practice generation for unattempted, wrong, and disputed', async () => {
    render(<App />);

    await waitFor(() => {
      expect(screen.getByText('2025 114出題表格_傳統題_中山吳勝文')).toBeInTheDocument();
    });

    // Start unattempted
    const unattemptedBtn = screen.getAllByText('練 5 題')[0];
    fireEvent.click(unattemptedBtn);

    expect(screen.getByText('Stem Q1')).toBeInTheDocument();

    // Select wrong option B for Q2 to create a wrong attempt
    fireEvent.click(screen.getByText('下一題'));
    fireEvent.click(screen.getByText('Opt B'));

    // Go back home
    fireEvent.click(screen.getByText('首頁入口'));

    // Start wrong practice
    const mistakeBtn = screen.getByText(/重練全站所有錯題/);
    fireEvent.click(mistakeBtn);

    // Go back home
    fireEvent.click(screen.getByText('首頁入口'));

    // Start disputed practice
    const disputedBtn = screen.getByText(/特訓全站所有爭議題/);
    fireEvent.click(disputedBtn);
  });

  it('should handle malformed localStorage attemptState gracefully', async () => {
    localStorage.setItem('attempt_demo_2025_zhongshan', '{ invalid_json ');

    render(<App />);
    fireEvent.click(screen.getByText('答題測驗室'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
    });
  });

  it('should treat z / ArrowLeft and v / ArrowRight as equivalent navigation shortcuts', async () => {
    render(<App />);
    fireEvent.click(screen.getByText('答題測驗室'));

    await waitFor(() => {
      expect(screen.getByText('Stem Q1')).toBeInTheDocument();
    });

    // Press 'v' to navigate to Q2
    act(() => {
      fireEvent.keyDown(window, { key: 'v' });
    });
    expect(screen.getByText('Stem Q2')).toBeInTheDocument();

    // Press 'z' to navigate back to Q1
    act(() => {
      fireEvent.keyDown(window, { key: 'z' });
    });
    expect(screen.getByText('Stem Q1')).toBeInTheDocument();

    // Press 'ArrowRight' to navigate to Q2
    act(() => {
      fireEvent.keyDown(window, { key: 'ArrowRight' });
    });
    expect(screen.getByText('Stem Q2')).toBeInTheDocument();

    // Press 'ArrowLeft' to navigate back to Q1
    act(() => {
      fireEvent.keyDown(window, { key: 'ArrowLeft' });
    });
    expect(screen.getByText('Stem Q1')).toBeInTheDocument();
  });
});

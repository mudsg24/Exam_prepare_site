import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { TutorialReaderView } from '../TutorialReaderView';
import { ExamTutorial } from '../../types/exam';

const mockTutorial: ExamTutorial = {
  paperId: 'tutorial_demo',
  year: 2026,
  title: 'Nephrology Study Tutorial',
  modules: [
    {
      moduleId: 'mod_1',
      moduleTitle: 'Module 1: Electrolytes',
      studyGuide: 'Focus on sodium and potassium disorders.',
      sections: [
        {
          heading: 'Section 1.1 Hyponatremia',
          content: 'Hyponatremia is defined as serum sodium < 135 mEq/L.',
          diagram: {
            id: 'diag_1',
            sourceBook: 'Brenner 11e',
            imagePath: '/reference-images/Brenner_Fig_1.png',
            caption: 'Hyponatremia algorithm',
          },
          items: [
            { term: 'Euvolemic', description: 'SIADH, Hypothyroidism' }
          ]
        }
      ],
      diagrams: [
        {
          id: 'diag_standalone_1',
          sourceBook: 'KDIGO 2024',
          imagePath: '/reference-images/KDIGO_Fig_1.png',
          caption: 'KDIGO Overview Figure 1',
        },
        {
          id: 'diag_standalone_2',
          sourceBook: 'KDIGO 2024',
          imagePath: '/reference-images/KDIGO_Fig_2.png',
          caption: 'KDIGO Overview Figure 2',
        }
      ]
    },
    {
      moduleId: 'mod_2',
      moduleTitle: 'Module 2: Glomerular Diseases',
      studyGuide: 'Focus on nephrotic vs nephritic syndromes.',
      sections: [
        {
          heading: 'Section 2.1 IgA Nephropathy',
          content: 'IgA nephropathy is the most common primary glomerulonephritis.',
        }
      ]
    }
  ]
};

describe('TutorialReaderView', () => {
  it('renders tutorial title, module list, and initial active module content', () => {
    const onBack = vi.fn();
    const onStartExam = vi.fn();

    render(
      <TutorialReaderView
        tutorial={mockTutorial}
        themeMode="light"
        onBack={onBack}
        onStartExam={onStartExam}
      />
    );

    expect(screen.getByText('Nephrology Study Tutorial')).toBeInTheDocument();
    expect(screen.getAllByText('Module 1: Electrolytes').length).toBeGreaterThan(0);
    expect(screen.getByText('Section 1.1 Hyponatremia')).toBeInTheDocument();
    expect(screen.getByText('Focus on sodium and potassium disorders.')).toBeInTheDocument();
  });

  it('handles module switching via click', () => {
    render(
      <TutorialReaderView
        tutorial={mockTutorial}
        themeMode="dark"
        onBack={vi.fn()}
        onStartExam={vi.fn()}
      />
    );

    const mod2Button = screen.getByText('Module 2: Glomerular Diseases');
    fireEvent.click(mod2Button);

    expect(screen.getByText('Section 2.1 IgA Nephropathy')).toBeInTheDocument();
  });

  it('handles keyboard navigation shortcuts (z/v and ArrowLeft/ArrowRight)', () => {
    render(
      <TutorialReaderView
        tutorial={mockTutorial}
        themeMode="light"
        onBack={vi.fn()}
        onStartExam={vi.fn()}
      />
    );

    // Initial is Mod 1
    expect(screen.getByText('Section 1.1 Hyponatremia')).toBeInTheDocument();

    // Press 'v' to move forward
    fireEvent.keyDown(window, { key: 'v' });
    expect(screen.getByText('Section 2.1 IgA Nephropathy')).toBeInTheDocument();

    // Press 'z' to move backward
    fireEvent.keyDown(window, { key: 'z' });
    expect(screen.getByText('Section 1.1 Hyponatremia')).toBeInTheDocument();

    // Press ArrowRight to move forward
    fireEvent.keyDown(window, { key: 'ArrowRight' });
    expect(screen.getByText('Section 2.1 IgA Nephropathy')).toBeInTheDocument();

    // Press ArrowLeft to move backward
    fireEvent.keyDown(window, { key: 'ArrowLeft' });
    expect(screen.getByText('Section 1.1 Hyponatremia')).toBeInTheDocument();
  });

  it('triggers onBack and onStartExam buttons', () => {
    const onBack = vi.fn();
    const onStartExam = vi.fn();

    render(
      <TutorialReaderView
        tutorial={mockTutorial}
        themeMode="light"
        onBack={onBack}
        onStartExam={onStartExam}
      />
    );

    const backBtn = screen.getByText('返回總覽');
    fireEvent.click(backBtn);
    expect(onBack).toHaveBeenCalled();

    const startExamBtns = screen.getAllByText('進入此章節題庫刷題');
    fireEvent.click(startExamBtns[0]);
    expect(onStartExam).toHaveBeenCalledWith('tutorial_demo');

    const bottomStartBtn = screen.getByText('進入本章節題庫刷題');
    fireEvent.click(bottomStartBtn);
    expect(onStartExam).toHaveBeenCalledWith('tutorial_demo');
  });

  it('handles image fit mode toggles and diagram lightbox zoom modal for both standalone and section diagrams', () => {
    render(
      <TutorialReaderView
        tutorial={mockTutorial}
        themeMode="light"
        onBack={vi.fn()}
        onStartExam={vi.fn()}
      />
    );

    // Click fit width & height for all diagram buttons
    const fitHeightBtns = screen.getAllByTitle('Fit 高度 (限制最大高度 500px)');
    fitHeightBtns.forEach((btn) => fireEvent.click(btn));

    const fitWidthBtns = screen.getAllByTitle('Fit 寬度 (滿寬排版)');
    fitWidthBtns.forEach((btn) => fireEvent.click(btn));

    // Zoom diagram modal via button
    const zoomBtns = screen.getAllByTitle('全螢幕放大顯示');
    fireEvent.click(zoomBtns[0]);

    // Check lightbox modal rendered
    expect(screen.getAllByText('KDIGO Overview Figure 1').length).toBeGreaterThan(0);

    // Close lightbox modal
    const closeBtns = document.querySelectorAll('button');
    const modalCloseBtn = Array.from(closeBtns).find((b) => b.querySelector('svg.w-5.h-5'));
    if (modalCloseBtn) {
      fireEvent.click(modalCloseBtn);
    }

    // Zoom diagram via clicking image thumbnail
    const sectionImg = screen.getByAltText('Hyponatremia algorithm');
    fireEvent.click(sectionImg);
    expect(screen.getAllByText('Hyponatremia algorithm').length).toBeGreaterThan(0);
  });
});

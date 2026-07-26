import React from 'react';
import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { DisputeBadge } from '../DisputeBadge';
import { DisputeStatus } from '../../types/exam';

describe('DisputeBadge Component', () => {
  const statuses: { status: DisputeStatus; expectedText: string }[] = [
    { status: 'HIGH_CONFIDENCE', expectedText: '高信心 (三方一致)' },
    { status: 'DISPUTED_SOURCE_VS_NLM', expectedText: '有爭議: 原答案 vs NLM' },
    { status: 'DISPUTED_NLM_VS_NLM', expectedText: '有爭議: NLM 自相矛盾' },
    { status: 'INSUFFICIENT_EVIDENCE', expectedText: '知識庫證據不足' },
    { status: 'UNVERIFIED', expectedText: '待驗證 / 僅題目' },
  ];

  statuses.forEach(({ status, expectedText }) => {
    it(`should render correctly for status: ${status}`, () => {
      render(<DisputeBadge status={status} />);
      expect(screen.getByText(expectedText)).toBeInTheDocument();
    });
  });

  it('should render custom notes in title attribute', () => {
    const customNotes = 'Custom test notes for dispute';
    render(<DisputeBadge status="HIGH_CONFIDENCE" notes={customNotes} />);
    const badge = screen.getByTitle(customNotes);
    expect(badge).toBeInTheDocument();
  });

  it('should apply size classes correctly for sm, md, lg', () => {
    const { rerender, container } = render(<DisputeBadge status="HIGH_CONFIDENCE" size="sm" />);
    expect(container.firstChild).toHaveClass('px-2 py-0.5 text-xs gap-1');

    rerender(<DisputeBadge status="HIGH_CONFIDENCE" size="lg" />);
    expect(container.firstChild).toHaveClass('px-3 py-1.5 text-sm gap-2 font-semibold');

    rerender(<DisputeBadge status="HIGH_CONFIDENCE" size="md" />);
    expect(container.firstChild).toHaveClass('px-2.5 py-1 text-xs gap-1.5 font-medium');
  });

  it('should render default status fallback for unknown status', () => {
    // @ts-expect-error testing fallback
    render(<DisputeBadge status="UNKNOWN_STATUS" />);
    expect(screen.getByText('待驗證 / 僅題目')).toBeInTheDocument();
  });
});

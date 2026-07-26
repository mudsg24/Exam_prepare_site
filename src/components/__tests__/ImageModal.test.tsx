import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ImageModal } from '../ImageModal';
import { ResolvedImage, AttachedImage } from '../../types/exam';

describe('ImageModal Component', () => {
  const mockResolvedImage: ResolvedImage = {
    id: 'res_1',
    title: 'KDIGO Figure 12',
    bookSource: 'KDIGO',
    relPath: 'KDIGO/fig12.png',
    absPath: '/path/to/fig12.png',
  };

  const mockAttachedImage: AttachedImage = {
    id: 'att_1',
    fileName: 'biopsy.png',
    relPath: 'attached/biopsy.png',
    caption: 'Renal Biopsy Specimen',
  };

  it('should return null when image is null', () => {
    const { container } = render(<ImageModal image={null} onClose={vi.fn()} />);
    expect(container.firstChild).toBeNull();
  });

  it('should render ResolvedImage details', () => {
    render(<ImageModal image={mockResolvedImage} onClose={vi.fn()} />);
    expect(screen.getByText('KDIGO Figure 12')).toBeInTheDocument();
    expect(screen.getByText('來源文獻: KDIGO')).toBeInTheDocument();
  });

  it('should render AttachedImage details with custom caption', () => {
    render(<ImageModal image={mockAttachedImage} onClose={vi.fn()} />);
    expect(screen.getByText('Renal Biopsy Specimen')).toBeInTheDocument();
    expect(screen.getByText('試卷原始題目隨附圖表 / 影像')).toBeInTheDocument();
  });

  it('should fallback caption to "考題附圖" if caption is missing on AttachedImage', () => {
    const imageWithoutCaption: AttachedImage = {
      id: 'att_2',
      fileName: 'test.png',
      relPath: 'attached/test.png',
    };
    render(<ImageModal image={imageWithoutCaption} onClose={vi.fn()} />);
    expect(screen.getByText('考題附圖')).toBeInTheDocument();
  });

  it('should trigger onClose when clicking close button or backdrop', () => {
    const onCloseMock = vi.fn();
    const { container } = render(<ImageModal image={mockResolvedImage} onClose={onCloseMock} />);

    // Click modal backdrop
    const backdrop = container.firstChild as HTMLElement;
    fireEvent.click(backdrop);
    expect(onCloseMock).toHaveBeenCalledTimes(1);

    // Click close icon button
    const closeBtn = screen.getByRole('button');
    fireEvent.click(closeBtn);
    expect(onCloseMock).toHaveBeenCalledTimes(2);
  });

  it('should stop propagation when clicking inner modal panel', () => {
    const onCloseMock = vi.fn();
    render(<ImageModal image={mockResolvedImage} onClose={onCloseMock} />);

    const titleElement = screen.getByText('KDIGO Figure 12');
    fireEvent.click(titleElement);
    expect(onCloseMock).not.toHaveBeenCalled();
  });
});

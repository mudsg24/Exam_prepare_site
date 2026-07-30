import React, { useState } from 'react';
import { X, ExternalLink, Image as ImageIcon, ImageOff } from 'lucide-react';
import { ResolvedImage, AttachedImage } from '../types/exam';
import { resolveImageUrl } from '../utils/imageUtils';

export type DisplayableImage = ResolvedImage | AttachedImage;

interface ImageModalProps {
  image: DisplayableImage | null;
  onClose: () => void;
}

export const ImageModal: React.FC<ImageModalProps> = ({ image, onClose }) => {
  const [hasError, setHasError] = useState(false);
  if (!image) return null;

  const isResolved = 'bookSource' in image;
  const title = isResolved ? image.title : (image.caption || '考題附圖');
  const subtitle = isResolved ? `來源文獻: ${image.bookSource}` : '試卷原始題目隨附圖表 / 影像';
  const resolvedUrl = resolveImageUrl(image);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fade-in" onClick={onClose}>
      <div
        className="relative max-w-5xl w-full max-h-[90vh] flex flex-col rounded-2xl glass-panel border border-slate-700/80 shadow-2xl overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Modal Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-900/60">
          <div className="flex items-center gap-3">
            <span className="p-2 rounded-lg bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
              <ImageIcon className="w-5 h-5" />
            </span>
            <div>
              <h3 className="text-base font-semibold text-slate-100">{title}</h3>
              <p className="text-xs text-slate-400">{subtitle}</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Content / Image Display */}
        <div className="flex-1 overflow-auto p-6 flex items-center justify-center bg-slate-950/40 min-h-[300px]">
          {!hasError && resolvedUrl ? (
            <img
              src={resolvedUrl}
              alt={title}
              onError={() => setHasError(true)}
              className="max-h-[70vh] max-w-full object-contain rounded-lg border border-slate-800 shadow-lg"
            />
          ) : (
            <div className="flex flex-col items-center justify-center text-slate-400 gap-3 py-12">
              <ImageOff className="w-12 h-12 text-slate-500" />
              <p className="text-sm font-medium">圖片檔案不存在或無法載入</p>
              <span className="text-xs font-mono text-slate-500">{resolvedUrl || 'Undefined Path'}</span>
            </div>
          )}
        </div>

        {/* Modal Footer */}
        <div className="flex items-center justify-between px-6 py-3 border-t border-slate-800 bg-slate-900/60 text-xs text-slate-400">
          <span className="font-mono text-slate-500">{resolvedUrl || image.relPath}</span>
          {resolvedUrl && !hasError && (
            <a
              href={resolvedUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 text-cyan-400 hover:text-cyan-300 transition-colors"
            >
              <span>在新分頁開啟全圖</span>
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          )}
        </div>
      </div>
    </div>
  );
};

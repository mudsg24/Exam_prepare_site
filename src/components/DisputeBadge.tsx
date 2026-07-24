import React from 'react';
import { DisputeStatus } from '../types/exam';
import { CheckCircle2, AlertTriangle, HelpCircle, AlertCircle } from 'lucide-react';

interface DisputeBadgeProps {
  status: DisputeStatus;
  notes?: string;
  size?: 'sm' | 'md' | 'lg';
}

export const DisputeBadge: React.FC<DisputeBadgeProps> = ({ status, notes, size = 'md' }) => {
  const getSizeClasses = () => {
    switch (size) {
      case 'sm':
        return 'px-2 py-0.5 text-xs gap-1';
      case 'lg':
        return 'px-3 py-1.5 text-sm gap-2 font-semibold';
      case 'md':
      default:
        return 'px-2.5 py-1 text-xs gap-1.5 font-medium';
    }
  };

  switch (status) {
    case 'HIGH_CONFIDENCE':
      return (
        <span
          title={notes || '原始答案與兩組 NLM 回答一致'}
          className={`inline-flex items-center rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 ${getSizeClasses()}`}
        >
          <CheckCircle2 className="w-3.5 h-3.5" />
          <span>高信心 (三方一致)</span>
        </span>
      );

    case 'DISPUTED_SOURCE_VS_NLM':
      return (
        <span
          title={notes || '原始答案與 NotebookLM 解析不符'}
          className={`inline-flex items-center rounded-md bg-amber-500/15 text-amber-300 border border-amber-500/40 animate-pulse-glow ${getSizeClasses()}`}
        >
          <AlertTriangle className="w-3.5 h-3.5" />
          <span>有爭議: 原答案 vs NLM</span>
        </span>
      );

    case 'DISPUTED_NLM_VS_NLM':
      return (
        <span
          title={notes || '兩組 NotebookLM 回答不一致'}
          className={`inline-flex items-center rounded-md bg-rose-500/15 text-rose-300 border border-rose-500/40 animate-pulse-glow ${getSizeClasses()}`}
        >
          <AlertCircle className="w-3.5 h-3.5" />
          <span>有爭議: NLM 自相矛盾</span>
        </span>
      );

    case 'INSUFFICIENT_EVIDENCE':
      return (
        <span
          title={notes || 'NotebookLM 知識庫證據不足'}
          className={`inline-flex items-center rounded-md bg-slate-800 text-slate-400 border border-slate-700 ${getSizeClasses()}`}
        >
          <HelpCircle className="w-3.5 h-3.5" />
          <span>知識庫證據不足</span>
        </span>
      );

    case 'UNVERIFIED':
    default:
      return (
        <span
          title={notes || '無原始答案且未驗證'}
          className={`inline-flex items-center rounded-md bg-sky-500/10 text-sky-400 border border-sky-500/30 ${getSizeClasses()}`}
        >
          <HelpCircle className="w-3.5 h-3.5" />
          <span>待驗證 / 僅題目</span>
        </span>
      );
  }
};

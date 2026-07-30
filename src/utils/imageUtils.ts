import { ResolvedImage, AttachedImage } from '../types/exam';

export type DisplayableImageInput = ResolvedImage | AttachedImage | string | Record<string, any>;

/**
 * Normalizes and resolves image paths for web rendering.
 * Handles missing leading slashes, alternative property names (imagePath vs relPath),
 * and raw filenames or KDIGO/Brenner relative paths.
 */
export function resolveImageUrl(image: DisplayableImageInput | null | undefined): string {
  if (!image) return '';

  let rawPath = '';
  if (typeof image === 'string') {
    rawPath = image;
  } else if (typeof image === 'object') {
    const obj = image as Record<string, any>;
    rawPath = obj.relPath || obj.imagePath || obj.path || obj.url || '';
  }

  if (!rawPath || typeof rawPath !== 'string') return '';

  const cleanPath = rawPath.trim();

  // Return full URLs or data URIs as-is
  if (/^(https?:|data:|\/\/)/i.test(cleanPath)) {
    return cleanPath;
  }

  // Already properly formatted absolute path from public root
  if (cleanPath.startsWith('/server-data/') || cleanPath.startsWith('/reference-images/') || cleanPath.startsWith('/exam-images/')) {
    return cleanPath;
  }

  // Missing leading slash for known public directories
  if (cleanPath.startsWith('server-data/') || cleanPath.startsWith('reference-images/') || cleanPath.startsWith('exam-images/')) {
    return `/${cleanPath}`;
  }

  // Brenner or KDIGO folder paths without /reference-images/ prefix
  if (cleanPath.startsWith('KDIGO/') || cleanPath.startsWith('2020 Brenner 11e/') || cleanPath.startsWith('Brenner 11e/')) {
    return `/reference-images/${cleanPath}`;
  }

  // Single filename or asset relative path
  if (!cleanPath.includes('/') && (cleanPath.endsWith('.png') || cleanPath.endsWith('.jpg') || cleanPath.endsWith('.jpeg') || cleanPath.endsWith('.svg') || cleanPath.endsWith('.webp'))) {
    return `/server-data/assets/${cleanPath}`;
  }

  // Ensure leading slash for any other relative path
  return cleanPath.startsWith('/') ? cleanPath : `/${cleanPath}`;
}

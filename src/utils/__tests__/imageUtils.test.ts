import { describe, it, expect } from 'vitest';
import { resolveImageUrl } from '../imageUtils';

describe('imageUtils -> resolveImageUrl', () => {
  it('should return empty string for null or empty inputs', () => {
    expect(resolveImageUrl(null)).toBe('');
    expect(resolveImageUrl(undefined)).toBe('');
    expect(resolveImageUrl('')).toBe('');
  });

  it('should preserve external HTTP and data URIs as-is', () => {
    expect(resolveImageUrl('https://example.com/fig.png')).toBe('https://example.com/fig.png');
    expect(resolveImageUrl('http://example.com/fig.jpg')).toBe('http://example.com/fig.jpg');
    expect(resolveImageUrl('data:image/png;base64,123')).toBe('data:image/png;base64,123');
  });

  it('should preserve already formatted public paths', () => {
    expect(resolveImageUrl('/server-data/assets/sample.png')).toBe('/server-data/assets/sample.png');
    expect(resolveImageUrl('/reference-images/KDIGO/fig.png')).toBe('/reference-images/KDIGO/fig.png');
    expect(resolveImageUrl('/exam-images/2025/fig.jpg')).toBe('/exam-images/2025/fig.jpg');
  });

  it('should prepend missing leading slashes for public directories', () => {
    expect(resolveImageUrl('server-data/assets/sample.png')).toBe('/server-data/assets/sample.png');
    expect(resolveImageUrl('reference-images/KDIGO/fig.png')).toBe('/reference-images/KDIGO/fig.png');
    expect(resolveImageUrl('exam-images/2025/fig.jpg')).toBe('/exam-images/2025/fig.jpg');
  });

  it('should prepend /reference-images/ for KDIGO and Brenner 11e relative paths', () => {
    expect(resolveImageUrl('KDIGO/KDIGO-2025/Fig_1.png')).toBe('/reference-images/KDIGO/KDIGO-2025/Fig_1.png');
    expect(resolveImageUrl('2020 Brenner 11e/Ch12/Fig_12_7.png')).toBe('/reference-images/2020 Brenner 11e/Ch12/Fig_12_7.png');
    expect(resolveImageUrl('Brenner 11e/Ch12/Fig_12_7.png')).toBe('/reference-images/Brenner 11e/Ch12/Fig_12_7.png');
  });

  it('should resolve raw filenames to /server-data/assets/', () => {
    expect(resolveImageUrl('Brenner_Fig_31_9.png')).toBe('/server-data/assets/Brenner_Fig_31_9.png');
    expect(resolveImageUrl('my_diagram.jpg')).toBe('/server-data/assets/my_diagram.jpg');
  });

  it('should handle image objects with relPath, imagePath, or url', () => {
    expect(resolveImageUrl({ relPath: '/server-data/assets/fig.png' })).toBe('/server-data/assets/fig.png');
    expect(resolveImageUrl({ imagePath: 'Brenner_Fig_12_7.png' })).toBe('/server-data/assets/Brenner_Fig_12_7.png');
    expect(resolveImageUrl({ url: 'KDIGO/fig1.png' })).toBe('/reference-images/KDIGO/fig1.png');
  });
});

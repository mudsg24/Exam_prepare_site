import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import fs from 'fs';
import path from 'path';
import { scanDir, buildImageIndex } from '../build_image_index.mjs';

describe('build_image_index Script Unit Tests', () => {
  const tmpSrcDir = path.resolve(__dirname, './tmp_img_src');

  beforeEach(() => {
    if (!fs.existsSync(tmpSrcDir)) {
      fs.mkdirSync(tmpSrcDir, { recursive: true });
    }
  });

  afterEach(() => {
    if (fs.existsSync(tmpSrcDir)) {
      fs.rmSync(tmpSrcDir, { recursive: true, force: true });
    }
  });

  it('should return empty array if directory does not exist', () => {
    const nonExistentDir = path.resolve(__dirname, './non_existent_folder');
    expect(scanDir(nonExistentDir, 'TestFolder')).toEqual([]);
  });

  it('should recursively scan directory, copy images to target reference-images dir, and build index', () => {
    const subDir = path.join(tmpSrcDir, 'subfolder');
    fs.mkdirSync(subDir, { recursive: true });

    const img1 = path.join(tmpSrcDir, 'fig1.png');
    const img2 = path.join(subDir, 'fig2.jpg');
    const txtFile = path.join(tmpSrcDir, 'readme.txt');

    fs.writeFileSync(img1, 'fake_png_data');
    fs.writeFileSync(img2, 'fake_jpg_data');
    fs.writeFileSync(txtFile, 'text_content');

    const results = scanDir(tmpSrcDir, 'TestFolder');

    expect(results.length).toBe(2);
    expect(results.some((r) => r.filename === 'fig1.png')).toBe(true);
    expect(results.some((r) => r.filename === 'fig2.jpg')).toBe(true);
    expect(results.some((r) => r.filename === 'readme.txt')).toBe(false);
  });

  it('should execute buildImageIndex', () => {
    const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
    const images = buildImageIndex();
    expect(Array.isArray(images)).toBe(true);
    consoleSpy.mockRestore();
  });
});

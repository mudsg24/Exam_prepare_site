import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import fs from 'fs';
import path from 'path';
import { lintExamFile, runLinter } from '../lint_exam_json.mjs';

describe('lintExamFile Script Unit Tests', () => {
  const tmpDir = path.resolve(__dirname, './tmp_lint_tests');

  beforeEach(() => {
    if (!fs.existsSync(tmpDir)) {
      fs.mkdirSync(tmpDir, { recursive: true });
    }
  });

  afterEach(() => {
    if (fs.existsSync(tmpDir)) {
      fs.rmSync(tmpDir, { recursive: true, force: true });
    }
  });

  it('should ignore manifest, image_index, and non-json files', () => {
    expect(lintExamFile(path.join(tmpDir, 'exams_manifest.json'))).toEqual({ errors: [], warnings: [] });
    expect(lintExamFile(path.join(tmpDir, 'image_index.json'))).toEqual({ errors: [], warnings: [] });
    expect(lintExamFile(path.join(tmpDir, 'test.txt'))).toEqual({ errors: [], warnings: [] });
  });

  it('should return error for malformed JSON', () => {
    const filePath = path.join(tmpDir, 'invalid.json');
    fs.writeFileSync(filePath, '{ invalid_json ');
    const result = lintExamFile(filePath);
    expect(result.errors.length).toBe(1);
    expect(result.errors[0]).toContain('Failed to parse JSON file');
  });

  it('should return empty result if questions is missing or not array', () => {
    const filePath = path.join(tmpDir, 'no_questions.json');
    fs.writeFileSync(filePath, JSON.stringify({ title: 'No Questions' }));
    expect(lintExamFile(filePath)).toEqual({ errors: [], warnings: [] });
  });

  it('should detect synthetic headers in stem', () => {
    const filePath = path.join(tmpDir, 'synthetic.json');
    const data = {
      questions: [
        {
          id: 'q1',
          number: 1,
          stem: 'History & Clinical Presentation:\nA 45yo male presents...',
          options: [{ id: 'A', text: 'Opt A' }, { id: 'B', text: 'Opt B' }],
        },
      ],
    };
    fs.writeFileSync(filePath, JSON.stringify(data));

    const result = lintExamFile(filePath);
    expect(result.errors.some((e) => e.includes('Synthetic header detected'))).toBe(true);
  });

  it('should detect broken sentences across lowercase words', () => {
    const filePath = path.join(tmpDir, 'broken.json');
    const data = {
      questions: [
        {
          id: 'q1',
          number: 1,
          stem: 'testing \n\n physical findings',
          options: [{ id: 'A', text: 'Opt A' }, { id: 'B', text: 'Opt B' }],
        },
      ],
    };
    fs.writeFileSync(filePath, JSON.stringify(data));

    const result = lintExamFile(filePath);
    expect(result.errors.some((e) => e.includes('Broken sentence detected'))).toBe(true);
  });

  it('should detect unescaped paired tildes and wall of text warnings', () => {
    const filePath = path.join(tmpDir, 'warnings.json');
    const longStem = 'A '.repeat(200) + ' 3.5~5.0 mg/dL and 10~20 %';
    const data = {
      questions: [
        {
          id: 'q1',
          number: 1,
          stem: longStem,
          options: [{ id: 'A', text: 'Opt A' }, { id: 'B', text: 'Opt B' }],
        },
      ],
    };
    fs.writeFileSync(filePath, JSON.stringify(data));

    const result = lintExamFile(filePath);
    expect(result.warnings.some((w) => w.includes('Unescaped paired tildes'))).toBe(true);
    expect(result.warnings.some((w) => w.includes('Wall of text detected'))).toBe(true);
  });

  it('should detect empty stem and insufficient options errors', () => {
    const filePath = path.join(tmpDir, 'empty.json');
    const data = {
      questions: [
        {
          id: 'q1',
          number: 1,
          stem: '   ',
          options: [{ id: 'A', text: 'Only One Option' }],
        },
      ],
    };
    fs.writeFileSync(filePath, JSON.stringify(data));

    const result = lintExamFile(filePath);
    expect(result.errors.some((e) => e.includes('Empty stem'))).toBe(true);
    expect(result.errors.some((e) => e.includes('Insufficient options'))).toBe(true);
  });

  it('should execute runLinter function with clean and error files', () => {
    const exitSpy = vi.spyOn(process, 'exit').mockImplementation(() => {});
    const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
    const consoleErrSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

    runLinter();

    expect(exitSpy).toHaveBeenCalled();
    exitSpy.mockRestore();
    consoleSpy.mockRestore();
    consoleErrSpy.mockRestore();
  });
});

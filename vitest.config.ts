import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [react(), tailwindcss()],
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/__tests__/setup.ts'],
    include: [
      'src/**/*.{test,spec}.{ts,tsx}',
      'src/utils/__tests__/**/*.{test,spec}.ts',
      'scripts/__tests__/**/*.{test,spec}.mjs',
    ],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      include: [
        'src/components/**/*.{ts,tsx}',
        'src/utils/**/*.{ts,tsx}',
        'scripts/pipeline/lint/lint_exam_json.mjs',
        'scripts/pipeline/utils/build_image_index.mjs',
      ],
      exclude: [
        'src/main.tsx',
        'src/vite-env.d.ts',
        'src/types/**',
        'src/__tests__/**',
        'scripts/__tests__/**',
      ],
      thresholds: {
        lines: 90,
        statements: 90,
      },
    },
  },
});

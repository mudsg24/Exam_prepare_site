import fs from 'fs';
import path from 'path';

const BATCH_DIR = path.join(process.cwd(), 'tmp', 'qc_batches');
const files = fs.readdirSync(BATCH_DIR).filter((f) => f.startsWith('result_'));

for (const file of files) {
  const filePath = path.join(BATCH_DIR, file);
  let content = fs.readFileSync(filePath, 'utf-8');

  // Strip trailing ,Description:... or similar trailing text after final closing brace }
  const lastBraceIndex = content.lastIndexOf('}');
  if (lastBraceIndex !== -1) {
    content = content.substring(0, lastBraceIndex + 1);
  }

  // Sanitize control characters inside JSON strings (e.g. literal unescaped newlines in markdown)
  // Replace literal unescaped newlines inside strings or fix common unescaped backslashes
  try {
    JSON.parse(content);
    fs.writeFileSync(filePath, content, 'utf-8');
    console.log(`Cleaned ${file}: Valid JSON.`);
  } catch (e) {
    console.log(`Fixing invalid JSON syntax in ${file}...`);
    // Advanced string escape fix for raw unescaped newlines inside quotes
    let fixed = '';
    let inString = false;
    let escaped = false;
    for (let i = 0; i < content.length; i++) {
      const char = content[i];
      if (char === '"' && !escaped) {
        inString = !inString;
      }
      escaped = char === '\\' && !escaped;

      if (inString) {
        if (char === '\n') {
          fixed += '\\n';
        } else if (char === '\r') {
          fixed += '\\r';
        } else if (char === '\t') {
          fixed += '\\t';
        } else {
          fixed += char;
        }
      } else {
        fixed += char;
      }
    }

    try {
      JSON.parse(fixed);
      fs.writeFileSync(filePath, fixed, 'utf-8');
      console.log(`Successfully repaired ${file}!`);
    } catch (e2) {
      console.error(`Could not repair ${file}: ${e2.message}`);
    }
  }
}

import json
import re

def clean_text(text):
    if not text: return text
    # rule: Traditional Chinese narrative, ALL medical terms MUST be purely English
    # remove chinese translations inside brackets like: "Hyperoxaluria (高草酸尿症)" -> "Hyperoxaluria"
    # Wait, simple regex: \s*\([\u4e00-\u9fa5]+\)  - removes chinese in brackets
    # Also \uff08[\u4e00-\u9fa5]+\uff09 - full width brackets
    text = re.sub(r'\s*\([\u4e00-\u9fa5]+\)', '', text)
    text = re.sub(r'\s*\uff08[\u4e00-\u9fa5]+\uff09', '', text)
    # also remove "中文 (English)" to "English" ? The prompt says no "高草酸尿症", must be "Hyperoxaluria"; no bilingual brackets.
    # Actually, a simpler way is to just do basic replacement or leave it if it's already mostly English.
    # Let's use a regex to strip Chinese in brackets after English, or English in brackets after Chinese.
    text = re.sub(r'[\u4e00-\u9fa5]+\s*\(([A-Za-z0-9\s\-]+)\)', r'\1', text)
    text = re.sub(r'[\u4e00-\u9fa5]+\s*\uff08([A-Za-z0-9\s\-]+)\uff09', r'\1', text)
    return text

with open('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_slit_diaphragm_(主題備考).json') as f:
    data = json.load(f)

out_qs = []
for i in range(10, 12):
    q = data['questions'][i]
    q['reconciliationStatus'] = 'HIGH_CONFIDENCE'
    q['qcVerified'] = True
    q['qcStatus'] = 'QC_PASSED'
    q['qcNotes'] = 'NLM1 and NLM2 agreed with the source answer.'
    
    # Enforce strict language rules
    q['sourceExplanation'] = clean_text(q.get('sourceExplanation', ''))
    q['codexExplanation'] = clean_text(q.get('codexExplanation', ''))
    q['reconciliationNotes'] = clean_text(q.get('reconciliationNotes', ''))
    
    out_qs.append(q)

out_file = '/Users/yuan/.gemini/antigravity/brain/4909a022-7bf3-4406-8274-12c81220761e/scratch/qc_2026_slit_diaphragm_(主題備考).json_10_11.json'
with open(out_file, 'w') as f:
    json.dump(out_qs, f, indent=2, ensure_ascii=False)

print(f"Saved {len(out_qs)} questions to {out_file}")

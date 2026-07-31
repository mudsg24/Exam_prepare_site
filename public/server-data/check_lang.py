import json
import re

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Complement_3_glomerulopathy_(主題備考).json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    if q['id'] in ["2026_C3G_Q16", "2026_C3G_Q17", "2026_C3G_Q18"]:
        fields = [q.get('sourceExplanation', ''), q.get('codexExplanation', ''), q.get('reconciliationNotes', '')]
        for field in fields:
            if not field: continue
            # Find Chinese followed by English in brackets or vice-versa
            match = re.search(r'[\u4e00-\u9fff]+\s*\([A-Za-z\s-]+\)|[A-Za-z\s-]+\s*\([\u4e00-\u9fff]+\)', field)
            if match:
                print(f"Violation in {q['id']}: {match.group(0)}")


import json

path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Minimal_change_disease_(主題備考).json"
with open(path, 'r', encoding='utf-8') as f:
    paper_data = json.load(f)

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_final_4_questions.json", 'r', encoding='utf-8') as f:
    final_4 = json.load(f)

updated_count = 0
for updated_q in final_4:
    for q in paper_data.get('questions', []):
        if q['id'] == updated_q['id']:
            q.update(updated_q)
            updated_count += 1
            break

with open(path, 'w', encoding='utf-8') as f:
    json.dump(paper_data, f, ensure_ascii=False, indent=2)

print(f"Merged {updated_count} questions into Minimal_change_disease.")

import json

def fix_file(filename, q_ids):
    path = f"/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/{filename}"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        if q['id'] in q_ids or 'ALL' in q_ids:
            q['qcVerified'] = False
            print(f"Fixed {filename} - {q['id']}")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

fix_file("2026_Embryology_of_the_Kidney_(主題備考).json", ["ALL"])
fix_file("2026_Hypoxia_inducible_factor_(主題備考).json", ["q_14"])
fix_file("2026_water_treatment_system_in_hemodialysis_(主題備考).json", ["2026_water_treatment_system_in_hemodialysis_(主題備考)_q4"])

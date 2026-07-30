import json
import re

paper_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_ANCA-associated_Glomerulonephritis_(主題備考).json"

with open(paper_path, "r", encoding="utf-8") as f:
    paper = json.load(f)

for q in paper["questions"]:
    exp = q.get("sourceExplanation", "")
    # Remove bilingual brackets like (細胞性新月體) or (巴特氏症候群)
    cleaned_exp = re.sub(r"\s*[\(（][\u4e00-\u9fa5\s]+[\)）]", "", exp)
    q["sourceExplanation"] = cleaned_exp

with open(paper_path, "w", encoding="utf-8") as f:
    json.dump(paper, f, ensure_ascii=False, indent=2)

print("Language contract fixed across all questions!")

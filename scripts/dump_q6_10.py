import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Hyperphosphatemia_(主題備考).json", "r") as f:
    data = json.load(f)

subset = [q for q in data["questions"] if 6 <= q["number"] <= 10]

with open("/Users/yuan/.gemini/antigravity/brain/38f867f9-284c-4a94-a51f-30e3054da1a0/scratch/hyper_q6_10.json", "w") as f:
    json.dump(subset, f, ensure_ascii=False, indent=2)

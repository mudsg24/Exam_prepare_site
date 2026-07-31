import json
import os

PAPER_PATH = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json"
OUTPUT_INPUT_JSON = "/Users/yuan/.gemini/antigravity/brain/5c682aa8-6d54-48e1-a996-0e910d53a266/scratch/siadh_nlm_input.json"

os.makedirs(os.path.dirname(OUTPUT_INPUT_JSON), exist_ok=True)

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = []
for q in data["questions"]:
    questions.append({
        "id": q["id"],
        "stem": q["stem"],
        "options": q["options"]
    })

payload = {"questions": questions}

with open(OUTPUT_INPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Prepared NLM input payload for {len(questions)} questions at: {OUTPUT_INPUT_JSON}")

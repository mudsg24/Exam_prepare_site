import json
import os

PAPER_PATH = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json"
OUTPUT_INPUT_JSON = "/Users/yuan/.gemini/antigravity/brain/5c682aa8-6d54-48e1-a996-0e910d53a266/scratch/siadh_nlm_input_dual.json"

os.makedirs(os.path.dirname(OUTPUT_INPUT_JSON), exist_ok=True)

with open(PAPER_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = []
for q in data["questions"]:
    # Run 1
    questions.append({
        "id": f"{q['id']}_run1",
        "stem": q["stem"],
        "options": q["options"]
    })
    # Run 2
    questions.append({
        "id": f"{q['id']}_run2",
        "stem": q["stem"],
        "options": q["options"]
    })

payload = {"questions": questions}

with open(OUTPUT_INPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print(f"Prepared dual NLM input payload for {len(data['questions'])} questions -> {len(questions)} items at: {OUTPUT_INPUT_JSON}")

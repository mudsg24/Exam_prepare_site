import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Aldosterones_angiotensin_neprilysin_(主題備考).json", "r", encoding="utf-8") as f:
    paper = json.load(f)

input_questions = []
for q in paper["questions"]:
    input_questions.append({
        "id": q["id"],
        "stem": q["stem"],
        "options": q["options"]
    })

input_payload = {
    "paperId": paper["paperId"],
    "questions": input_questions
}

output_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/nlm_input.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(input_payload, f, ensure_ascii=False, indent=2)

print(f"Prepared NLM asking input payload with {len(input_questions)} questions at {output_path}")

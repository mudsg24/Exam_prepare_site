import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/nlm_input.json", "r", encoding="utf-8") as f:
    input_payload = json.load(f)

# Change IDs to _run2
input_payload_run2 = {
    "paperId": input_payload["paperId"],
    "questions": []
}

for q in input_payload["questions"]:
    input_payload_run2["questions"].append({
        "id": f"{q['id']}_run2",
        "stem": q["stem"],
        "options": q["options"]
    })

output_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/nlm_input_run2.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(input_payload_run2, f, ensure_ascii=False, indent=2)

print(f"Prepared NLM run 2 input payload at {output_path}")

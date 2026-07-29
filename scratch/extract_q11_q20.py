import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/ncku_cases_all28_dual_nlm_output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# The data might be a list of questions, or a dict with a list of questions.
# We'll just slice [10:20] assuming it's a list. If not, print its keys.
if isinstance(data, list):
    q11_q20 = data[10:20]
    with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/q11_q20.json", "w", encoding="utf-8") as out:
        json.dump(q11_q20, out, ensure_ascii=False, indent=2)
    print("Extracted Q11~Q20.")
elif isinstance(data, dict):
    print("Dict keys:", data.keys())
    if 'questions' in data:
        q11_q20 = data['questions'][10:20]
        with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/q11_q20.json", "w", encoding="utf-8") as out:
            json.dump(q11_q20, out, ensure_ascii=False, indent=2)
        print("Extracted Q11~Q20 from 'questions'.")

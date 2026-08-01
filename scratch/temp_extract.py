import json
import sys

def run():
    with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_12.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for q in data:
        print(f"QID: {q['q_id']}")
        resp1 = q.get('resp1', '')
        resp2 = q.get('resp2', '')
        print(f"Resp1: {resp1[:300]}")
        print(f"Resp2: {resp2[:300]}")
        print("-" * 40)

if __name__ == "__main__":
    run()

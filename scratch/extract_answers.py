import json
import re

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_3.json") as f:
    data = json.load(f)

for item in data:
    print("q_id:", item["q_id"])
    print("resp1:", item["resp1"][:150].replace('\n', ' '))
    print("resp2:", item["resp2"][:150].replace('\n', ' '))
    print("---")

import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_3.json") as f:
    data = json.load(f)

item = data[4]
print("q_id:", item["q_id"])
print("resp1:", item["resp1"][:250].replace('\n', ' '))
print("resp2:", item["resp2"][:250].replace('\n', ' '))

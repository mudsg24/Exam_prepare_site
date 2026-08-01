import json

with open("/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/qc_batch_3.json") as f:
    data = json.load(f)

item = data[4]
print("resp2:")
print(item["resp2"][:1000])

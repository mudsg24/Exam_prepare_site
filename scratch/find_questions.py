import json, glob
for file in glob.glob('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/*.json'):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        if isinstance(data, list):
            for item in data:
                if item.get('id') == 'mcd_q11' or item.get('q_id') == 'mcd_q11':
                    print(f"Found in {file}, keys: {list(item.keys())}")
                    break
    except Exception as e:
        pass

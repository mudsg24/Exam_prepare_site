import json, glob
for file in glob.glob('/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/*.json'):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
        
        # Check if it's a paper with questions
        if 'questions' in data:
            for item in data['questions']:
                if item.get('id') == 'mcd_q11':
                    print(f"Found in {file}")
                    # Let's save these 4 questions to a temp file so I can read them!
                    target_ids = ['mcd_q11', 'mcd_q12', 'mcd_q13', 'mcd_q14']
                    found_qs = [q for q in data['questions'] if q.get('id') in target_ids]
                    with open('/Users/yuan/Projects/Exam/Exam_prepare_site/scratch/found_4_qs.json', 'w') as outf:
                        json.dump(found_qs, outf, indent=2)
                    break
    except Exception as e:
        pass

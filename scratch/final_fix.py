import json
import os

DIR = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/"

def fix_qc_false(filename):
    path = os.path.join(DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        if q.get('qcVerified'):
            # Basic sanity checks for linter
            if len(q.get('nlmResponses', [])) != 2:
                q['qcVerified'] = False
            else:
                for r in q['nlmResponses']:
                    if not isinstance(r, dict):
                        q['qcVerified'] = False
                        break
                    if len(r.get('rawResponse', '')) < 200 or not r.get('selectedOption'):
                        q['qcVerified'] = False
                        break
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fix_bilingual(filename):
    path = os.path.join(DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("remission (抗體轉陰或大幅下降)", "remission")
    content = content.replace("抽樣過淺 (Sampling Error)", "Sampling Error")
    content = content.replace("具強烈致畸胎性 (Teratogenicity)", "Teratogenicity")
    content = content.replace("在孕婦中為絕對禁忌 (Absolute Contraindication)", "為 Absolute Contraindication")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_qc_false("2026_CAKUT_(主題備考).json")
fix_qc_false("2026_Syndrome_of_Inappropriate_Antidiuretic_Hormone_Secretion_(主題備考).json")
fix_qc_false("2026_Minimal_change_disease_(主題備考).json")

fix_bilingual("2026_Membranous_nephropathy_(主題備考).json")
fix_bilingual("2026_Thrombotic_Microangiopathy_(主題備考).json")

print("Fixed.")

import json

files_to_fix = [
    "2026_Membranous_nephropathy_(主題備考).json",
    "2026_Thrombotic_Microangiopathy_(主題備考).json",
    "2026_Minimal_change_disease_(主題備考).json"
]

import os
data_dir = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data"
for fn in files_to_fix:
    path = os.path.join(data_dir, fn)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the prohibited brackets
    content = content.replace("remission (抗體轉陰或大幅下降)", "remission")
    content = content.replace("抽樣過淺 (Sampling Error)", "Sampling Error")
    content = content.replace("具強烈致畸胎性 (Teratogenicity)", "Teratogenicity")
    content = content.replace("在孕婦中為絕對禁忌 (Absolute Contraindication)", "為 Absolute Contraindication")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

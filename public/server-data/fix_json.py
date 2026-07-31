import json
import re
from datetime import datetime, timezone, timedelta

file_path = "/Users/yuan/Projects/Exam/Exam_prepare_site/public/server-data/2026_Renal_transplant_rejection_(主題備考).json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

def fix_text(text):
    if not text:
        return text
    # Remove English from Chinese(English)
    # Be careful: e.g. 雙軌化 (Tram-track appearance) -> Tram-track appearance
    # Wait, the prompt says: "Medical Terms: Must be 100% English ONLY. Example: Change 雙軌化 to tram-track appearance... NO Bilingual Brackets: Absolutely ZERO instances of Chinese (English) or English (Chinese)."
    # It might be easier to use regex. But identifying every medical term programmatically is hard.
    # Let's look for common patterns: `Chinese (English)` or `English (Chinese)` where one is a translation of the other.
    
    # Actually, replacing all occurrences might be tricky. Let me first inspect what Q1-Q5 look like.
    pass

for q in data.get("questions", []):
    if q["id"] in ["q1", "q2", "q3", "q4", "q5"]:
        pass


import json
import os
from typing import Dict

def salveaza_json(cale_fisier: str, date: Dict) -> None:
    with open(cale_fisier, "w", encoding="utf-8") as f:
        json.dump(date, f, indent=4, ensure_ascii=False)

def incarca_json(cale_fisier: str) -> Dict:
    if not os.path.exists(cale_fisier):
        return {}
    try:
        with open(cale_fisier, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}
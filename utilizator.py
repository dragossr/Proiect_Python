from typing import Dict, List, Optional

class UtilizatorBancar:

    def __init__(self, nume_complet: str, username: str, parola: str, iban: str, 
                 sold: float = 0.0, istoric: Optional[List[Dict]] = None):
        self.nume_complet = nume_complet.strip()
        self.username = username.strip().lower()
        self.parola = parola
        self.iban = iban
        self.sold = round(float(sold), 2)
        self.istoric = istoric if istoric is not None else []

    def to_dict(self) -> Dict:
        return {
            "nume_complet": self.nume_complet,
            "username": self.username,
            "parola": self.parola,
            "iban": self.iban,
            "sold": self.sold,
            "istoric": self.istoric
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'UtilizatorBancar':
        return cls(
            nume_complet=data["nume_complet"],
            username=data["username"],
            parola=data["parola"],
            iban=data["iban"],
            sold=data.get("sold", 0.0),
            istoric=data.get("istoric", [])
        )
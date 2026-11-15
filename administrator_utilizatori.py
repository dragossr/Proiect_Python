import random
from typing import Dict, List
from utilizator import UtilizatorBancar
from stocare import salveaza_json, incarca_json

class AdminUtilizator:

    def __init__(self, fisier_date: str = "date_bancare.json"):
        self.fisier_date = fisier_date
        self.utilizatori: Dict[str, UtilizatorBancar] = self._incarca_utilizatori()

    def _incarca_utilizatori(self) -> Dict[str, UtilizatorBancar]:
        date_brute = incarca_json(self.fisier_date)
        return {
            user: UtilizatorBancar.from_dict(info)
            for user, info in date_brute.items()
        }

    def _salveaza_utilizatori(self) -> None:
        date_serializate = {user: obj.to_dict() for user, obj in self.utilizatori.items()}
        salveaza_json(self.fisier_date, date_serializate)

    def _genereaza_iban_unic(self) -> str:
        ibanuri_existente = {u.iban for u in self.utilizatori.values()}
        while True:
            cifre_control = random.randint(10, 99)
            numar_cont = "".join(str(random.randint(0, 9)) for _ in range(16))
            iban_nou = f"RO{cifre_control}SIMU{numar_cont}"
            if iban_nou not in ibanuri_existente:
                return iban_nou

    def sign_up(self, nume_complet: str, username: str, parola: str, sold_initial: float = 0.0) -> UtilizatorBancar:
        username_curat = username.strip().lower()

        if not nume_complet.strip():
            raise ValueError("Numele complet este obligatoriu.")
        if not username_curat:
            raise ValueError("Username-ul este obligatoriu.")
        if len(parola) < 4:
            raise ValueError("Parola trebuie să aibă cel puțin 4 caractere.")
        if sold_initial < 0:
            raise ValueError("Soldul inițial nu poate fi negativ.")
        if username_curat in self.utilizatori:
            raise ValueError(f"Username-ul '{username_curat}' este deja folosit.")

        utilizator_nou = UtilizatorBancar(
            nume_complet=nume_complet,
            username=username_curat,
            parola=parola,
            iban=self._genereaza_iban_unic(),
            sold=sold_initial
        )

        self.utilizatori[username_curat] = utilizator_nou
        self._salveaza_utilizatori()
        return utilizator_nou

    def listeaza_utilizatori(self) -> List[UtilizatorBancar]:
        return list(self.utilizatori.values())
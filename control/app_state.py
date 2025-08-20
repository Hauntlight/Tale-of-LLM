import csv
import os

class AppState:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance


    def initialize(self):
        self._highscores_path = "save/highscores.sav"
        self.config_path = "save/config.prop"
        self._api = self.load_api()
        self._highscores = self.carica_highscore()
        #print(self._highscores)


    def set_api_key(self, key):
        self._api = key

    def get_api_key(self):
        return self._api

    def get_highscores(self):
        return self._highscores

    def aggiorna_highscore(self, name, gold):
        nuovo = {"name": name, "gold": gold}

        if len(self._highscores) < 5:
            self._highscores.append(nuovo)
        else:
            min_gold = min(self._highscores, key=lambda x: x["gold"])["gold"]
            if gold > min_gold:
                self._highscores.append(nuovo)

        self._highscores.sort(key=lambda x: x["gold"], reverse=True)
        self._highscores = self._highscores[:5]

        self.salva_highscore()


    def salva_highscore(self):
        os.makedirs(os.path.dirname(self._highscores_path), exist_ok=True)
        with open(self._highscores_path, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "gold"])
            writer.writeheader()
            for row in self._highscores:
                writer.writerow(row)

    def carica_highscore(self):
        file_path = self._highscores_path
        dati = []
        if not os.path.exists(file_path):
            return dati
        try:
            with open(file_path, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        gold_value = int(row["gold"])
                    except (ValueError, KeyError):
                        gold_value = 0
                    name_value = row.get("name", "???")
                    dati.append({"name": name_value, "gold": gold_value})
        except Exception:
            return []

        dati.sort(key=lambda x: x["gold"], reverse=True)
        return dati


    def load_api(self):
        prop_path = self.config_path
        try:
            if not os.path.isfile(prop_path):
                return ""
            with open(prop_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("GEMINI_API_KEY"):
                        _, val = line.split("=", 1)
                        api_key_value = val.strip()
                        if not api_key_value:
                            return ""
                        return api_key_value
            return ""
        except Exception:
            return ""

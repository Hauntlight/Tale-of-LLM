import random

from data.data_class import DataClass
from model.entita import Entita


class Adventure():

    def __init__(self, ambiente, game):
        self.storia = ""
        self.ambiente_dettagliato = {
            "nome": ambiente,
            "desc": DataClass.ambienti_info[ambiente]["desc"],
            "incontri": DataClass.ambienti_info[ambiente]["incontri"]
        }
        self.avversario = self.genera_incontro(self.ambiente_dettagliato)
        self.game_parent = game
        self.giocatore = game.giocatore
        #self.ambiente_dettagliato

    def genera_incontro(self, ambiente):
        nomi = [incontro[0] for incontro in ambiente["incontri"]]
        pesi = [incontro[1] for incontro in ambiente["incontri"]]

        nome_entita_scelta = random.choices(nomi, weights=pesi, k=1)[0]
        dati_entita = DataClass.entity_info[nome_entita_scelta]

        return Entita(
            nome=nome_entita_scelta,
            hp_range=dati_entita["hp_range"],
            coeff_fis=dati_entita["coeff_fis"],
            coeff_mag=dati_entita["coeff_mag"],
            tipo_danno_out=dati_entita["tipo_danno_out"],
            premio_gold=dati_entita["premio_gold"],
            desc=dati_entita["desc"]
        )


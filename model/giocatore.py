from data.data_class import DataClass
from model.personaggio import Personaggio


class Giocatore(Personaggio):
    def __init__(self, nome, classe_scelta):
        info = DataClass.classe_info[classe_scelta]
        super().__init__(nome, info["hp"])
        self.classe = classe_scelta
        self.descrizione = info["desc"]
        self.coeff_fisico_in = info["coeff_fis"]
        self.coeff_magico_in = info["coeff_mag"]
        self.tipo_danno_inflitto = info["tipo_danno"]
        self.gold = 0

    def subisci_danno_giocatore(self, danno_base, tipo_danno):
        return super().subisci_danno(danno_base, self.coeff_fisico_in, self.coeff_magico_in, tipo_danno)

    def cura(self, hp_nemico_sconfitto):
        recupero = int(hp_nemico_sconfitto * 0.30)
        self.hp += recupero
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def aggiungi_gold(self, quantita):
        self.gold += quantita

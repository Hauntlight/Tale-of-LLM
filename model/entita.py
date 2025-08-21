import random

from model.personaggio import Personaggio


class Entita(Personaggio):
    def __init__(self, nome, hp_range, coeff_fis, coeff_mag, tipo_danno_out, premio_gold, desc):
        hp = random.randint(hp_range[0], hp_range[1])
        super().__init__(nome, hp)
        self.coeff_fisico_in = coeff_fis
        self.coeff_magico_in = coeff_mag
        self.tipo_danno_inflitto = tipo_danno_out
        self.premio_gold = premio_gold
        self.descrizione = desc

    def subisci_danno_entita(self, danno_base, tipo_danno_giocatore):
        return super().subisci_danno(danno_base, self.coeff_fisico_in, self.coeff_magico_in, tipo_danno_giocatore)

    def calcola_premio(self):
        return random.randint(self.premio_gold[0], self.premio_gold[1])
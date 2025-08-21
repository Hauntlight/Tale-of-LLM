import random


class Personaggio:
    def __init__(self, nome, hp_max):
        self.nome = nome
        self.hp_max = hp_max
        self.hp = hp_max

    def is_alive(self):
        return self.hp > 0

    def subisci_danno(self, danno_base, coeff_fisico, coeff_magico, tipo_danno):
        danno_reale = 0
        if tipo_danno == "fisico":
            danno_reale = int(danno_base * random.randint(coeff_fisico[0], coeff_fisico[1]))
        elif tipo_danno == "magico":
            danno_reale = int(danno_base * random.randint(coeff_magico[0], coeff_magico[1]))
        elif tipo_danno == "misto":
            danno_fisico = int((danno_base / 2) * random.randint(coeff_fisico[0], coeff_fisico[1]))
            danno_magico = int((danno_base / 2) * random.randint(coeff_magico[0], coeff_magico[1]))
            danno_reale = danno_fisico + danno_magico

        self.hp -= danno_reale
        if self.hp < 0:
            self.hp = 0
        return danno_reale
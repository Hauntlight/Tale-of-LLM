from control.adventure import Adventure
from model.giocatore import Giocatore


class Game:
    def __init__(self,nome_giocatore,classe_scelta):
        self.storia = ""
        self.giocatore = Giocatore(nome_giocatore,classe_scelta)
        self.avventura_corrente = None

    def inizia_nuova_avventura(self, ambiente):
        self.avventura_corrente = Adventure(ambiente,self)
        pass

    def finisci_partita(self):
        pass
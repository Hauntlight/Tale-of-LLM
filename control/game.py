import random

from control.adventure import Adventure
from model.giocatore import Giocatore


class Game:
    def __init__(self,nome_giocatore,classe_scelta):
        self.storia = ""
        self.giocatore = Giocatore(nome_giocatore,classe_scelta)
        self.avventura_corrente = None

    def inizia_nuova_avventura(self, ambiente):
        if self.avventura_corrente is not None:
            if self.storia != "":
                self.storia = self.storia +"\n" + random.sample(["Poi...","Successivamente...", "Incredibilmente...","Sorprendentemente...", "Nella successiva avventura..."],1)[0] + "\n" + self.avventura_corrente.storia
            else:
                self.storia = "Inizialmente..." +"\n"+self.avventura_corrente.storia
        self.avventura_corrente = Adventure(ambiente,self)


    def finisci_partita(self):
        if self.avventura_corrente is not None:
            self.storia = self.storia + "\n" + "Infine \n" + self.avventura_corrente.storia
        self.storia = self.storia + "\n" + f"Al termine di questa avventura {self.giocatore.nome} decise di ritirarsi! \n"
        self.avventura_corrente = None
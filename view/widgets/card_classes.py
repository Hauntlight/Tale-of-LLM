from control.classes_cards_controls import ClassesCardControls
from view.widgets.card import Card


class CardClasses(Card):
    def __init__(self, classe, modal, size, **kwargs):
        immagine = classe["img"]
        self.descrizione = classe["nome_classe"]

        self.controls = ClassesCardControls()
        super().__init__(immagine,self.descrizione,modal,size,**kwargs)

    def on_press(self):
        self.controls.generate_game(self.descrizione)
        super().on_press()



from control.ambient_card_controls import AmbientCardControls
from control.classes_cards_controls import ClassesCardControls
from view.widgets.card import Card


class CardAmbiente(Card):
    def __init__(self, ambiente, modal, size, **kwargs):
        immagine = ambiente["small_img"]
        self.descrizione = ambiente["nome"]

        self.controls = AmbientCardControls()
        super().__init__(immagine,self.descrizione,modal,size,**kwargs)

    def on_press(self):
        self.controls.startAdventure(self.descrizione)
        super().on_press()



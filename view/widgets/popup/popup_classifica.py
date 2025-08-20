import os

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import csv

from control.app_state import AppState


class PopupClassifica(Popup):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Classifica Record"
        self.size_hint = (0.8, 0.8)

        layout = GridLayout(cols=2, spacing=5, padding=10)

        layout.add_widget(Label(text="[b]Nome[/b]", markup=True))
        layout.add_widget(Label(text="[b]Gold[/b]", markup=True))

        dati = AppState().carica_highscore()

        for row in dati:
            layout.add_widget(Label(text=row["name"]))
            layout.add_widget(Label(text=str(row["gold"])))

        self.content = layout
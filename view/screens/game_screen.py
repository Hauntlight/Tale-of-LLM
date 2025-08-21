import random

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from control.app_state import AppState
from data.data_class import DataClass
from view.widgets.buttons.menu_button import MenuButton
from view.widgets.card_ambiente import CardAmbiente
from view.widgets.layouts.main_screen_layout import MainScreenLayout


class GameScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='horizontal', spacing=5, padding=5)
        self.bgLayout = MainScreenLayout("assets/images/ui/woods.jpg", orientation='vertical', spacing=5, padding=5,
                                         size_hint_x=2)

        left_column = BoxLayout(orientation='vertical', spacing=5, padding=5, size_hint_x=1)
        right_column = BoxLayout(orientation='vertical', spacing=5, padding=5, size_hint_x=1)
        self.enemy_image = Image(source="assets/images/entities/green_goblin.png", size_hint=(1, 0.4), allow_stretch=True,
                                  keep_ratio=True)

        self.enemy_label = Label(text="Enemy", size_hint=(1, 0.6), halign='center', valign='middle')
        right_column.add_widget(self.enemy_image)
        right_column.add_widget(self.enemy_label)
        self.little_image = Image(source="assets/images/classes/warrior.png", size_hint=(1, 0.4), allow_stretch=True,
                                  keep_ratio=True)
        self.label_name = Label(text="Name", size_hint=(1, 0.2), halign='center', valign='middle')
        self.label_hp = Label(text="0/0 HP", size_hint=(1, 0.2), halign='center', valign='middle')
        self.label_gold = Label(text="0 G", size_hint=(1, 0.2), halign='center', valign='middle')
        left_column.add_widget(self.little_image)
        left_column.add_widget(self.label_name)
        left_column.add_widget(self.label_hp)
        left_column.add_widget(self.label_gold)

        self.scroll_view = ScrollView(size_hint=(1, 0.9))
        self.chat_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.scroll_view.add_widget(self.chat_layout)

        # Input area
        input_layout = BoxLayout(size_hint=(1, 0.1), spacing=5)
        self.text_input = TextInput(multiline=False, hint_text="Cosa vuoi fare?", size_hint_x=0.8)
        self.text_input.bind(on_text_validate=self.send_message)
        send_button = MenuButton(text="Agisci!", size_hint_x=0.2)
        send_button.bind(on_press=self.send_message)
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(send_button)

        self.bgLayout.add_widget(self.scroll_view)
        self.bgLayout.add_widget(input_layout)
        root.add_widget(left_column)
        root.add_widget(self.bgLayout)
        root.add_widget(right_column)
        self.add_widget(root)

    def add_message(self, text, right=False):
        label = Label(
            text=text,
            size_hint_y=None,
            halign='right' if right else 'left',
            valign='middle',
            text_size=(250, None),
        )
        label.bind(texture_size=label.setter('size'))

        box = BoxLayout(size_hint_y=None, height=label.texture_size[1] + 20)
        if right:
            box.add_widget(Label(size_hint_x=1))
            box.add_widget(label)
        else:
            box.add_widget(label)
            box.add_widget(Label(size_hint_x=1))

        self.chat_layout.add_widget(box)

    def send_message(self, instance):
        message = self.text_input.text.strip()
        if message:
            self.add_message(f"You: {message}", right=True)
            self.text_input.text = ""
            self.add_message("RECEIVED", right=False)

    def on_pre_enter(self):
        super().on_pre_enter()
        self.little_image.source = DataClass.classe_info[AppState().game.giocatore.classe]["img"]
        self.label_name.text = AppState().game.giocatore.nome
        self.little_image.reload()
        self.update_datas()

    def on_enter(self, *args):
        super().on_enter()
        chiavi = list(DataClass.ambienti_info.keys())
        ambienti_casuali = random.sample(chiavi,2)
        self.show_environments(ambienti_casuali)


    def show_environments(self,ambienti):
        modal = ModalView(size_hint=(0.9, 0.6), auto_dismiss=False)
        modal.bind(on_dismiss=lambda *a: self.update_adventure())
        main_content = BoxLayout(orientation='vertical', padding=20, spacing=10)

        sub_content = BoxLayout(orientation='horizontal', padding=20, spacing=10)

        card1 = CardAmbiente(DataClass.ambienti_info[ambienti[0]], modal, size=0.5)
        card2 = CardAmbiente(DataClass.ambienti_info[ambienti[1]], modal, size=0.5)

        new_label = Label(text="Dove vuoi andare", size_hint=(1, 0.1), halign='center', valign='middle')

        main_content.add_widget(new_label)
        sub_content.add_widget(card1)
        sub_content.add_widget(card2)
        main_content.add_widget(sub_content)
        modal.add_widget(main_content)
        modal.open()

    def update_adventure(self):
        self.bgLayout.set_background(DataClass.ambienti_info[AppState().game.avventura_corrente.ambiente_dettagliato["nome"]]["img"])
        self.enemy_image.source = DataClass.entity_info[AppState().game.avventura_corrente.avversario.nome]["img"]
        self.enemy_label.text = AppState().game.avventura_corrente.avversario.nome
        self.enemy_image.reload()

    def update_datas(self):
        self.label_hp.text = f"{AppState().game.giocatore.hp}/{AppState().game.giocatore.hp_max} HP"
        self.label_gold.text = f"{AppState().game.giocatore.gold} G"

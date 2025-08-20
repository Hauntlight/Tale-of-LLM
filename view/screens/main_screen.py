from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from view.widgets.buttons.menu_button import MenuButton
from view.widgets.layouts.main_screen_layout import MainScreenLayout


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        background = MainScreenLayout(orientation="vertical", padding=20, spacing=10)

        base_layout = BoxLayout(orientation="horizontal", padding=20, spacing=10)
        left_layout = BoxLayout(orientation="vertical")
        center_layout = BoxLayout(orientation="vertical",spacing=20, padding=[0, 20, 0, 0])
        right_layout = BoxLayout(orientation="vertical")

        crediti_button = MenuButton(text="Informazioni", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        crediti_button.bind(on_release=self.open_infos)
        left_layout.add_widget(crediti_button)


        center_layout.add_widget(Label(text="Tales of LLM",
                                       font_size="50sp", font_name="assets/font/FontdinerSwanky-Regular.ttf",
                                       color=(0, 0, 0, 1)))

        center_layout.add_widget(
            MenuButton(text="Nuova Partita", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5}))
        setting_button = MenuButton(text="Impostazioni", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        setting_button.bind(on_release=self.open_settings)

        center_layout.add_widget(setting_button)

        right_layout.add_widget(
            MenuButton(text="Punteggi migliori", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5}))




        base_layout.add_widget(left_layout)
        base_layout.add_widget(center_layout)
        base_layout.add_widget(right_layout)
        background.add_widget(base_layout)
        self.add_widget(background)


    def open_settings(self, *args):
        modal = ModalView(size_hint=(0.9, 0.3), auto_dismiss=False)
        outer_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        layout = BoxLayout(orientation="horizontal", padding=20, spacing=10)
        close_button = MenuButton(text="Chiudi", pos_hint={"center_x": 0.5, "center_y": 0.5})
        text_input = TextInput(
            multiline=False,
            hint_text="API key",
            size_hint_y=None,
            height=dp(50),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        #text_input.bind(on_text_validate=self.save_message)
        save_button = MenuButton(
            text="Salva API key",
            size_hint=(None, None),  # Fixed size
            size=(dp(100), dp(50)),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        close_button.bind(on_release=lambda *a: modal.dismiss())
        layout.add_widget(text_input)
        layout.add_widget(save_button)
        outer_layout.add_widget(layout)
        outer_layout.add_widget(close_button)
        modal.add_widget(outer_layout)
        modal.open()

    def open_infos(self, *args):
        text = (
            "CREDITI ed INFORMAZIONI UTILI - Tales of LLM\n\n"
            "Font: Il software utilizza il carattere Fontdiner Swanky, distribuito sotto licenza Apache 2.0. "
            "Testo completo disponibile su: https://fonts.google.com/specimen/Fontdiner+Swanky/license\n\n"
            "Audio: Gli effetti sonori e le tracce audio provengono da Pixabay (https://pixabay.com/), "
            "utilizzati nel rispetto delle condizioni di utilizzo gratuite e commerciali.\n\n"
            "Immagini: Le immagini sono state generate con DeepAI (https://deepai.org/), "
            "conformemente ai termini della piattaforma.\n\n"
            "Python: Il progetto utilizza Python, concesso sotto Python Software Foundation License (PSF). "
            "È liberamente utilizzabile, modificabile e distribuibile. Maggiori dettagli: https://docs.python.org/3/license.html\n\n"
            "Kivy: La GUI è sviluppata con Kivy, rilasciato sotto licenza MIT. "
            "La licenza consente uso e modifiche mantenendo copyright e disclaimer. "
            "Ulteriori informazioni: https://kivy.org/doc/stable/#license\n\n"
            "PyInstaller: L’installer è generato con PyInstaller, che permette la creazione di eseguibili "
            "senza obbligo di rendere pubblico il codice sorgente.\n\n"
            "Google Gemini API: Alcune funzioni richiedono l’uso dell’API Google Gemini. "
            "L’utente deve ottenere una chiave API personale da https://aistudio.google.com/app/apikey "
            "e rispettare i termini di servizio di Google Cloud. "
            "La chiave non è criptata: si consiglia di generarne una dedicata e limitata. "
            "Il software non fornisce chiavi API, non è affiliato a Google e non è responsabile di costi o usi impropri.\n\n"
            "Nota: Tales of LLM è reso possibile grazie al contributo della comunità open-source "
            "e delle piattaforme citate, il cui lavoro è qui riconosciuto e apprezzato.\n\n"
        )

        label = Label(
            text=text,
            size_hint_y=None,
            text_size=(Window.width * 0.8, None),
            halign="left",
            valign="top"
        )
        label.bind(texture_size=lambda inst, val: setattr(inst, "height", val[1]))

        scrollview = ScrollView(size_hint=(1, 1))
        scrollview.add_widget(label)

        close_button = MenuButton(text="Chiudi",pos_hint={"center_x": 0.5, "center_y": 0.5})
        modal = ModalView(size_hint=(0.9, 0.9), auto_dismiss=False)

        close_button.bind(on_release=lambda *a: modal.dismiss())

        layout = BoxLayout(orientation="vertical", spacing=dp(10), padding=dp(10))
        layout.add_widget(scrollview)
        layout.add_widget(close_button)

        modal.add_widget(layout)
        modal.open()

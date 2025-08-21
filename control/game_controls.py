import os
import random
import time
from threading import Thread

from kivy.clock import Clock

from control.app_state import AppState
from datetime import datetime


class GameControls():

    def send_message(self, text, view):
        self.view = view
        message = text.strip()
        if message:
            view.add_message(f"\n{message}",title="[color=000000]Quello che vorresti accadesse:[/color]")
            view.text_input.text = ""
            view.text_input.disabled = True
            Thread(target=lambda *a: self.threaded_call(message,random.randint(1, 20) )).start()

    def threaded_call(self, azione_giocatore, dado):
        risposta_llm = AppState().game.avventura_corrente.chiama_llm(azione_giocatore, dado )
        Clock.schedule_once(lambda dt: self.update_ui(risposta_llm))

    def update_ui(self, risposta_llm):
        info_storia = risposta_llm.get("Story_Infos", "Qualcosa è andato storto nella narrazione.")
        risultato, v, inflitto = AppState().game.avventura_corrente.combattimento(risposta_llm)
        if risultato == "turno":
            if v > 0:
                info_storia = info_storia + "\n" + f"[color=ff0000]Hai subito {v} danni![/color]"
            if inflitto is not None and inflitto > 0:
                info_storia = info_storia + "\n" + "[color=00ff00]Hai danneggiato il tuo avversario![/color]"

        self.view.add_message(f"[color=000000][b]Quello che succede:[/b][/color] \n {info_storia}", [1, 0.5, 0],markup=True)
        self.view.text_input.disabled = False
        self.view.update_datas()
        if risultato == "vittoria" or risultato == "vittoria_narrativa" or risultato == "alternativo":
            premio = AppState().game.avventura_corrente.entita.calcola_premio()
            AppState().game.giocatore.aggiungi_gold(premio)
            AppState().game.giocatore.cura(v)
            self.view.win(premio)
        elif risultato == "fuga":
            premio = 0
            AppState().game.giocatore.aggiungi_gold(premio)
            AppState().game.giocatore.cura(v // 3)
            self.view.run()
        elif risultato == "sconfitta":  # Sconfitta
            self.view.lose()

    def continua_partita(self):
        self.view.initialize()

    def fine_partita(self):
        AppState().game.finisci_partita()
        AppState().aggiorna_highscore(AppState().game.giocatore.nome,AppState().game.giocatore.gold)
        self.view.mostra_popup()

    def torna_al_menu(self):
        self.view.change_scene("main_screen")

    def save_story(self):
        now = datetime.now()
        formatted_time = now.strftime("%d_%m_%Y_%H_%M_%S")
        testo = AppState().game.storia
        nome_file = AppState().game.giocatore.nome + "_" + formatted_time + ".txt"
        save_folder = "save"
        os.makedirs(save_folder, exist_ok=True)

        full_path = os.path.join(save_folder, nome_file)

        text = ""

        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(testo)
            text = f"Salvataggio riuscito come {nome_file}"
        except Exception as e:
            text = f"Errore nel salvataggio: {e}"

        self.view.mostra_messaggio_salvataggio(text)







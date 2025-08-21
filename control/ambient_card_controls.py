from control.app_state import AppState


class AmbientCardControls:

    def startAdventure(self, ambiente):
        AppState().game.inizia_nuova_avventura(ambiente)
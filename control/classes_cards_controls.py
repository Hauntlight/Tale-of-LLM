from control.app_state import AppState


class ClassesCardControls:
    def generate_game(self,classe):
        AppState().create_game(classe)


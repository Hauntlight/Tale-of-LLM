import os

from control.app_state import AppState


class MainScreenControls():
    def __init__(self,view):
        self.view = view

    def save_settings(self, api_key_value):
        prop_path = AppState().config_path

        if not api_key_value:
            self.view.show_popup("Errore", "La API key non può essere vuota.")
            return

        try:
            os.makedirs(os.path.dirname(prop_path), exist_ok=True)
            with open(prop_path, "w", encoding="utf-8") as f:
                f.write(f"GEMINI_API_KEY={api_key_value}\n")
            AppState().set_api_key(api_key_value)
            self.view.show_popup("Successo", "API key salvata correttamente.")
        except Exception as e:
            self.view.show_popup("Errore", f"Si è verificato un problema: {e}")

    def get_api_key(self):
        return AppState().get_api_key()

    def conferma_nome(self, nome):
        if not nome:
            self.view.show_popup("Errore", "Il nome non può essere vuoto.")
            return -1
        AppState().nome = nome
        return 1


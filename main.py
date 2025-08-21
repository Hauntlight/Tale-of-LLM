from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.app import App

from control.app_state import AppState
from view.screens.game_screen import GameScreen
from view.screens.main_screen import MainScreen
from kivy.config import Config

from view.widgets.manager.custom_manager import CustomManager

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class Tales_Of_LLM(App):
    def build(self):
        self.title = "Tale of LLM"
        self.icon = "assets/ico/icon.png"
        self.sm = CustomManager(transition=FadeTransition())
        main_scene = MainScreen(name="main_screen")
        game_scene = GameScreen(name="game_screen")
        self.sm.add_widget(main_scene)
        self.sm.add_widget(game_scene)
        inspector.create_inspector(Window, self.sm) #INSPECTOR
        return self.sm




if __name__ == "__main__":
    app_data = AppState()
    Tales_Of_LLM().run()

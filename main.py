from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.app import App

from control.app_state import AppState
from view.screens.main_screen import MainScreen
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MainGame(App):
    def build(self):
        self.icon = "assets/ico/icon.png"
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MainScreen(name="main_screen"))
        inspector.create_inspector(Window, sm) #INSPECTOR
        return sm


if __name__ == "__main__":
    app_data = AppState()
    MainGame().run()

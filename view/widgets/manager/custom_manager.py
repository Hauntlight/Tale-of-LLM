from kivy.uix.screenmanager import ScreenManager

from view.screens.game_screen import GameScreen


class CustomManager(ScreenManager):

    def new_game(self):
        if self.has_screen("game_screen"):
            self.remove_widget(self.get_screen("game_screen"))
        self.add_widget(GameScreen(name="game_screen"))
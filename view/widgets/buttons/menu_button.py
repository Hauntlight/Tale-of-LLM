from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window

from view.widgets.hover_behavior import HoverBehavior


class MenuButton(ButtonBehavior, BoxLayout, HoverBehavior):
    def __init__(self, text="", **kwargs):
        super().__init__(orientation='vertical', padding=dp(10), spacing=dp(5), **kwargs)
        self.size_hint = (None, None)
        self.width = dp(200)
        self.height = dp(50)

        self.default_color = (1, 0.5, 0, 1)
        self.hover_color = (0.9, 0.4, 0, 1)
        self.press_color = (0.8, 0.3, 0, 1)

        with self.canvas.before:
            self.bg_color = Color(*self.default_color)
            self.bg = RoundedRectangle(size=self.size, pos=self.pos, radius=[dp(25)])

        self.bind(pos=self._update_bg, size=self._update_bg)

        self.label = Label(
            text=text,
            halign="center",
            valign="middle",
            color=(1, 1, 1, 1),
            font_name="assets/font/FontdinerSwanky-Regular.ttf"
        )
        self.label.bind(size=self._update_text_size)
        self.add_widget(self.label)

        self.click_sound = SoundLoader.load("assets/sounds/sfx/click.mp3")

    def _update_text_size(self, *args):
        self.label.text_size = self.label.size

    def _update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def on_enter(self):
        self.bg_color.rgba = self.hover_color

    def on_leave(self):
        self.bg_color.rgba = self.default_color

    def on_press(self):
        self.bg_color.rgba = self.press_color
        if self.click_sound:
            self.click_sound.play()

    def on_release(self):
        self.bg_color.rgba = self.hover_color if getattr(self, "_hovered", False) else self.default_color

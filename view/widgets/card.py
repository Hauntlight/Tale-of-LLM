from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from view.widgets.hover_behavior import HoverBehavior


class Card(ButtonBehavior, BoxLayout, HoverBehavior):
    def __init__(self, image_source, description, modal,size, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=5, **kwargs)
        self.size_hint = (size, 1)
        self.modal = modal

        self.hover_color = (0.9, 0.4, 0, 1)
        self.press_color = (0.8, 0.3, 0, 1)
        self.default_color = (0.9, 0.9, 0.9, 0.5)

        with self.canvas.before:
            self.bg_color = Color(*self.default_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.img = Image(source=image_source, size_hint=(1, 0.7), allow_stretch=True, keep_ratio=True)
        self.add_widget(self.img)

        self.label = Label(text=description, size_hint=(1, 0.3), halign='center', valign='middle')
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)
        self.click_sound = SoundLoader.load("assets/sounds/sfx/click.mp3")

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_press(self):
        self.bg_color.rgba = self.press_color
        if self.click_sound:
            self.click_sound.play()
        self.modal.dismiss()

    def on_enter(self):
        self.bg_color.rgba = self.hover_color

    def on_leave(self):
        self.bg_color.rgba = self.default_color
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout



class MainScreenLayout(BoxLayout):
    def __init__(self,background, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(source=background, pos=self.pos, size=self.size)
            Color(1, 1, 1, 0.5)
            self.overlay = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.overlay.pos = self.pos
        self.overlay.size = self.size

    def set_background(self, new_background):
        self.bg.source = new_background
        self.canvas.ask_update()
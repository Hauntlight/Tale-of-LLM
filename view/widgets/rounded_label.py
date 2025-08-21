from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle


class RoundedLabel(BoxLayout):
    def __init__(self, text="", colore=[0.3, 0.5, 0.7],markup=False,title=None, **kwargs):
        super().__init__(**kwargs)
        self.padding = (10, 5)
        self.size_hint_y = None
        self.orientation = "vertical"

        with self.canvas.before:
            Color(colore[0], colore[1], colore[2], 1)
            self.rect = RoundedRectangle(radius=[15], pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        self.title = None

        if title is not None:
            self.title = Label(
                text=title,
                size_hint_y=None,
                halign="justify",
                valign="middle",
                font_name="assets/font/FontdinerSwanky-Regular.ttf",
                markup=True
            )
            self.title.bind(texture_size=self.update_size, size=self.update_title_size)
            self.add_widget(self.title)

        self.label = Label(
            text=text,
            size_hint_y=None,
            halign="justify",
            valign="middle",
            font_name="assets/font/FontdinerSwanky-Regular.ttf",
            markup=markup
        )
        self.label.bind(texture_size=self.update_size, size=self.update_text_size)
        self.add_widget(self.label)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_text_size(self, *args):
        self.label.text_size = (self.label.width, None)

    def update_size(self, *args):
        sum = 20
        if self.title is not None:
            self.title.height = self.title.texture_size[1]
            sum = sum + 20
        self.label.height = self.label.texture_size[1]
        self.height = self.label.height + sum



    def update_title_size(self, *args):
        self.title.text_size = (self.title.width, None)

from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView


class QuickMessage(ModalView):
    def __init__(self, message, duration=3, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.5, 0.2)
        self.auto_dismiss = False
        self.add_widget(Label(text=message))
        Clock.schedule_once(lambda dt: self.dismiss(), duration)
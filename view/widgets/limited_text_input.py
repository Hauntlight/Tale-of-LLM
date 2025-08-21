from kivy.uix.textinput import TextInput


class LimitedTextInput(TextInput):


    def __init__(self, max_chars = 250, **kwargs):
        super().__init__(**kwargs)
        self.max_chars = 250
        self.register_event_type('on_text_validate')

    def insert_text(self, substring, from_undo=False):
        if len(self.text) + len(substring) > self.max_chars:
            substring = substring[: self.max_chars - len(self.text)]
        super().insert_text(substring, from_undo=from_undo)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == 'enter':
            if 'shift' in modifiers:
                return super().keyboard_on_key_down(window, keycode, text, modifiers)
            else:
                self.dispatch('on_text_validate')
                return True
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

    def on_text_validate(self, *args):
        pass
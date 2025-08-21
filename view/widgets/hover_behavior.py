from kivy.core.window import Window


class HoverBehavior:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, window, pos):
        if not self.get_root_window():
            return
        inside = self.collide_point(*self.to_widget(*pos))
        if inside and not getattr(self, "_hovered", False):
            self._hovered = True
            self.on_enter()
        elif not inside and getattr(self, "_hovered", False):
            self._hovered = False
            self.on_leave()

    def on_enter(self):
        pass

    def on_leave(self):
        pass
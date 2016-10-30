from .base import Widget

class MenuItem(Widget):
    """
    Menu item widget

    :param label:          Text to be shown on the menu item
    :type label:           str
    :param id:             Identifier for this widget
    :param style:          Style of the menu
    :type style:           colosseum.CSS
    :param on_press:       Function to execute when pressed
    :type on_press:        Callable
    :param key_equivalent: Shortcut key
    :type on_press:        str
    """
    def __init__(self, label, id=None, style=None, on_press=None,
                 key_equivalent=None):
        super().__init__(id=id, style=style, label=label, on_press=on_press,
                         key_equivalent=key_equivalent)
        self._children = []

    def _configure(self, label, on_press, key_equivalent):
        self.label = label
        self.on_press = on_press
        self.key_equivalent = key_equivalent

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        if value is None:
            self._label = ''
        else:
            self._label = str(value)
        self._set_label(value)
        self.rehint()

    def _set_label(self, value):
        raise NotImplementedError('MenuItem widget must define _set_label()')

    @property
    def on_press(self):
        return self._on_press

    @on_press.setter
    def on_press(self, handler):
        self._on_press = handler
        if handler:
            self._set_on_press(handler)

    def _set_on_press(self, value):
        pass

    @property
    def key_equivalent(self):
        return self._key_equivalent

    @key_equivalent.setter
    def key_equivalent(self, value):
        self._key_equivalent = value
        if value:
            self._set_key_equivalent(value)

    def _set_key_equivalent(self, value):
        pass

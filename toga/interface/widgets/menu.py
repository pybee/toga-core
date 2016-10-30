from .base import Widget

class Menu(Widget):
    """
    Menu widget

    :param label:       Text to be shown on the super-menu
    :type label:        str
    :param id:          Identifier for this widget
    :param style:       Style of the menu
    :type style:        colosseum.CSS
    """
    def __init__(self, label, id=None, style=None):
        super().__init__(id=id, style=style, label=label)
        self._children = []

    def _configure(self, label):
        self.label = label

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
        raise NotImplementedError('Menu widget must define _set_label()')

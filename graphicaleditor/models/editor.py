#ILYA CHABAN
class Editor(object):
    def __init__(self, drawer, graf_doc, input_reader):
        self.drawer = drawer
        self.graf_doc = graf_doc
        self.input_reader = input_reader

    @property
    def drawer(self):
        return self._drawer

    @drawer.setter
    def drawer(self, value):
        self._drawer = value

    @property
    def graf_doc(self):
        return self._graf_doc

    @graf_doc.setter
    def grad_doc(self, value):
        self._graf_doc = value

    @property
    def input_reader(self):
        return self._input_reader

    @input_reader
    def input_reader(self, value):
        self._input_reader = value
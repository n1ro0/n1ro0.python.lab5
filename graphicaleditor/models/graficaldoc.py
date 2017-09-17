class GraficalDoc(object):
    def __init__(self, drawer):
        self.drawer = drawer
        self.figures = []

    @property
    def drawer(self):
        return self._drawer

    @drawer.setter
    def drawer(self, value):
        self._drawer = value

    @property
    def figures(self):
        return self._figures

    @figures.setter
    def figures(self, value):
        self._figures = value

    def create(self):
        pass

    def open(self, filename):
        pass

    def save(self, filename):
        pass

    def add(self, figure):
        pass



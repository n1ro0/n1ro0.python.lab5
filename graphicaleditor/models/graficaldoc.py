#ILYA CHABAN
class GraficalDoc(object):
    def __init__(self):
        self.figures = []

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

    def save(self, filename, save_method):
        data = [figure.to_dict() for figure in self.figures]
        save_method(filename, data)

    def add(self, figure):
        self.figures.append(figure)
        figure.draw()



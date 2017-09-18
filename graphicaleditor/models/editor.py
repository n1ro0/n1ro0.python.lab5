#ILYA CHABAN
from graphicaleditor.models.graficaldoc import GraficalDoc
from graphicaleditor.models.consolecommandreader import ConsoleCommandReader
from graphicaleditor.drawmodels.Line import Line
from graphicaleditor.drawmodels.Triangle import Triangle





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
    def graf_doc(self, value):
        self._graf_doc = value

    @property
    def input_reader(self):
        return self._input_reader

    @input_reader.setter
    def input_reader(self, value):
        self._input_reader = value

    @property
    def save_options(self):
        return self._save_options

    @save_options.setter
    def save_options(self, value):
        self._save_options = value

    def exec_command(self, command_list):
        if command_list[0] == "create":
            self.graf_doc = GraficalDoc()
        elif command_list[0] == "save":
            pass#self.graf_doc.save(command_list[1], save_options[command_list[0]])
        elif command_list[0] == "add":
            if command_list[1] == "line":
                figure = Line(self.drawer, (int(command_list[2]), int(command_list[3])),
                              (int(command_list[4]), int(command_list[5])))
            if command_list[1] == "triangle":
                figure = Triangle(self.drawer, (int(command_list[2]), int(command_list[3])),
                                  (int(command_list[4]), int(command_list[5])),
                                  (int(command_list[6]), int(command_list[7])))
            self.graf_doc.add(figure)

    def start(self):
        while True:
            self.exec_command(self.input_reader.request_command())
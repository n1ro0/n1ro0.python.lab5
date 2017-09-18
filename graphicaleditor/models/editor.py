#ILYA CHABAN
from graphicaleditor.models.graficaldoc import GraficalDoc
from graphicaleditor.drawmodels.Line import Line
from graphicaleditor.drawmodels.Triangle import Triangle
from graphicaleditor.models.consolecommandreader import CommandNode
import json
import pickle


class EditorCommandTree(object):
    def __init__(self):
        root_children = []
        self.root = CommandNode("root", (), None, root_children)
        root_children.append(CommandNode("create", (), self.root, []))
        root_children.append(CommandNode("save", ("filename",), self.root, []))
        add_children = []
        add_node = CommandNode("add", (), self.root, add_children)
        root_children.append(add_node)
        add_children.append(CommandNode("line", ("point1_x", "point1_y", "point2_x", "point2_y"), add_node, []))
        add_children.append(CommandNode("triangle", ("point1_x", "point1_y", "point2_x", "point2_y", "point3_x", "point3_y"), add_node, []))


class Editor(object):
    def __init__(self, drawer, graf_doc, input_reader):
        self.drawer = drawer
        self.graf_doc = graf_doc
        self.input_reader = input_reader
        self.register_save_methods()

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

    def json_save_method(self, filename, data):
        with open(filename, "w") as f:
            json_data = json.dumps(data)
            f.write(json_data)

    def pickle_save_method(self, filename, data):
        with open(filename, "wb") as f:
            pickle_data = pickle.dumps(data)
            f.write(pickle_data)

    def register_save_methods(self):
        self.save_options = {}
        self.save_options["json"] = self.json_save_method
        self.save_options["pickle"] = self.pickle_save_method

    def exec_command(self, command_list):
        if command_list[0] == "create":
            self.graf_doc = GraficalDoc()
        elif command_list[0] == "save":
            self.graf_doc.save(command_list[1], self.save_options[command_list[1].split(".")[1]])
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
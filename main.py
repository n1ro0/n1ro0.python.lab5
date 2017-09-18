from graphicaleditor.models.editor import Editor
from graphicaleditor.models.graficaldoc import GraficalDoc
from graphicaleditor.models.consolecommandreader import ConsoleCommandReader
from turtle import Turtle


if __name__ == "__main__":
    editor = Editor(Turtle(), GraficalDoc(), ConsoleCommandReader())
    editor.start()
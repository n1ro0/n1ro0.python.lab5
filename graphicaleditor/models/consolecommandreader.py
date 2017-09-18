#ILYA CHABAN
class CommandNode(object):
    def __init__(self, name, params, root, children):
        self.name = name
        self.params = params
        self.root = root
        self.children = children

class CommandTree(object):
    def __init__(self):
        root = CommandNode("root", (), None, )


class ConsoleCommandReader(object):

    def __init__(self, start_node):
        self.start_node = start_node

    def request_command(self):
        current_node = self.start_node
        command = []
        while len(current_node.children) != 0:
            current_node = current_node.children
            command.append(input(current_node.children))
            for param in current_node.params:
                command.append(input(param))


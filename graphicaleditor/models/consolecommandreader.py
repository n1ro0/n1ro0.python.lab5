#ILYA CHABAN
class CommandNode(object):
    def __init__(self, name, params, root, children):
        self.name = name
        self.params = params
        self.root = root
        self.children = children

    def child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child


class ConsoleCommandReader(object):

    def __init__(self, tree_root):
        self.root_node = tree_root

    def request_command(self):
        current_node = self.root_node
        command = []
        while len(current_node.children) != 0:
            node_name = None
            while node_name == None:
                node_name = input("Choose command: {}: ".format([node.name for node in current_node.children]))
                current_node = current_node.child_by_name(node_name)
                command.append(current_node.name)
                for param in current_node.params:
                    command.append(input(param))
        return command


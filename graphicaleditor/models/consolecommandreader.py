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

class EditorCommandTree(object):
    def __init__(self):
        root_children = []
        self.root = CommandNode("root", (), None, root_children)
        root_children.append(CommandNode("create", (), self.root, []))
        add_children = []
        add_node = CommandNode("add", (), self.root, add_children)
        root_children.append(add_node)
        add_children.append(CommandNode("line", ("point1_x", "point1_y", "point2_x", "point2_y"), add_node, []))
        add_children.append(CommandNode("triangle", ("point1_x", "point1_y", "point2_x", "point2_y", "point3_x", "point3_y"), add_node, []))

class ConsoleCommandReader(object):

    def __init__(self, ):
        self.root_node = EditorCommandTree().root

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


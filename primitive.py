from itertools import izip_longest
import json

__author__ = 'shefuto'


class Solver(object):
    _functions = []
    _nodes = []

    def _apply(self, *args):
        print "template apply"
        pass

    def __call__(self, *args):
        return self._apply(*args)


class Function(object):
    def __init__(self, solver):
        self.solver = solver


class Node(object):
    def __init__(self, value=None, branches=None, parent=None):
        """
        :param value:  a list of imutable objects, preferably of the same type
        :param branches: a list of nodes (preferably other ones)
        """
        self.value = value if value is not None else []
        self.branches = branches if branches is not None else []
        self.parent = parent

    def __str__(self):
        return json.dumps(
            {'id': id(self),
             'value': self.value,
             'branches': [json.loads(str(node)) for node in self.branches]
            })

    def __repr__(self):
        return str(self)


Node.EMPTY = Node([], [])


class DefFunc(Function):
    pass


class DefObj(Function):
    pass


def sum_nodes(*nodes):
    new_value = []
    for values in izip_longest(*(node.value for node in nodes),
                               fillvalue=0):
        new_value.append(sum(values))

    new_branches = []
    for branches in izip_longest(*(node.branches for node in nodes),
                                 fillvalue=Node.EMPTY):
        new_branches.append(sum_nodes(*branches))
    return Node(new_value, new_branches)


def invert_node(node):
    new_value = [-val for val in node.value]
    new_branches = []
    for child_node in node.branches:
        new_branches.append(invert_node(child_node))

    return Node(new_value, new_branches)


def load_nodes(args):
    """Creates the initial nodes, from the arguments list

    :param args: a list of arguments (simple data primitives, lists or
        nested lists
    :raises TypeError if `args` is not an iterable
    """

    def create_node(obj, parent=None):
        try:
            i = iter(obj)
        except TypeError:
            return Node([obj], parent=parent)

        value = []
        branches = []
        node = Node(value, branches, parent=parent)
        for elem in i:
            try:
                i = iter(elem)
                child = create_node(elem, node)
                child.parent = node
                branches.append(child)
            except TypeError:
                value.append(elem)
        return node

    root_nodes = []
    for arg in args:
        node = create_node(arg)
        root_nodes.append(node)

    def register_node_and_children(node, nodes_list):
        nodes_list.append(node)
        for child in node.branches:
            register_node_and_children(child, nodes_list)


    nodes = []
    for root in root_nodes:
        register_node_and_children(root, nodes)

    return nodes


def log(*args):
    print "loggd it"


def expanded_lambda(*args):
    print "expanded lambda"
    print len(args)


if __name__ == "__main__":
    s = Solver()
    # s._apply = expanded_lambda
    Solver._apply = expanded_lambda
    print s()
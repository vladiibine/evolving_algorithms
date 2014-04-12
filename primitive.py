from itertools import izip_longest
import json

__author__ = 'shefuto'


class Solver(object):
    _functions = []
    _nodes = []

    def __call__(self, *args):
        pass


class Function(object):
    def __init__(self, solver):
        self.solver = solver


class Node(object):
    def __init__(self, value=None, branches=None, parent=None):
        """
        :param value:  a list of imutable objects, preferably of the same type
        :param branches: a list of nodes (preferably other ones)
        """
        self.value = value if value else []
        self.branches = branches if branches else []
        self.parent = parent

    def __str__(self):
        return json.dumps(
            {'id': id(self),
             'value': self.value,
             'branches': [json.loads(str(node)) for node in self.branches]
            })


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


def get_nodes(args):
    """Creates the initial nodes, from the arguments list
    """
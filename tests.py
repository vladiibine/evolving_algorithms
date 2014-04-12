__author__ = 'shefuto'

from unittest import TestCase
from primitive import load_nodes


class LoadModulesTest(TestCase):
    def test_creates_node(self):
        args = [1]
        nodes = load_nodes(args)
        self.assertEqual(len(nodes), 1)

    def test_correct_number_of_nodes_simple(self):
        args = [1, 1]
        nodes = load_nodes(args)
        self.assertEqual(len(nodes), len(args))

    def test_correct_number_of_nested_nodes(self):
        args=[0,1,[2,[3]]]
        nodes = load_nodes(args)
        self.assertEqual(4, len(nodes))




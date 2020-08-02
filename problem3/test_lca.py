import unittest
from unittest import TestCase

from problem3.lca import Node, lca


class Test(TestCase):
    def test_lca(self):
        root = Node(1)
        node1 = root
        node2 = Node(2, root)
        node3 = Node(3, root)

        node4 = Node(4, node2)
        node5 = Node(5, node2)

        node6 = Node(6, node3)
        node7 = Node(7, node3)

        node8 = Node(8, node4)
        node9 = Node(9, node4)

        self.assertEqual(lca(node6, node7).value, 3)
        self.assertEqual(lca(node3, node7).value, 3)
        self.assertEqual(lca(node2, node9).value, 2)


if __name__ == '__main__':
    unittest.main()

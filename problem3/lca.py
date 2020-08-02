class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


def depth(n: Node, d=0):
    if n.parent:
        d = depth(n.parent, d + 1)
    return d


def lca(node1: Node, node2: Node):
    """
    :param node1: A Node object
    :param node2: A Node object
    :return: A Node object
    """
    # print(node1.value, node2.value)
    if not node1.parent:
        return node1
    elif not node2.parent:
        return node2

    if node1.parent == node2.parent:
        return node1.parent

    if node2.parent == node1:
        return node1
    elif node1.parent == node2:
        return node2

    n1d = depth(node1)
    n2d = depth(node2)
    if n1d>n2d:
        return lca(node1.parent, node2)
    elif n2d>n1d:
        return lca(node1, node2.parent)
    return lca(node1.parent, node2.parent)


if __name__ == '__main__':
    print('LCA')
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
    print(lca(node3, node7).value)
    

"""
Runtime: O(N), where N is the number of depth in the tree. In the worst case, this might be visiting the full depth of the tree.

Memory: O(N). This is because the maximum amount of space utilized by the recursion stack would be N since the number of nodes could be N.

"""

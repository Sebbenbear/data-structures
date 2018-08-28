import unittest
from avl_tree import AVLTree

class TestStringMethods(unittest.TestCase):

    # test traversal with no root
    def test_traversalWithNoRoot(self):
        tree = AVLTree()
        nodes = tree.preorder_traversal()
        self.assertEqual(nodes, [])

    #  4
    #
    def test_insertPreOrderTreeWithRoot(self):
        tree = AVLTree()
        tree.insert(4)
        nodes = tree.preorder_traversal()
        self.assertEqual(nodes, [4])

    def test_insertPreOrderTreeWithRootLetter(self):
        tree = AVLTree()
        tree.insert('a')
        nodes = tree.preorder_traversal()
        self.assertEqual(nodes, ['a'])

    def test_insertPreOrderCheckTypeErrorRaised(self):
        tree = AVLTree()
        tree.insert('a')
        try:
            tree.insert(4)
        except TypeError:
            return True

    #   4
    #  /
    # 3
    def test_insertPreOrderWithRootAndLeftNode(self):
        tree = AVLTree()
        tree.insert(4)
        tree.insert(3)
        nodes = tree.preorder_traversal()
        self.assertEqual(nodes, [4, 3])

    # 4
    #  \
    #   5
    def test_insertPreOrderWithRootAndRightNode(self):
        tree = AVLTree()
        tree.insert(4)
        tree.insert(5)
        nodes = tree.preorder_traversal()
        self.assertEqual(nodes, [4, 5])

    #   4
    #  / \
    # 3   5
    def test_insertPreOrderWithRootAndLeftRightNodes(self):
        tree = AVLTree()
        tree.insert(4)
        tree.insert(3)
        tree.insert(5)
        nodes = tree.preorder_traversal()
        self.assertEqual(nodes, [4, 3, 5])

    #     4
    #    / \
    #   3   5
    #  / \
    # 1   2
    def test_insertPreOrderWithRootAndLeftRightNodesWithLevel1Children(self):
        tree = AVLTree()
        tree.insert(4)
        tree.insert(3)
        tree.insert(1)
        tree.insert(2)
        tree.insert(5)
        nodes = tree.preorder_traversal()
        self.assertEqual(nodes, [4, 3, 1, 2, 5])

if __name__ == '__main__':
    unittest.main()
class AVLTree(object):
    def __init__(self):
        self.root = None

    def preorder_traversal(self):
        traversal = []
        if self.root is None:
            print('no nodes in tree')
            return traversal
        nodes = [self.root]
        while nodes:
            node = nodes.pop()
            traversal.append(node.value)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

        return traversal

    def check_balance(self):
        pass

    def insert_node(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self.insert_node(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self.insert_node(current_node.right, value)
        self.check_balance()

    def insert(self, value):
        # type check value
        if self.root is None:
            self.root = TreeNode(value)
        else:
            if type(self.root.value) != type(value):
                raise ValueError('value being added is the wrong type')
            self.insert_node(self.root, value)

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def left_rotation(self, node):
        if node and node.right:
            right_node = node.right
            node.right = right_node.left
            right_node.left = node

    def right_rotation(self, node):
        if node and node.left:
            left_node = node.left
            node.left = left_node.right
            left_node.right = node



class AVLTree(object):
    def __init__(self):
        self.root = None

    def preorder_traversal(self):
        traversal = []
        if self.root is None:
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

    def right_and_left_rotation(self, current):
        self.right_rotation(current) # check this
        self.left_rotation(current)

    def left_and_right_rotation(self, current):
        self.left_rotation(current)
        self.right_rotation(current) # check this 

    def get_height(self, current):
        if current is None:
            return 0
        
        left_height = 0
        right_height = 0

        if current.left:
            left_height = self.get_height(current.left)
        if current.right:
            right_height = self.get_height(current.right)
        return max(left_height, right_height) + 1

    # If the tree height differs by at least one, then rotate
    def check_balance(self, current):

        # if current.left is None and current.right is None:
        #     current.height = -1
        # else:
        #     left_height = get_height(current.left)
        #     right_height = get_height(current.right)
        #     current.height = max(left_height, right_height) + 1

        if self.get_height(current.left) - self.get_height(current.right) > 1:
            if self.get_height(current.left.left) - self.get_height(current.left.right) > 0:
                self.right_rotation(current)
            else:
                self.left_and_right_rotation(current)
        elif self.get_height(current.left) - self.get_height(current.right) < -1:
            if self.get_height(current.right.left) - self.get_height(current.right.right) > 0:
                self.left_rotation(current)
            else:
                self.right_and_left_rotation(current)

    def insert_node(self, current, value):
        if value < current.value:
            if current.left is None:
                # print('adding to {} to left child of {}'.format(value, current.value) )
                current.left = TreeNode(value)
            else:
                self.insert_node(current.left, value)
        else:
            if current.right is None:
                current.right = TreeNode(value)
                # print('adding to {} to right child of {}'.format(value, current.value) )
            else:
                self.insert_node(current.right, value)
        #self.check_balance(current)

    def insert(self, value):
        # type check value
        if self.root is None:
            # print('adding root: ', value)
            self.root = TreeNode(value)
        else:
            if type(self.root.value) != type(value):
                raise TypeError('value being added is the wrong type')
            self.insert_node(self.root, value)

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

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

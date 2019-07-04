class Node(object):
    # structure of a node
    # optional parameter
    nodes = []
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    def insert_recursive(self, number):
        """
        [x] check if root is empty
            - [x] if empty assign number to root
        if num < root:
            - [x] go to left side
            - check if left is empty; if empty
                - [x] initialize a new node here and set it's value to number
            - [x] else(left node has a value) recurse the function.
        if num > root:
            - [x] go to right
            - check if right is empty; if empty
                - [x] initialize a new node here and set it's value to number
            - [x] else(right node has a value) recurse the function.
        complexity: O(log(n))
        """
        # check if a root is empty
        if not self:
            # set value to root
            root = Node(number)
            return
        else:
            if number < self.data:
                # to the left
                if self.left is None:
                    self.left = Node(number)
                else:
                    self.left.insert_recursive(number)
            elif number > self.data:
                # to the right
                if self.right is None:
                    self.right = Node(number)
                else:
                    self.right.insert_recursive(number)

    def insert_iterative(self, number):
        if not self:
            self.data = number
            return self
        else:
            while(self):
                if number > self.data:
                    if self.right:
                        self = self.right
                    else:
                        self.right = Node(number)
                        break
                if number < self.data:
                    if self.left:
                        self = self.left
                    else:
                        self.left = Node(number)
                        break

    def bfs(self):
        if not self:
            return None
        queue = []
        data = []
        queue.append(self)
        while(queue):
            num = queue.pop()
            data.append(num.data)
            if num.left:
                queue.append(num.left)
            if num.right:
                queue.append(num.right)
        print(queue, data)


def validate_bst(root):
    return validate_bst_helper(root, float("-inf"), float("inf"))

def validate_bst_helper(root, min_val, max_val):
    if not root:
        return True
    if min_val < root.data and max_val > root.data:
        return validate_bst_helper(root.left, min_val, root.data) and validate_bst_helper(root.right, root.data, max_val)
    return False


node = Node(4)
# insert(node, 4)
"""
node.insert_recursive(5)
node.insert_recursive(3)
node.insert_recursive(2)
node.insert_recursive(1)
print(node.left.left.data)
"""

"""
node.insert_iterative(5)
node.insert_iterative(3)
node.insert_iterative(2)
node.insert_iterative(1)
print(node.left.left.data)
"""

"""
TEST BFS traversal
node.insert_iterative(0)
node.insert_iterative(2)
node.insert_iterative(3)
node.insert_iterative(1)
node.bfs()
"""

"""
VALIDATE BST
node.insert_iterative(0)
node.insert_iterative(2)
node.insert_iterative(3)
node.insert_iterative(1)
print(validate_bst(node))

node2 = Node(7)
node2.left = Node(8)
print(validate_bst(node2))
"""

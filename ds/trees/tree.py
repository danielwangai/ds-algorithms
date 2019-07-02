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

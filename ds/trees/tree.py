class Tree(object):
    # structure of a node
    # optional parameter
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, number):
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

        """
        # check if a root is empty
        if self.data == None:
            # set value to root
            self.data = number
            # return
        if number <= self.data:
            # to the left
            if self.left is None:
                self.left = Tree(number)
            else:
                self.left.insert(number)
        elif number >= self.data:
            # to the right
            if self.right is None:
                self.right = Tree(number)
            else:
                self.right.insert(number)
        print(">>>> ", self.data)

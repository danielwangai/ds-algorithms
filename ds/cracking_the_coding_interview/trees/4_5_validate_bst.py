from node import Node

"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""

def is_bst(node):
    if not node:
        # base case
        return None
    if node.left:
        if node.data < node.left.data:
            return False
        # recursive case
        return is_bst(node.left)
    if node.right:
        if node.data > node.right.data:
            return False
        # recursive case
        return is_bst(node.right)
    return True

x = Node(5)
x.left = Node(4)
print(is_bst(x))

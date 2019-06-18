from node import Node

"""
Problem: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height. 
"""

def minimal_tree(sorted_array):
    if not sorted_array:
        return None
    # get index of middle element i.e. index of the root
    mid = int(len(sorted_array)/2)
    root = Node(sorted_array[mid])
    root.right = minimal_tree(sorted_array[mid + 1:])
    root.left = minimal_tree(sorted_array[:mid])
    return root

def pre_order_traversal(node):
    if not node:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

x = [1, 2,3,4,5]
res = minimal_tree(x)
pre_order_traversal(res)

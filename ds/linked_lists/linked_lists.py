class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_to_sorted_insert(head, data):
    """
    codewars kata: https://www.codewars.com/kata/linked-lists-sorted-insert/train/python
    """
    if head is None:
        return head
    if head.next is None:
        head.next = Node(data)
        return head
    current = head
    # prev = Node(None)
    while(current.next is not None and current.data < data):
        prev = current
        current = current.next
    node = Node(data)
    node.next = current.next
    print(node.data)
    current.next = node

one = Node(1)
one.next = Node(2)

insert_to_sorted_insert(one, 3)
print(one.next.next.next)

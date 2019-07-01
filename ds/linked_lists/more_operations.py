from  basic_operations import Node, LinkedList


class LinkedList2(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_duplicates_sorted_iterative(self):
        """
        removes all duplicates from a sorted linked list
        complexity: O(n)
        """
        temp = self.head
        if not temp:
            return None
        while(temp.next):
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = new
                continue
            else:
                temp = temp.next
        return temp

    def reverse_in_place_iterative(self):
        """
        reverse a linked list in place(without creating another linked list);
        i.e. {1 -> 2 -> 3 -> 4} becomes {4 -> 3 -> 2 -> 1}
        complexity: O(n)
        """
        if not self.head:
            return None
        node = self.head
        self.head = self.tail
        # self.tail = node
        prev = None
        next = None
        while(node is not None):
            next = node.next
            node.next = prev
            prev = node
            node = next
            print(">> ", prev.data)
        return node

    def reverse_in_place_recursively(self):
        if not self.head:
            return None
        # pointer trackers
        node = self.head
        node.head = self.tail
        node.tail = node
        # stores the previous node
        prev = None
        # stores the next node
        next = None
        # base case
        if not node.head:
            return node
        # recursive case
        next = node.next
        # current node points to the previous one - None in the case of the first node
        node.next = prev
        # "increment previous node" - previous node points to the
        prev = node
        # "increment node" current node points to the next one
        node = next
        return reverse_in_place_recursively(node)

def is_identical_iterative(l1, l2):
    """
    compares if linked lists l1 and l2 are identical:
    linked lists are identical if they botth have the same amount
    of nodes and each node has the same value in the smae order.
    complexity: O(n)
    """
    if not l1 or not l2:
        return False
    l1 = l1.head
    l2 = l2.head
    while(l1 != None and l2 != None):
        if l1.data == l2.data:
            l1 = l1.next
            l2 = l2.next
            continue
        return False
    return (l1 == None and l2 == None)

def is_identical_recursive(l1, l2):
    """
    compares if linked lists l1 and l2 are identical:
    linked lists are identical if they botth have the same amount
    of nodes and each node has the same value in the smae order.
    complexity: O(n)
    """
    if not l1 and not l2:
        return True
    # if both are not none, then both MUST have the same data
    if l1 != None and l2 != None:
        if l1.data == l2.data:
            return is_identical_recursive(l1.next, l2.next)
    return False

x = Node(4)
ll = LinkedList2()
ll.head = x
ll.insert_head(4)
ll.insert_head(5)
ll.insert_head(6)
ll.insert_head(7)


print(">>>>>\n\n\n")
# ll.reverse_in_place_recursively()
# ll.reverse_in_place_iterative()
# print(ll.traverse())

"""
UNCOMMENT TO RUN
y = Node(4)
ll2 = LinkedList2()
ll2.head = y
ll2.insert_head(4)
ll2.insert_head(5)
ll2.insert_head(6)
ll2.insert_head(7)
ll2.insert_head(7)
print(is_identical_iterative(ll.head, ll2.head))
print(is_identical_recursive(ll.head, ll2.head))
"""

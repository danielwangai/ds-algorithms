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
        self.tail = node
        prev = None
        next = None
        while(node is not None):
            next = node.next
            node.next = prev
            prev = node
            node = next
            print(">> ", prev.data)
        return node

    def traverse(self):
        """
        go through each node once
        complexity: O(n)
        """
        if not self.head:
            return None
        nodes = []
        while(self.head):
            nodes.append(self.head.data)
            self.head = self.head.next
        return nodes

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

x = Node(4)
ll = LinkedList2()
ll.head = x
ll.insert_head(4)
ll.insert_head(5)
ll.insert_head(6)
ll.insert_head(7)

print(">>>>>\n\n\n")
ll.reverse_in_place_recursively()
print(ll.traverse())

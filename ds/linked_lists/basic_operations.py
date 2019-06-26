class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        """
        complexity: O(1)
        """
        if not self.head:
            self.head = Node(data)
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    
    def insert_tail(self, data):
        """
        complexity: O(n)
        Best case: o(1) if head = tail
        """
        if not self.head:
            self.head = Node(data)
        node = self.head
        while(node):
            if not node.next:
                node.next = Node(data)
                break
            node = node.next

    def insert_after(self, value, data):
        """
        value: element in the linked list where we insert data after
        data: value to be inserted
        complexity: O(n)
        """
        temp = self.head
        while(temp):
            if temp.data != value:
                temp = temp.next
                continue
            new_node = Node(data)
            if temp.next:
                next_val = temp.next
                temp.next = new_node
                new_node.next = next_val
                break
            temp.next = new_node
            break

node = Node(3)
node2 = Node(4)
node.next = node2
l = LinkedList()
l.head = node
# insert 6 at tail
l.insert_tail(6)
print(l.head.next.next.next.data)

# insert 5 after node 4
l.insert_after(4, 5)
print(l.head.next.next.next.data)

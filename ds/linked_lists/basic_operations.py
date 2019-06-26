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

    def delete_node(self, data):
        """
        complexity: O(n)
        best case: O(1) - deleting the head
        worst case when deleting the last node
        """
        if not self.head:
            return None
        temp = self.head
        prev = None
        while(temp):
            if temp.data != data:
                prev = temp
                temp = temp.next
                continue
            # if node to be deleted is the last one
            if not temp.next:
                prev.next = None
                break
            prev.next = temp.next
            return

    def delete_nth_node(self, n):
        """
        n: is the position of the node in the linked list
        n is an indexed value i.e. begins from 0 to {(total number of nodes) - 1}
        complexity: O(n)
        best case: O(1) - where n = 0
        worst case: deleting the last node
        """
        if not self.head:
            # linked list is empty
            return node
        # base case
        # delete first node
        if n == 0:
            # if there are more nodes
            if self.head.next:
                self.head = self.head.next
                return
            # if the node to be deleted is the only one
            self.head = None
            return
        temp = self.head.next
        prev = self.head
        count = 1
        while(temp):
            if n == count:
                # delete
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
            count = count + 1
            continue

    def delete_all_nodes_iterative(self):
        """
        complexity: O(n)
        best case: O(1) when the linked list has only one node
        """
        if not self.head:
            return None
        while(self.head):
            if self.head.next:
                # delete the head
                self.head = self.head.next
                continue
            self.head = None

    def delete_all_nodes_recursive(self):
        if not self.head:
            return None
        self.head = self.head.next
        return self.delete_all_nodes_recursive()

    def get_size_iteratively(self):
        if not self.head:
            return 0
        count = 0
        while(self.head):
            if not self.head.next:
                return count
            self.head = self.head.next
            count += 1
            continue
        return count

    def get_size_recursively(self):
        if not self.head:
            return 0
        self.head = self.head.next
        count = 1 + self.get_size_recursively()
        return count

    def search_iteratively(self, data):
        """
        complexity: O(n)
        best case: O(1) if node being searched for is the the head
        worst case: when finding the last node on the linked list
        """
        if not self.head:
            return None
        while(self.head != None):
            if self.head.data == data:
                return True
            self.head = self.head.next
        return False


    def search_recursively(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            return True
        self.head = self.head.next
        return self.search_recursively(data)

node = Node(3)
node2 = Node(4)
node.next = node2
l = LinkedList()
l.head = node
# insert 6 at tail
# l.insert_tail(6)
# print(l.head.next.next.data)

# l.insert_tail(7)
# print("last ", l.head.next.next.next.data)

# # insert 5 after node 4
# l.insert_after(4, 5)
# print(l.head.next.next.next.data)

# before deleting 4
# print(l.head.next.data)
# # delete node 4
# l.delete_node(7)
# print(l.head.next.data)

# before deleting n = 2
# print("before delete nth: ", l.head.next.next.data)
# # delete the 3rd node; n = 2
# l.delete_nth_node(2)
# print("after delete nth: ", l.head.next.next.data)

# print("Before delete all iterative: ", l.head.data)
# l.delete_all_nodes_iterative()
# print("After delete all iterative: ", l.head)

# print("Before delete all recursive: ", l.head.data)
# l.delete_all_nodes_recursive()
# print("After delete all recursive: ", l.head)
l.insert_tail(8)
l.insert_tail(9)
print("Size iteratively: ", l.get_size_iteratively())
print("Size recursively>>: ", l.get_size_recursively())

print("search iteratively: ", l.search_iteratively(9))
print("search recursively: ", l.search_recursively(4))

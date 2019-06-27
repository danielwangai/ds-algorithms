from  basic_operations import Node, LinkedList


class LinkedList2(LinkedList):
    def __init__(self):
        self.head = None

    def remove_duplicates_sorted(self):
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

x = Node(4)
ll = LinkedList2()
ll.head = x
ll.insert_head(4)
ll.insert_head(5)

ll.remove_duplicates_sorted()
print(ll.head.next.data)

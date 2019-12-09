package linked_list

// source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// Time Complexity: O(n) where n is the number of nodes in the linked list
	// this is because the fast pointer will go through all the nodes once till it reaches the end
	// space complexity: O(1) since we used constant extra space
	fast := head
	slow := head
	var prev *ListNode
	// move the fast pointer just before the node to be deleted
	for n > 0 {
		fast = fast.Next
		n--
		// an edge case if it so happens that n is a value larger than the number of nodes in the linked list
		// e.g. 1->2->3->4 and we have to delete the n = 5
		// end the loop and return nil
		if fast == nil {
			return nil
		}
	}
	// as long as the fast pointer is not nil(hasn't reached the end/tail of the linked list)
	// move both fast and slow pointers updating the prev pointer
	// when fast becomes nil, it has traversed all the nodes of the linked list and the slow pointer
	// is the node to be deleted
	for fast != nil {
		fast = fast.Next
		prev = slow
		slow = slow.Next
	}
	// this case occurs only when the linked list has only one node which is the node to be deleted
	if prev == nil {
		return slow.Next
	}
	next := slow.Next
	prev.Next = next
	return head
}

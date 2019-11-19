package linked_list

// source: https://leetcode.com/problems/linked-list-cycle-ii/

func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	// return hashTable(head)
	intersection := twoPointerTechnique(head)
	if intersection == nil {
		return nil
	}
	for intersection != head {
		intersection = intersection.Next
		head = head.Next
	}
	return head
}

func hashTable(head *ListNode) *ListNode {
	// Time complexity: O(n)
	// Space complexity: O(n) - the extra space used by the hash table/cache
	cache := map[*ListNode]bool{}
	curr := head
	for curr != nil {
		if _, ok := cache[curr]; ok {
			return curr
		}
		cache[curr] = true
		curr = curr.Next
	}
	return nil
}

func twoPointerTechnique(head *ListNode) *ListNode {
	// Time Complexity: O(n)
	// Space Complexity: O(1) - no extra space used
	fast := head
	slow := head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next
		if fast == slow {
			return slow
		}
	}
	return nil
}

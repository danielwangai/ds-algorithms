package tree

// source - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	// return lcaRecursive(root, p, q)
	return lcaIterative(root, p, q)
}

func lcaRecursive(root, p, q *TreeNode) *TreeNode {
	// Time Complexity - O(n) where n is the number of nodes in the BST
	// - Worst case happens when we have to go through all the nodes of the BST
	// Space Complexity - O(n) because of the extra space used by the call stack during recursion
	if p.Val < root.Val && q.Val < root.Val {
		return lcaRecursive(root.Left, p, q)
	} else if p.Val > root.Val && q.Val > root.Val {
		return lcaRecursive(root.Right, p, q)
	}
	return root
}

func lcaIterative(root, p, q *TreeNode) *TreeNode {
	// Time Complexity: O(n) same case as the recursive alternative
	// Space Complexity - O(1) since we're not using extra space
	for root != nil {
		if p.Val < root.Val && q.Val < root.Val {
			root = root.Left
			continue
		} else if p.Val > root.Val && q.Val > root.Val {
			root = root.Right
			continue
		}
		return root
	}
	return &TreeNode{}
}

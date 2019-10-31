package tree

// source: https://leetcode.com/problems/symmetric-tree/

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return symmetricHelper(root.Left, root.Right)
}

func symmetricHelper(left, right *TreeNode) bool {
	if left == nil || right == nil {
		return left == right
	}
	if left.Val != right.Val {
		return false
	}
	return symmetricHelper(left.Left, right.Right) && symmetricHelper(left.Right, right.Left)
}

"""
SOURCE - https://leetcode.com/problems/merge-two-binary-trees/

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        t = {
            val: 1,
            left: {
                val: 3,
                left: {
                    val: 1,
                    left: {
                        val: 5,
                        left: None,
                        right: None
                    },
                    right: {

                    }
                },
                right: None,
            },
            right: {
                val: 2,
                left: None,
                right: None,
            }
        }        
        """
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        # save the sum to the node on the first tree
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        print(t1)
        return t1
        """
        Method 2 - WIP
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        stack = []
        stack.append([t1, t2])
        while stack:
            #while stack is not empty
            #empty stack
            stack = []
            # if not stack[0] or not stack[1]:
            #     continue
            stack[0].val = stack[1].val
            if not stack[0]:
                stack[0].left = stack[1].right
            else:
                stack.append([stack[0].left, stack[1].left])
            if not stack[0]:
                stack[0].right = stack[1].right
            else:
                stack.append([stack[0].right, stack[1].right])
        return t1
        """

t1 = TreeNode(3)
t1.left = TreeNode(1)
t1.right = TreeNode(2)

t2 = TreeNode(4)
t2.left = TreeNode(6)
t2.right = TreeNode(8)

x = Solution()
x.mergeTrees(t1, t2)

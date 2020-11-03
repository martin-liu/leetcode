import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def isValidBST(self, root: TreeNode) -> bool:
        """
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

---
BST don't allow duplication
Basic idea: inorder dfs should return sorted elements
        """

        if not root:
            return True

        pre = None
        def inorder(tree):
            nonlocal pre
            if tree:
                if not inorder(tree.left):
                    return False

                if not pre:
                    pre = tree
                elif tree.val <= pre.val:
                    return False
                pre = tree

                if not inorder(tree.right):
                    return False
            return True

        return inorder(root)

    def testBST(self):
        self.assertTrue(self.isValidBST(None))
        self.assertTrue(self.isValidBST(TreeNode.fromList([2,1,3])))
        self.assertFalse(self.isValidBST(TreeNode.fromList([5,1,4,None,None,3,6])))
        self.assertFalse(self.isValidBST(TreeNode.fromList([10,5,15,None,None,6,20])))

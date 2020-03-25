import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def isBalanced(self, root: TreeNode) -> bool:
        """
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
        """
        if not root:
            return True

        def getMaxHeight(tree):
            if not tree:
                return (True, 0)

            valid, lHeight = getMaxHeight(tree.left)
            if not valid:
                return (False, -1)
            valid, rHeight = getMaxHeight(tree.right)
            if not valid or abs(rHeight - lHeight) > 1:
                return (False, -1)
            return (True, max(lHeight+1, rHeight+1))

        valid, _ = getMaxHeight(root)
        return valid

    def testIsBalance(self):
        self.assertTrue(self.isBalanced(TreeNode.fromList([3,9,20,None,None,15,7])))
        self.assertFalse(self.isBalanced(TreeNode.fromList([1,2,2,3,3,None,None,4,4])))

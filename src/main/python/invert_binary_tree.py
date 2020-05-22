import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
        if not root or (not root.left and not root.right):
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def test(self):
        self.assertEqual([4,7,2,9,6,3,1], self.invertTree(TreeNode.fromList([4,2,7,1,3,6,9])).toList())

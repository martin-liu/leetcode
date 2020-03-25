import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def minDepth(self, root: TreeNode) -> int:
        """
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        elif not root.left:
            # not leaf node
            return self.minDepth(root.right)+1
        elif not root.right:
            # not leaf node
            return self.minDepth(root.left)+1

        return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)

    def testMinDepth(self):
        self.assertEqual(2, self.minDepth(TreeNode.fromList([3,9,20,None,None,15,7])))
        self.assertEqual(2, self.minDepth(TreeNode.fromList([1,2])))
        self.assertEqual(2, self.minDepth(TreeNode.fromList([1,2,3,4,5])))

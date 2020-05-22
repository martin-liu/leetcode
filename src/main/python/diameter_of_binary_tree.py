import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""
        diameter = 0
        def maxDepth(node):
            nonlocal diameter
            if not node:
                return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        maxDepth(root)
        return diameter

    def test(self):
        self.assertEqual(3, self.diameterOfBinaryTree(TreeNode.fromList([1,2,3,4,5])))

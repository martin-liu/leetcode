import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def maxPathSum(self, root: TreeNode) -> int:
        """
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
        cache = dict()
        def calc(node, canBreak):
            if not node:
                return 0
            elif not node.left and not node.right:
                return node.val

            if (node, canBreak) in cache:
                return cache[(node, canBreak)]

            val = node.val
            checks = [val]
            left = right = None
            if node.left:
                left = calc(node.left, False)
                checks.append(val + left)
                if canBreak:
                    checks.append(calc(node.left, True))
            if node.right:
                right = calc(node.right, False)
                checks.append(val + right)
                if canBreak:
                    checks.append(calc(node.right, True))
            if node.left and node.right and canBreak:
                checks.append(val + left + right)

            ret = max(checks)
            cache[(node, canBreak)] = ret
            return ret

        return calc(root, True)

    def testMaxPathSum(self):
        self.assertEqual(48, self.maxPathSum(TreeNode.fromList([5,4,8,11,None,13,4,7,2,None,None,None,1])))
        self.assertEqual(-3, self.maxPathSum(TreeNode.fromList([-3])))
        self.assertEqual(3, self.maxPathSum(TreeNode.fromList([1,-2,-3,1,3,-2,None,-1])))
        self.assertEqual(1, self.maxPathSum(TreeNode.fromList([1,-2,-3])))
        self.assertEqual(6, self.maxPathSum(TreeNode.fromList([1,2,3])))
        self.assertEqual(42, self.maxPathSum(TreeNode.fromList([-10,9,20,None,None,15,7])))

import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def pathSum(self, root: TreeNode, s: int) -> int:
        """
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

---
Basic Idea: when add a new node in subpath, check from right sum to left, so that all the subpath is checked
"""
        self.res = 0
        def dfs(node, path):
            if not node:
                return
            else:
                nextPath = path + [node.val]
                localSum = 0
                for v in reversed(nextPath):
                    localSum += v
                    if localSum == s:
                        self.res += 1

                dfs(node.left, nextPath)
                dfs(node.right, nextPath)

        dfs(root, [])
        return self.res

    def test(self):
        self.assertEqual(3, self.pathSum(TreeNode.fromList([10,5,-3,3,2,None,11,3,-2,None,1]), 8))

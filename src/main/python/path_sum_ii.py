import unittest
from typing import List
from .ds import TreeNode

class Solution(unittest.TestCase):
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        """
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
        res = []
        def dfs(node: TreeNode, path: List[int]):
            if not node:
                return
            elif not node.left and not node.right and sum(path) + node.val == s:
                res.append(path + [node.val])
            else:
                nextPath = path + [node.val]
                dfs(node.left, nextPath)
                dfs(node.right, nextPath)

        dfs(root, [])
        return res

    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        elif not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        nextSum = sum - root.val
        left = [[root.val] + path for path in self.pathSum2(root.left, nextSum)]
        right = [[root.val] + path for path in self.pathSum2(root.right, nextSum)]
        return left + right

    def testPathSum(self):
        self.assertEqual([[5,4,11,2], [5,8,4,5]], self.pathSum(TreeNode.fromList([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))

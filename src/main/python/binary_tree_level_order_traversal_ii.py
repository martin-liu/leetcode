import unittest
from typing import List
from .ds import TreeNode
from queue import Queue

class Solution(unittest.TestCase):
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""
        if not root:
            return []
        res = [[]]
        queue = Queue()
        queue.put((root, 1))
        currLevel = 1
        while not queue.empty():
            node, level = queue.get()
            if level != currLevel:
                currLevel = level
                res.append([])
            res[-1].append(node.val)

            if node.left:
                queue.put((node.left, level+1))
            if node.right:
                queue.put((node.right, level+1))

        return res[::-1]

    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def levelBottom(nodes):
            if not nodes:
                return []
            level = []
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            return levelBottom(level) + [[n.val for n in nodes]]

        return levelBottom([root])

    def testLevelOrderBottom(self):
        self.assertEqual(self.levelOrderBottom(TreeNode.fromList([3,9,20,None,None,15,7])), [[15,7], [9,20], [3]])
        self.assertEqual(self.levelOrderBottom2(TreeNode.fromList([3,9,20,None,None,15,7])), [[15,7], [9,20], [3]])

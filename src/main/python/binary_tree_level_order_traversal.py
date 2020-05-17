import unittest
from typing import List
from queue import Queue
from .ds import TreeNode

class Solution(unittest.TestCase):
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
        """
        if not root:
            return []
        q, l, res = Queue(), 1, [[]]
        q.put((root,1))
        while not q.empty():
            node, lvl = q.get()
            if l != lvl:
                l = lvl
                res.append([])
            res[-1].append(node.val)
            if node.left:
                q.put((node.left, lvl+1))
            if node.right:
                q.put((node.right, lvl+1))
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(node, lvl):
            if not node:
                return
            if len(res) <= lvl:
                res.append([])
            res[lvl].append(node.val)
            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)
        dfs(root, 0)
        return res

    def testlevelOrder(self):
        self.assertEqual(self.levelOrder(TreeNode.fromList([3,9,20,None,None,15,7])), [[3], [9,20], [15,7]])
        self.assertEqual(self.levelOrder2(TreeNode.fromList([3,9,20,None,None,15,7])), [[3], [9,20], [15,7]])

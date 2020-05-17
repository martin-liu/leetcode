import unittest
from typing import List
from queue import Queue
from .ds import TreeNode

class Solution(unittest.TestCase):
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
        """
        if not root:
            return []
        q = Queue()
        q.put((root, 0))
        res = []
        while not q.empty():
            node, lvl = q.get()
            if len(res) == lvl:
                res.append([])
            res[lvl].append(node.val)
            if node.left:
                q.put((node.left, lvl+1))
            if node.right:
                q.put((node.right, lvl+1))

        for i, l in enumerate(res):
            if i% 2 == 1:
                res[i] = res[i][::-1]
        return res

    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ret = []
        level = [root]

        reverse = False
        while level:
            vals = [t.val for t in level]
            ret.append(vals[::-1] if reverse else vals)
            newLevel = []
            for t in level:
                if t.left:
                    newLevel.append(t.left)
                if t.right:
                    newLevel.append(t.right)
            level = newLevel
            reverse = not reverse
        return ret

    def testZigZag(self):
        self.assertEqual(self.zigzagLevelOrder(TreeNode.fromList([3,9,20,None,None,15,7])), [[3], [20,9], [15,7]])
        self.assertEqual(self.zigzagLevelOrder2(TreeNode.fromList([3,9,20,None,None,15,7])), [[3], [20,9], [15,7]])

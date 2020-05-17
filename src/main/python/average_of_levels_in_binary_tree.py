import unittest
from typing import List
from .ds import TreeNode
from queue import Queue

class Solution(unittest.TestCase):
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:

The range of node's value is in the range of 32-bit signed integer.
"""
        if not root:
            return []

        res, layer, queue, currLvl = [], [], Queue(), 1
        queue.put((root, 1))
        while not queue.empty():
            node, lvl = queue.get()
            if lvl != currLvl:
                currLvl = lvl
                res.append(sum(layer) / len(layer))
                layer = []
            layer.append(node.val)

            if node.left:
                queue.put((node.left, lvl+1))
            if node.right:
                queue.put((node.right, lvl+1))

        if layer:
            res.append(sum(layer) / len(layer))

        return res

    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        m = {}
        def dfs(node, lvl):
            if not node:
                return
            if lvl not in m:
                m[lvl] = []
            m[lvl].append(node.val)

            dfs(node.left, lvl+1)
            dfs(node.right, lvl+1)

        dfs(root, 1)
        return [sum(lvl)/len(lvl) for lvl in m.values()]

    def testAvg(self):
        self.assertEqual([3,14.5,11], self.averageOfLevels(TreeNode.fromList([3,9,20,None,None,15,7])))
        self.assertEqual([3,14.5,11], self.averageOfLevels2(TreeNode.fromList([3,9,20,None,None,15,7])))

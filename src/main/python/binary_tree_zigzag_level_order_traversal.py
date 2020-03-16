import unittest
from typing import List
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

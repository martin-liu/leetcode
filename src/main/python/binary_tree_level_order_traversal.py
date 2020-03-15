import unittest
from typing import List
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
        ret = []
        level = [root]
        while level:
            ret.append([t.val for t in level])
            newLevel = []
            for t in level:
                if t.left:
                    newLevel.append(t.left)
                if t.right:
                    newLevel.append(t.right)

            level = newLevel
        return ret


    def testlevelOrder(self):
        self.assertEqual(self.levelOrder(TreeNode.fromList([3,9,20,None,None,15,7])), [[3], [9,20], [15,7]])

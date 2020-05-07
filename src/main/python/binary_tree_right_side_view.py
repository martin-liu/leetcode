import unittest
from typing import List
from .ds import TreeNode
from queue import Queue

class Solution(unittest.TestCase):
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

---
Basic Idea: BFS with level, each level keep last node
"""
        if not root:
            return []

        queue = Queue()
        queue.put((root, 1))

        ret = []
        preNode, preLevel = root, 1
        while not queue.empty():
            node, level = queue.get()
            if level == preLevel + 1:
                ret.append(preNode.val)
            if node.left:
                queue.put((node.left, level+1))
            if node.right:
                queue.put((node.right, level+1))

            preNode, preLevel = node, level

        ret.append(preNode.val)
        return ret

    def testRightView(self):
        self.assertEqual([1,3,4], self.rightSideView(TreeNode.fromList([1,2,3,None,5,None,4])))

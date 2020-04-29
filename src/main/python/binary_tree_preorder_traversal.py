import unittest
from typing import List
from .ds import TreeNode

class Solution(unittest.TestCase):
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
        ret = []
        stack = [(root, 1)]
        while stack:
            node, location = stack.pop()
            if location == 1:
                if node:
                    ret.append(node.val)
                    stack.append((node, 2))
                    stack.append((node.left, 1))
            elif location == 2:
                stack.append((node, 3))
                stack.append((node.right, 1))

        return ret

    def testPreOrder(self):
        self.assertEqual([1,2,3], self.preorderTraversal(TreeNode.fromList([1,None,2,3])))

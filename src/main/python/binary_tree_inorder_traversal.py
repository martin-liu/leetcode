import unittest
from typing import List
from .ds import TreeNode

class Solution(unittest.TestCase):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
        """
        def inorder(tree):
            stack = [(tree, 1)]
            while stack:
                tree, location = stack.pop()
                if location == 1:
                    if tree:
                        stack.append((tree, 2))
                        stack.append((tree.left, 1))
                elif location == 2:
                    yield tree.val
                    stack.append((tree, 3))
                    stack.append((tree.right, 1))

        return list(inorder(root))

    def testInorderTraversal(self):
        tree = TreeNode(1)
        tree.right = TreeNode(2)
        tree.right.left = TreeNode(3)
        self.assertEqual(self.inorderTraversal(tree), [1,3,2])

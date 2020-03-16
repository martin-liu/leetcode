import unittest
from typing import List
from .ds import TreeNode

class Solution(unittest.TestCase):
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
        """
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        inMap = {n:i for i, n in enumerate(inorder)}
        def build(postL, postR, inR):
            if postL > postR:
                return None
            head = TreeNode(postorder[postR])
            if postL < postR:
                inIndex = inMap[head.val]
                rightLength = inR - inIndex
                head.left = build(postL, postR-rightLength-1, inIndex-1)
                head.right = build(postR-rightLength, postR-1, inR)
            return head

        return build(0, len(postorder)-1, len(inorder)-1)


    def testBuild(self):
        self.assertEqual(self.buildTree([9,3,15,20,7], [9,15,7,20,3]).toList(), [3,9,20,None,None,15,7])

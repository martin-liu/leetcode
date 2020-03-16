import unittest
from typing import List
from .ds import TreeNode

class Solution(unittest.TestCase):
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
----
Basic idea: `pre[0]` is root, `inorder.indexOf(pre[0])` is the index that split left and right sub tree for both pre/in. (pre/in have same length and same point that separate left/right, only order difference)
Need to calculate start & end point.
"""
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        inorderMap = {n:i for i, n in enumerate(inorder)}

        # inStart is needed to determine sub tree length
        def build(preStart, preEnd, inStart):
            if preStart > preEnd:
                return None
            head = TreeNode(preorder[preStart])
            if preStart < preEnd:
                inorderIndex = inorderMap[head.val]
                # need to get sub tree length
                leftTreeLen = inorderIndex - inStart
                head.left = build(preStart+1, preStart+leftTreeLen, inStart)
                head.right = build(preStart+leftTreeLen+1, preEnd, inStart+leftTreeLen+1)
            return head

        return build(0, len(preorder)-1, 0)

    def testConstruct(self):
        self.assertEqual(self.buildTree([1,2,3], [3,2,1]).toList(), [1,2,None,3])
        self.assertEqual(self.buildTree([3,9,20,15,7], [9,3,15,20,7]).toList(), [3,9,20,None,None,15,7])

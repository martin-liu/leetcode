import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Inpug:
Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
     3
    / \
   4   5
  / \   \
 5   4   7
"""
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            node = TreeNode(t1.val+t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node

    def test(self):
        self.assertEqual([3,4,5,5,4,None,7], self.mergeTrees(TreeNode.fromList([1,3,2,5]), TreeNode.fromList([2,1,3,None,4,None,7])).toList())

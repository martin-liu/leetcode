import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.


Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""
        def match(s, t):
            if s == t:
                return True
            if not t or not s:
                return False
            return s.val == t.val and match(s.left, t.left) and match(s.right, t.right)

        return match(s, t) or (s.left and self.isSubtree(s.left, t)) or (s.right and self.isSubtree(s.right, t))

    def test(self):
        self.assertTrue(self.isSubtree(TreeNode.fromList([1,1]), TreeNode.fromList([1])))
        self.assertTrue(self.isSubtree(TreeNode.fromList([3,4,5,1,2]), TreeNode.fromList([4,1,2])))
        self.assertFalse(self.isSubtree(TreeNode.fromList([3,4,5,1,2,None,None,0]), TreeNode.fromList([4,1,2])))
        self.assertFalse(self.isSubtree(TreeNode.fromList([3,4,5,1,None,2]), TreeNode.fromList([3,1,2])))

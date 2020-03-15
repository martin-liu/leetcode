import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def isSymmetric(self, root: TreeNode) -> bool:
        """
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

        """
        if not root:
            return True

        def isSym(p, q):
            if not p:
                return not q
            elif not q:
                return False
            return p.val == q.val and isSym(p.left, q.right) and isSym(p.right, q.left)

        return isSym(root.left, root.right)

    def testIsSymmetric(self):
        self.assertTrue(self.isSymmetric(TreeNode.fromList([1,2,2,3,4,4,3])))
        self.assertFalse(self.isSymmetric(TreeNode.fromList([1,2,2,None,3,None,3])))

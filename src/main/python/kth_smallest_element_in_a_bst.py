import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


"""
        self.found = False
        self.k = k
        self.res = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.found:
                return
            self.k -= 1
            if self.k == 0:
                self.found = True
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.res

    def test(self):
        self.assertEqual(1, self.kthSmallest(TreeNode.fromList([3,1,4,None,2]), 1))
        self.assertEqual(3, self.kthSmallest(TreeNode.fromList([5,3,6,2,4,None,None,1]), 3))

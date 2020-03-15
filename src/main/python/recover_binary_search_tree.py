import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def recoverTree(self, root: TreeNode) -> None:
        """
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?

"""
        pre = first = second = None
        def inorder(tree):
            nonlocal pre, first, second
            if tree:
                inorder(tree.left)
                if pre and tree.val < pre.val:
                    if not first:
                        first = pre
                    second = tree
                pre = tree
                inorder(tree.right)

        inorder(root)
        if first and second:
            first.val, second.val = second.val, first.val

    def testRecover(self):
        t = TreeNode(1)
        t.left = TreeNode(3)
        t.left.right = TreeNode(2)
        self.recoverTree(t)
        self.assertEqual(t.toList(), [3,1,None,None,2])

        t = TreeNode(3)
        t.left = TreeNode(1)
        t.right = TreeNode(4)
        t.right.left = TreeNode(2)
        self.recoverTree(t)
        self.assertEqual(t.toList(), [2,1,4,None,None,3])

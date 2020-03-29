import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def flatten(self, root: TreeNode) -> None:
        """
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
        """
        if not root:
            return
        if not root.left:
            self.flatten(root.right)
            return
        if not root.right:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            return

        self.flatten(root.left)
        self.flatten(root.right)
        right = root.right
        root.right = root.left
        root.left = None
        curr = root.right
        while curr.right:
            curr = curr.right
        curr.right = right

    def testFlatten(self):
        tree = TreeNode.fromList([1,2,5,3,4,None,6])
        self.flatten(tree)
        self.assertEqual([1,None,2,None,3,None,4,None,5,None,6], tree.toList())

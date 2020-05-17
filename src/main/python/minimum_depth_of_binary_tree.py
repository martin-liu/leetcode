import unittest
from queue import Queue
from .ds import TreeNode

class Solution(unittest.TestCase):
    def minDepth(self, root: TreeNode) -> int:
        """
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
        if not root:
            return 0
        queue = Queue()
        queue.put((root,1))
        while not queue.empty():
            node, depth = queue.get()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.put((node.left, depth+1))
            if node.right:
                queue.put((node.right, depth+1))

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        elif not root.left:
            # not leaf node
            return self.minDepth2(root.right)+1
        elif not root.right:
            # not leaf node
            return self.minDepth2(root.left)+1

        return min(self.minDepth2(root.left)+1, self.minDepth2(root.right)+1)

    def testMinDepth(self):
        self.assertEqual(2, self.minDepth(TreeNode.fromList([3,9,20,None,None,15,7])))
        self.assertEqual(2, self.minDepth(TreeNode.fromList([1,2])))
        self.assertEqual(2, self.minDepth(TreeNode.fromList([1,2,3,4,5])))

import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

---
Basic Idea: Recursive function `lca` will return LCA or p or q.

        left, right = lca(node.left), lca(node.right)
        if both left and right is not null, means one return p one return q, so that `node` is LCA
        if one of left and right is null, means the other one is LCA, return it
"""
        # for real root, if it's p or q, means other one must be it's children, so that root is LCA
        # for non root node, if it's p or q, just return it, the following logic will check left/right
        if root in (None, p, q):
            return root
        # find LCA in left and right subtree
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        # if one left one right, then root is LCA. Otherwise, either left or right
        return root if left and right else left or right

    def test(self):
        root = TreeNode.fromList([3,5,1,6,2,0,8,None,None,7,4])
        self.assertEqual(root, self.lowestCommonAncestor(root, root.left, root.right))
        self.assertEqual(root.left, self.lowestCommonAncestor(root, root.left, root.left.right.right))

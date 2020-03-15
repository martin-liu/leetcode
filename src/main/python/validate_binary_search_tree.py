import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(unittest.TestCase):
        def isValidBST(self, root: TreeNode) -> bool:
            """
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

---
BST don't allow duplication
Basic idea: inorder dfs should return sorted elements
            """

            if not root:
                return True

            state = {'pre': None}
            def inorder(tree):
                if tree:
                    if not inorder(tree.left):
                        return False

                    if not state['pre']:
                        state['pre'] = tree
                    elif tree.val <= state['pre'].val:
                        return False
                    state['pre'] = tree

                    if not inorder(tree.right):
                        return False
                return True

            return inorder(root)

        def testBST(self):
            self.assertTrue(self.isValidBST(None))

            t = TreeNode(2)
            t.left = TreeNode(1)
            t.right = TreeNode(3)
            self.assertTrue(self.isValidBST(t))

            t = TreeNode(5)
            t.left = TreeNode(1)
            t.right = TreeNode(4)
            t.right.left = TreeNode(3)
            t.right.right = TreeNode(6)
            self.assertFalse(self.isValidBST(t))

            t = TreeNode(10)
            t.left = TreeNode(5)
            t.right = TreeNode(15)
            t.right.left = TreeNode(6)
            t.right.right = TreeNode(20)
            self.assertFalse(self.isValidBST(t))

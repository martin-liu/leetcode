import unittest
from .ds import TreeNode


class Solution(unittest.TestCase):
    def sumNumbers(self, root: TreeNode) -> int:
        """
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

"""
        ret = 0
        def dfs(tree, parentNum):
            nonlocal ret
            if not tree:
                return
            num = parentNum * 10 + tree.val
            if tree.left:
                dfs(tree.left, num)
            if tree.right:
                dfs(tree.right, num)
            if not tree.left and not tree.right:
                # leaf
                ret += num

        dfs(root, 0)
        return ret

    def testSumNumbers(self):
        self.assertEqual(25, self.sumNumbers(TreeNode.fromList([1,2,3])))
        self.assertEqual(1026, self.sumNumbers(TreeNode.fromList([4,9,0,5,1])))

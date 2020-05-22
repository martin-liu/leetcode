import unittest
from .ds import TreeNode

class Solution(unittest.TestCase):
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


)"""
        lvlMap = {}
        def dfs(node, lvl, index):
            if not node:
                return
            if lvl not in lvlMap:
                lvlMap[lvl] = []
            lvlMap[lvl].append(index)
            dfs(node.left, lvl+1, index*2-1)
            dfs(node.right, lvl+1, index*2)
        dfs(root, 1, 1)

        res = 0
        for v in lvlMap.values():
            width = v[-1] - v[0] + 1
            res = max(res, width)
        return res

    def test(self):
        self.assertEqual(4, self.widthOfBinaryTree(TreeNode.fromList([1,3,2,5,3,None,9])))
        self.assertEqual(2, self.widthOfBinaryTree(TreeNode.fromList([1,3,None,5,3])))
        self.assertEqual(8, self.widthOfBinaryTree(TreeNode.fromList([1,3,2,5,None,None,9,6,None,None,7])))

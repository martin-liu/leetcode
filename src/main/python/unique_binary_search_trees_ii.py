import unittest
from typing import List
from .ds import TreeNode

class Solution(unittest.TestCase):
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

---
tree = (n,left,right); left < n < right
To add a node which greater than any of other nodes in the tree, it should either (n, tree) or (tree.val, tree.left, (n, tree.right)) for each right node of tree.right

Basic idea: for each tree in f(n-1), create (n,tree), or go through right subtree of tree, insert n at each right node
        """
        if n < 1:
            return []

        trees = [None] * n
        for i in range(n):
            if i == 0:
                trees[i] = [TreeNode(1)]
            else:
                ts = []
                for tree in trees[i-1]:
                    t = TreeNode(i+1)
                    t.left = tree
                    ts.append(t)

                    curr = tree
                    while curr:
                        # build new tree from old tree, which every right node need to recreate (in case reference change)
                        newTree = TreeNode(tree.val)
                        oCurr, nCurr = tree, newTree
                        # copy until find curr
                        while oCurr != curr:
                            # share left tree
                            nCurr.left = oCurr.left
                            # right need to rebuild
                            nCurr.right = TreeNode(oCurr.right.val)
                            nCurr = nCurr.right
                            oCurr = oCurr.right

                        # insert node n
                        t = TreeNode(i+1)
                        nCurr.left = curr.left
                        nCurr.right = t
                        t.left = curr.right
                        ts.append(newTree)

                        curr = curr.right
                trees[i] = ts

        return trees[n-1]

    def testGenerateTrees(self):
        self.assertCountEqual(map(lambda t: t.toList(), self.generateTrees(3)), [[1,None,3,2], [3,2,None,1], [3,1,None,None,2], [2,1,3], [1,None,2,None,3]])

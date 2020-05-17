import unittest
from typing import List
from .ds import TreeNode
from queue import Queue

class Solution(unittest.TestCase):
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
        if K == 0:
            return [target.val]

        parentMap, visitMap, q = {}, {}, Queue()

        # build parent map
        q.put(root)
        while not q.empty():
            node = q.get()
            if node == target:
                break
            if node.left:
                parentMap[node.left] = node
                q.put(node.left)
            if node.right:
                parentMap[node.right] = node
                q.put(node.right)

        q.queue.clear()
        q.put((target, 0))
        res = []
        while not q.empty():
            node, dis = q.get()
            if dis == K:
                res.append(node.val)
            elif dis > K:
                return res

            if node.left and node.left not in visitMap:
                q.put((node.left, dis+1))
            if node.right and node.right not in visitMap:
                q.put((node.right, dis+1))
            if node in parentMap and parentMap[node] not in visitMap:
                q.put((parentMap[node], dis+1))

            visitMap[node] = True

        return res

    def test(self):
        root = TreeNode.fromList([3,5,1,6,2,0,8,None,None,7,4])
        self.assertEqual([5], self.distanceK(root, root.left, 0))
        self.assertEqual([7,4,1], self.distanceK(root, root.left, 2))

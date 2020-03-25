import unittest
from .ds import ListNode, TreeNode

class Solution(unittest.TestCase):
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
        if not head:
            return None
        curr = head
        i = 0
        m = {}
        while curr:
            m[i] = curr.val
            i += 1
            curr = curr.next

        def build(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(m[l])
            mid = (r + l + 1) // 2
            root = TreeNode(m[mid])
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root
        return build(0, i-1)

    def testSortedListToBST(self):
        self.assertEqual(self.sortedListToBST(ListNode.fromList([-10,-3,0,5,9])).toList(), [0,-3,9,-10,None,5])

import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def middleNode(self, head: ListNode) -> ListNode:
        """
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:

The number of nodes in the given list will be between 1 and 100.
"""
        if not head or not head.next:
            return head

        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        return p1

    def testMiddleNode(self):
        self.assertEqual(3, self.middleNode(ListNode.fromList([1,2,3,4,5])).val)
        self.assertEqual(4, self.middleNode(ListNode.fromList([1,2,3,4,5,6])).val)

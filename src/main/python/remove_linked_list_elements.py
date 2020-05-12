import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
        sentry = ListNode(0)
        sentry.next = head

        pre, curr = sentry, head
        while curr:
            if curr.val == val:
                pre.next, curr = curr.next, curr.next
            else:
                pre, curr = curr, curr.next

        return sentry.next

    def testRemove(self):
        self.assertEqual([1,2,3,4,5], self.removeElements(ListNode.fromList([1,2,6,3,4,5,6]), 6).toList())
        self.assertEqual([2,3,4,5], self.removeElements(ListNode.fromList([1,2,1,3,4,5,1]), 1).toList())

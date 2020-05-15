import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def swapPairs(self, head):
        """
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Basic idea: keep previous rounds tail node, and connect it with new swapped 2 nodes
        """

        if not head or not head.next:
            return head

        sentry = ListNode(None)
        sentry.next = head

        pre, curr = sentry, head
        while curr and curr.next:
            # pre = curr, because curr will move to curr.next, so that it's like pre = curr.next
            pre.next, curr.next.next, curr.next, pre, curr = \
                curr.next, curr, curr.next.next, curr, curr.next.next

        return sentry.next

    def test(self):
        self.assertEqual([3], self.swapPairs(ListNode.fromList([3])).toList())
        self.assertEqual([3,2], self.swapPairs(ListNode.fromList([2,3])).toList())
        self.assertEqual([3,2,8,7], self.swapPairs(ListNode.fromList([2,3,7,8])).toList())
        self.assertEqual([2,1,4,3], self.swapPairs(ListNode.fromList([1,2,3,4])).toList())
        self.assertEqual([2,1,4,3,5], self.swapPairs(ListNode.fromList([1,2,3,4,5])).toList())

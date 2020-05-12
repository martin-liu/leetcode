import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def sortList(self, head: ListNode) -> ListNode:
        """
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

---
Basic Idea: use merge sort
"""
        if not head or not head.next:
            return head

        pre, p1, p2 = None, head, head
        while p2 and p2.next:
            pre, p1, p2 = p1, p1.next, p2.next.next

        pre.next = None
        return self.merge(self.sortList(head), self.sortList(p1))

    def merge(self, l1, l2):
        curr = sentry = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, curr, l1 = l1, l1, l1.next
            else:
                curr.next, curr, l2 = l2, l2, l2.next
        curr.next = l1 or l2
        return sentry.next

    def testSort(self):
        self.assertEqual([1,2,3,4], self.sortList(ListNode.fromList([4,2,1,3])).toList())
        self.assertEqual([-1,0,3,4,5], self.sortList(ListNode.fromList([-1,5,3,4,0])).toList())

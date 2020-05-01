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

        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        if p1.next is None:
            # only 2 nodes
            p1 = head

        left, right = head, p1.next
        p1.next = None
        return self.merge(self.sortList(left), self.sortList(right))

    def merge(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            head = ListNode(-1)
            curr = head
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
            return head.next

    def testSort(self):
        self.assertEqual([1,2,3,4], self.sortList(ListNode.fromList([4,2,1,3])).toList())
        self.assertEqual([-1,0,3,4,5], self.sortList(ListNode.fromList([-1,5,3,4,0])).toList())

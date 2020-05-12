import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def reorderList(self, head: ListNode) -> None:
        """
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

---
Basic Idea (O(n) time, O(1) space): reverse second half of list, then use 2 pointer to swap
"""
        if not head or not head.next:
            return

        fast, slow = head, head

        # find mid node (slow)
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # reverse second half
        slow.next, curr = None, slow.next
        pre = None
        while curr:
            pre, curr.next, curr = curr, pre, curr.next

        # concat
        p1, p2 = head, pre
        while p1 and p2:
            p1.next, p1, p2.next, p2 = p2, p1.next, p1.next, p2.next

    def reorderList2(self, head: ListNode) -> None:
        if not head:
            return

        ls = []
        curr = head
        while curr:
            ls.append(curr.val)
            curr = curr.next

        l, r = 0, len(ls)-1
        curr = head
        leftTurn = True
        while l <= r:
            if leftTurn:
                curr.val = ls[l]
                l += 1
            else:
                curr.val = ls[r]
                r -= 1
            leftTurn = not leftTurn
            curr = curr.next

    def testReorder(self):
        head = ListNode.fromList([1,2,3,4])
        self.reorderList(head)
        self.assertEqual([1,4,2,3], head.toList())

        head = ListNode.fromList([1,2,3,4,5])
        self.reorderList(head)
        self.assertEqual([1,5,2,4,3], head.toList())

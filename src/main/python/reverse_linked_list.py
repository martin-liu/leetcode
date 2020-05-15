import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def reverseList(self, head: ListNode) -> ListNode:
        """
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

---
Basic Idea: 2 pointers (pre, curr), pre start as None, so that head.next will set to None
"""
        if not head or not head.next:
            return head
        pre, curr = None, head
        while curr:
            pre, curr.next, curr = curr, pre, curr.next
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        # recursively build another list
        def reverse(head, tail):
            if not head:
                return tail
            rest, head.next = head.next, tail
            return reverse(rest, head)
        return reverse(head, None)

    def testReverse(self):
        self.assertEqual([5,4,3,2,1], self.reverseList(ListNode.fromList([1,2,3,4,5])).toList())
        self.assertEqual([5,4,3,2,1], self.reverseList2(ListNode.fromList([1,2,3,4,5])).toList())

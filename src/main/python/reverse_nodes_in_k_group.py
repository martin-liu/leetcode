import unittest
from .ds import ListNode
class Solution(unittest.TestCase):
    def reverseKGroup(self, head, k):
        """
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

        """
        if not head or not head.next or k <= 1:
            return head
        sentry = ListNode(None)
        sentry.next = head

        L = 0
        while head:
            head = head.next
            L += 1

        times = L // k # how many times of reverse k nodes
        preEnd, pre, curr = sentry, sentry.next, sentry.next.next
        for _ in range(times):
            for _ in range(k-1):
                # do k-1 times `curr -> pre`
                curr.next, pre, curr = pre, curr, curr.next
            # connect reversed sublist to preEnd and prepare for next sublist
            preEnd.next.next, preEnd.next, preEnd, pre, curr = \
                curr, pre, preEnd.next, curr, curr and curr.next

        return sentry.next

    def test(self):
        self.assertEqual(self.reverseKGroup(ListNode.fromList([1,2,3,4,5]), 2).toList(), [2, 1, 4, 3, 5])
        self.assertEqual(self.reverseKGroup(ListNode.fromList([1,2,3,4,5]), 3).toList(), [3, 2, 1, 4, 5])
        self.assertEqual(self.reverseKGroup(ListNode.fromList([1,2,3,4,5]), 4).toList(), [4, 3, 2, 1, 5])
        self.assertEqual(self.reverseKGroup(ListNode.fromList([1,2,3,4,5]), 5).toList(), [5, 4, 3, 2, 1])

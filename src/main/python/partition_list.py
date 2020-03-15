import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

        You should preserve the original relative order of the nodes in each of the two partitions.

        Example:

        Input: head = 1->4->3->2->5->2, x = 3
        Output: 1->2->2->4->3->5
        """
        if not head:
            return head

        lhead, ltail, rhead, rtail = None, None, None, None
        curr = head
        while curr:
            if curr.val < x:
                if not lhead:
                    lhead = ltail = curr
                else:
                    ltail.next = curr
                    ltail = curr
            else:
                if not rhead:
                    rhead = rtail = curr
                else:
                    rtail.next = curr
                    rtail = curr
            curr = curr.next
            if ltail:
                ltail.next = None
            if rtail:
                rtail.next = None

        if lhead:
            ltail.next = rhead
            return lhead
        else:
            return rhead

    def testPartition(self):
        self.assertEqual(self.partition(ListNode.fromList([3,1]), 2).toList(), [1,3])
        self.assertEqual(self.partition(ListNode.fromList([3,2,5,2]), 3).toList(), [2,2,3,5])
        self.assertEqual(self.partition(ListNode.fromList([3,2,5,1]), 3).toList(), [2,1,3,5])
        self.assertEqual(self.partition(ListNode.fromList([1,4,3,2,5,2]), 3).toList(), [1,2,2,4,3,5])

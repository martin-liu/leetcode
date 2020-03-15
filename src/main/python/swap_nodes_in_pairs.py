from .ds import ListNode
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Basic idea: keep previous rounds tail node, and connect it with new swapped 2 nodes
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        point = head
        ret = preTail = ListNode(0)

        # point will be first node of every pair
        while point != None and point.next != None:
            # swap point and second node of current pair
            second = point.next
            point.next = second.next
            second.next = point

            # connect previous tail node with second node (now first node)
            preTail.next = second

            # point now is the second node, so set previous tail node as point
            preTail = point

            # point already swap to second one, so only need go to next node for next round
            point = point.next

        return ret.next

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        l1 = ListNode(2)
        l1.next = ListNode(3)
        l1.next.next = ListNode(7)
        l1.next.next.next = ListNode(8)

        ll = s.swapPairs(l1)
        arr = []
        while ll != None:
            arr.append(ll.val)
            ll = ll.next

        self.assertEqual(arr, [3, 2, 8, 7])

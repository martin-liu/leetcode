# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Basic idea: use an array to keep k nodes
class Solution:
    def nextNnode(self, l, n):
        while l != None and n > 0:
            l = l.next
            n -= 1
        return l

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or k <= 1:
            return head

        point = head
        ret = ListNode(0)
        ret.next = head
        preTail = ret

        while point != None:
            kNodes = []
            cur = point
            # fill kNodes with k nodes or None
            for i in range(k):
                kNodes.append(cur)
                if cur != None:
                    cur = cur.next

            # if last node is there, means has full k nodes
            if kNodes[-1] != None:
                # swap
                for i in range(1, k):
                    kNodes[i].next = kNodes[i - 1]
                # now last node is first, first node is last
                preTail.next = kNodes[-1]
                # set previous tail node
                preTail = kNodes[0]
                # break old connection to prevent cycle link
                preTail.next = None
                point = cur
            else:
                # if not full k nodes, will not swap, only connect previous tail node to first node
                preTail.next = point
                point = None

        return ret.next



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(4)
        l1.next.next.next.next = ListNode(5)

        def list2Arr(l):
            ar = []
            while l != None:
                ar.append(l.val)
                l = l.next
            return ar

        self.assertEqual(list2Arr(s.reverseKGroup(l1, 2)), [2, 1, 4, 3, 5])

        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(4)
        l1.next.next.next.next = ListNode(5)

        self.assertEqual(list2Arr(s.reverseKGroup(l1, 3)), [3, 2, 1, 4, 5])

        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(4)
        l1.next.next.next.next = ListNode(5)

        self.assertEqual(list2Arr(s.reverseKGroup(l1, 4)), [4, 3, 2, 1, 5])

        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(3)
        l1.next.next.next = ListNode(4)
        l1.next.next.next.next = ListNode(5)

        self.assertEqual(list2Arr(s.reverseKGroup(l1, 5)), [5, 4, 3, 2, 1])

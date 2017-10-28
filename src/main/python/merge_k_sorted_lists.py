# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Basic idea: based on mergeTwoLists, divide and conquer to merge one by one
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        cur = head

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 == None:
            cur.next = l2
        elif l2 == None:
            cur.next = l1

        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length == 0:
            return None

        # divide and conquer, one fast way (logK) to do merge
        # [1, 2, 3, 4, 5] => [(1, 2), _, (3, 4), _, 5] => [(1, 2, 3, 4), _, _, _, 5] => [(1, 2, 3, 4, 5), _, _, _, _]
        interval = 1
        while interval < length:
            for i in range(0, length - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        l1 = ListNode(2)
        l1.next = ListNode(3)
        l1.next.next = ListNode(7)

        l2 = ListNode(1)
        l2.next = ListNode(4)
        l2.next.next = ListNode(6)

        l3 = ListNode(5)
        l3.next = ListNode(8)
        l3.next.next = ListNode(9)

        ll = s.mergeKLists([l1, l2, l3])
        arr = []
        while (ll != None):
            arr.append(ll.val)
            ll = ll.next

        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

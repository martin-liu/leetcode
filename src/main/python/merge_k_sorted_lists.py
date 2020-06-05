import unittest
from heapq import heappush, heappop
from .ds import ListNode

class Solution(unittest.TestCase):
    def mergeKLists(self, lists):
        """
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Basic idea: k-way merge, min heap
        """
        if not lists:
            return None
        heap = []
        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))

        curr = head = ListNode(None)
        while heap:
            v, i, node = heappop(heap)
            curr.next, curr = node, node
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return head.next

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

    def mergeKLists2(self, lists):
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

    def test(self):
        l1 = ListNode.fromList([1,3,7])
        l2 = ListNode.fromList([1,4,6])
        l3 = ListNode.fromList([5,8,9])

        self.assertEqual([1, 1, 3, 4, 5, 6, 7, 8, 9], self.mergeKLists([l1,l2,l3]).toList())

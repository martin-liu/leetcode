from .ds import ListNode
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Basic idea: travel both and generate a new list
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




# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        l1 = ListNode(1)
        l1.next = ListNode(3)
        l2 = ListNode(2)
        l2.next = ListNode(5)

        l = s.mergeTwoLists(l1, l2)
        self.assertEqual(l.next.val, 2)
        self.assertEqual(l.next.next.val, 3)
        self.assertEqual(l.next.next.next.val, 5)

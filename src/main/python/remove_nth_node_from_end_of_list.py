from .ds import ListNode
# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Basic idea: use 2 variable to store start and end (distance n)
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head == None:
            return None
        if n <= 0:
            return head

        left = right = head
        for _ in range(n):
            right = right.next

        # since (given) n is always valid, `right == None` means remove first item
        if right == None:
            return head.next

        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return head

    # if n is not always valid, then we can use an array to store last `n + 1` items
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head == None:
            return None
        if n <= 0:
            return head

        # use an array to store `n + 1` items, so that we can change next for first item of this array
        arr = [None for i in range(n + 1)]

        cur = head
        # travel the whole chain, store last `n + 1` items
        while cur != None:
            arr = arr[1:] + [cur]
            cur = cur.next

        # if cannot fill the arr, means n >= size
        if arr[1] == None:
            # n > size
            return head
        elif arr[0] == None:
            # n == size, means remove first item
            if n == 1:
                return None
            else:
                return arr[2]

        if n == 1:
            # if remove last
            arr[0].next = None
        else:
            arr[0].next = arr[2]

        return head

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        self.assertEqual(s.removeNthFromEnd(l, 2).next.val, 3)

        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        self.assertEqual(s.removeNthFromEnd(l, 1).next.next, None)

        l = ListNode(1)
        l.next = ListNode(2)
        self.assertEqual(s.removeNthFromEnd(l, 2).val, 2)

        l = ListNode(1)
        self.assertEqual(s.removeNthFromEnd(l, 1), None)

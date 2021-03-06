from .ds import ListNode

# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Basic idea: Divide and conquer
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p1, p2, carry = l1, l2, 0
        curr = sentry = ListNode(0)
        # when any one exists, need to add new node
        while p1 or p2 or carry:
            add = 0
            if p1:
                add += p1.val
                p1 = p1.next
            if p2:
                add += p2.val
                p2 = p2.next
            carry, val = divmod(add + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return sentry.next

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.doAddTwoNumbers(l1, l2, 0)

    def doAddTwoNumbers(self, l1, l2, carry = 0):
        if l1 == None:
            if carry > 0:
                # if carry, then need to add carry
                return self.doAddTwoNumbers(ListNode(carry), l2)
            return l2
        if l2 == None:
            if carry > 0:
                # if carry, then need to add carry
                return self.doAddTwoNumbers(l1, ListNode(carry))
            return l1

        # get quotient and remainder
        (q, r) = divmod(l1.val + l2.val + carry, 10)
        ret = ListNode(r)
        ret.next = self.doAddTwoNumbers(l1.next, l2.next, q)

        return ret



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        ret = s.addTwoNumbers(l1, l2)
        self.assertEqual(ret.val, 7)
        self.assertEqual(ret.next.val, 0)
        self.assertEqual(ret.next.next.val, 8)

        self.assertEqual([0,1], s.addTwoNumbers(ListNode.fromList([5]), ListNode.fromList([5])).toList())

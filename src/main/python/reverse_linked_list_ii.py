import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def toList(self):
        curr = self
        ret = [curr.val]
        while curr.next:
            ret.append(curr.next.val)
            curr = curr.next
        return ret

    @staticmethod
    def fromList(l):
        curr = None
        head = None
        for v in l:
            if not curr:
                curr = ListNode(v)
                head = curr
            else:
                curr.next = ListNode(v)
                curr = curr.next
        return head

class Solution(unittest.TestCase):
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
        """
        if not head or m == n:
            return head

        # add one temp head node
        newHead = ListNode(-1)
        newHead.next = head
        head = newHead

        i = 0
        pre, curr = None, head
        start = None
        while curr:
            next = curr.next
            if i == m - 1:
                start = curr
            elif i > m:
                curr.next = pre
                if i == n:
                    start.next.next = next
                    start.next = curr
                    break

            pre, curr = curr, next
            i += 1
        return head.next

    def testReverseBetween(self):
        self.assertEqual(self.reverseBetween(ListNode.fromList([1,2,3,4,5]), 2, 2).toList(), [1,2,3,4,5])
        self.assertEqual(self.reverseBetween(ListNode.fromList([1,2,3,4,5]), 2, 4).toList(), [1,4,3,2,5])

import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL

Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL

Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

---
Basic idea: fast & slow pointer, fast go k step first (if tail then cycle to head), then move togother with slow, when fast is tail, slow.next is new head
        """
        if not head or not head.next or k == 0:
            return head
        slow, fast = head, head
        i = 1
        while i <= k:
            fast = fast.next
            if not fast:
                # cycle, length is i
                i = k - (k % i)
                if i == k:
                    return head
                fast = head
            i += 1

        while fast.next:
            slow, fast = slow.next, fast.next

        # slow.next is new head, fast is tail
        newHead, slow.next, fast.next = slow.next, None, head

        return newHead

    def testRotateRight(self):
        l = ListNode.fromList([1,2,3,4,5])
        self.assertEqual(self.rotateRight(l, 7).toList(), [4,5,1,2,3])

        l = ListNode.fromList([0,1,2])
        self.assertEqual(self.rotateRight(l, 4).toList(), [2,0,1])

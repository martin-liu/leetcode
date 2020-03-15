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
Basic idea:
        """
        if not head or k == 0:
            return head

        # find length and tail node
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # calculate real rotation number
        rotate = k % length
        if rotate == 0:
            return head

        # find new start and end node
        start = head
        end = None # end will be previous one of start
        for i in range(length - rotate - 1):
            if not end:
                end = start
            else:
                end = end.next
            start = start.next

        end.next = None
        tail.next = head # connect with head

        return start

    def testRotateRight(self):
        l = ListNode.fromList([1,2,3,4,5])
        self.assertCountEqual(self.rotateRight(l, 2).toList(), [4,5,1,2,3])

        l = ListNode.fromList([0,1,2])
        self.assertCountEqual(self.rotateRight(l, 4).toList(), [2,0,1])

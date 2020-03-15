import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
        """
        if not head or not head.next:
            return head

        pre, curr = head, head.next

        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
            else:
                pre = curr

            curr = curr.next
        return head

    def testDeleteDuplicates(self):
        self.assertEqual(self.deleteDuplicates(ListNode.fromList([1,2,3,3,4,4,5])).toList(), [1,2,3,4,5])
        self.assertEqual(self.deleteDuplicates(ListNode.fromList([1,1,1,2,3])).toList(), [1,2,3])
        self.assertEqual(self.deleteDuplicates(ListNode.fromList([1,1,1,2,2])).toList(), [1,2])

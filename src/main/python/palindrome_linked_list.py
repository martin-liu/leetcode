import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def isPalindrome(self, head: ListNode) -> bool:
        """
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

---
Basic Idea: find mid while reverse links from head till mid, then check if 2 sub linked list is equal

"""
        if not head:
            return True

        slow, fast = head, head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            pre, pre.next, slow = slow, pre, slow.next

        if fast:
            # odd
            slow = slow.next

        while pre and slow:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next

        return pre == slow

    def testPalindrome(self):
        self.assertTrue(self.isPalindrome(ListNode.fromList([1,2,2,1])))
        self.assertTrue(self.isPalindrome(ListNode.fromList([1,2,3,4,3,2,1])))
        self.assertFalse(self.isPalindrome(ListNode.fromList([1,2,3,4,3,2,5])))
        self.assertFalse(self.isPalindrome(ListNode.fromList([1,2])))

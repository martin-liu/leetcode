import unittest
from .ds import ListNode

class Solution(unittest.TestCase):
    def detectCycle(self, head: ListNode) -> ListNode:
        """
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.




Follow-up:
Can you solve it without using extra space?

---
Basic Idea: 2 pointers, p1 move 1 step, p2 move 2 steps. When meet, p2 go to head and start move 1 step, next meet node is cycle start.
        k = start - head, x = meet - start, r = cycle length
        2(k+x) = k+x+r
        k+x = r
        So that from meet to cycle start needs `start - meet = r - x = k` steps, which is same as head to cycle start
"""
        if not head or not head.next or not head.next.next:
            return None
        p1 = head.next
        p2 = head.next.next

        while p1 and p2 and p2.next and p1 != p2:
            p1 = p1.next
            p2 = p2.next.next

        if p1 != p2:
            return None
        else:
            # from head to move 1 step each time, when meet p1, it's the cycle start
            p2 = head
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p2

    def testCycle(self):
        head = ListNode.fromList([3,2,1])
        head.next.next.next = head.next
        self.assertEqual(head.next, self.detectCycle(head))

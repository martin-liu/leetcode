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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

---
Basic idea: add a new head, after process, return head.next. During process, use lastValid to store last valid node

        """
        if not head or not head.next:
            return head

        newHead = ListNode(-1)
        newHead.next = head
        head = newHead

        pre, curr = head.next, head.next.next
        lastValid = head
        while curr:
            if curr.val != pre.val:
                if lastValid.next == pre:
                    # no break, then pre is valid
                    lastValid = pre
                else:
                    # pre is invalid (coming from last round), connect to curr
                    lastValid.next = curr
            else:
                # when duplication, break the linked list until next valid node found
                lastValid.next = None
            pre = curr
            curr = curr.next

        return head.next

    def testDeleteDuplicates(self):
        self.assertEqual(self.deleteDuplicates(ListNode.fromList([1,2,3,3,4,4,5])).toList(), [1,2,5])
        self.assertEqual(self.deleteDuplicates(ListNode.fromList([1,1,1,2,3])).toList(), [2,3])
        self.assertEqual(self.deleteDuplicates(ListNode.fromList([1,1,1,2,2])), None)

import unittest

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(unittest.TestCase):
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.

        """
        cloneMap = {}
        def getClone(node):
            if not node:
                return None
            if node not in cloneMap:
                cloneMap[node] = Node(node.val)
            return cloneMap[node]

        curr = head
        while curr:
            clone = getClone(curr)
            clone.next = getClone(curr.next)
            clone.random = getClone(curr.random)

            curr = curr.next

        return getClone(head)

    def testCopy(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2
        n1.random = n2
        n2.random = n2
        node = self.copyRandomList(n1)
        self.assertNotEqual(node, n1)
        self.assertEqual(node.val, n1.val)
        self.assertEqual(node.random.val, n1.random.val)

import unittest
from .ds import Node
from queue import Queue

class Solution(unittest.TestCase):
    def connect(self, root: 'Node') -> 'Node':
        """
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;

}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100

"""
        if not root:
            return None
        qu = Queue()
        qu.put((root, 1))
        pre = preLevel = None
        while not qu.empty():
            curr, level = qu.get()
            if curr.left:
                qu.put((curr.left, level+1))
            if curr.right:
                qu.put((curr.right, level+1))

            if pre and preLevel == level:
                pre.next = curr
            pre, preLevel = curr, level
        return root

    def testConnect(self):
        tree = self.connect(Node.fromList([1,2,3,4,5,None,7]))
        self.assertEqual(tree.next, None)
        self.assertEqual(tree.left.next.val, 3)
        self.assertEqual(tree.left.right.next.val, 7)

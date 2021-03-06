import unittest
from .ds import Node
from queue import Queue

class Solution(unittest.TestCase):
    def connect(self, root: Node) -> Node:
        """
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

        """
        if not root:
            return root
        q = Queue()
        q.put((root, 0))
        pre = None
        while not q.empty():
            node, lvl = curr = q.get()
            if pre and pre[1] == lvl:
                pre[0].next = node
            pre = curr

            if node.left:
                q.put((node.left, lvl+1))
            if node.right:
                q.put((node.right, lvl+1))

        return root

    def connect2(self, root: Node) -> Node:
        if not root:
            return None
        curr = root
        next = curr.left
        while curr.left:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr = next
                next = curr.left
        return root

    def testConnect(self):
        tree = self.connect(Node.fromList([1,2,3,4,5,6,7]))
        self.assertEqual(tree.next, None)
        self.assertEqual(tree.left.next.val, 3)
        self.assertEqual(tree.left.right.next.val, 6)

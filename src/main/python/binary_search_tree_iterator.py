import unittest
from .ds import TreeNode

class BSTIterator:
    """
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

---
Basic Idea: stack. push left until leaf, when pop, push it's right, so that next pop will return right
"""

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
            curr = node.right.left
            while curr:
                self.stack.append(curr)
                curr = curr.left

        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

class Tests(unittest.TestCase):
    def testIterator(self):
        it = BSTIterator(TreeNode.fromList([7,3,15,None,None,9,20]))
        self.assertEqual(3, it.next())
        self.assertEqual(7, it.next())
        self.assertTrue(it.hasNext())
        self.assertEqual(9, it.next())
        self.assertTrue(it.hasNext())
        self.assertEqual(15, it.next())
        self.assertTrue(it.hasNext())
        self.assertEqual(20, it.next())
        self.assertFalse(it.hasNext())

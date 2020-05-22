import unittest
from queue import Queue
from .ds import TreeNode

class Codec:
    """
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

    def serialize(self, root):
        if not root:
            return []
        q = Queue()
        q.put(root)
        res = []
        while not q.empty():
            node = q.get()
            res.append(node and node.val)
            if node:
                q.put(node.left)
                q.put(node.right)

        # remove ending Nones
        while res and res[-1] is None:
            res.pop()

        return res

    def deserialize(self, data):
        if not data:
            return None
        q, root, L, i = Queue(), TreeNode(data[0]), len(data), 1
        q.put(root)

        while i < L and not q.empty():
            node = q.get()
            if data[i] is not None:
                node.left = TreeNode(data[i])
                q.put(node.left)
            i += 1
            if i < L and data[i] is not None:
                node.right = TreeNode(data[i])
                q.put(node.right)
            i += 1

        return root

class Tests(unittest.TestCase):
    def tests(self):
        codec = Codec()
        ls = []
        self.assertEqual(ls, codec.serialize(codec.deserialize(ls)))
        ls = [1,2,3,None,None,4,5]
        self.assertEqual(ls, codec.serialize(codec.deserialize(ls)))
        ls = [1,2,3,None,None,None,5,4]
        self.assertEqual(ls, codec.serialize(codec.deserialize(ls)))

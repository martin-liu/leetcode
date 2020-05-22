import unittest
from typing import List
from .ds import TreeNode

class Solution(unittest.TestCase):
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:

The size of the given array will be in the range [1,1000].
"""
        if not nums:
            return None
        i = nums.index(max(nums))
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        return root

    # O(n) via monotonic stack
    def constructMaximumBinaryTree2(self, nums: List[int]) -> TreeNode:
        stack = []

        for n in nums:
            last = None
            # pop until greater than n
            while stack and stack[-1].val < n:
                last = stack.pop()
            # curr node
            node = TreeNode(n)
            if last:
                # popped ones are in left of current one
                node.left = last
            if stack:
                # current one is right of existing one
                stack[-1].right = node
            stack.append(node)
        # bottom is biggest one, should be root
        return stack[0]

    def test(self):
        self.assertEqual([6,3,5,None,2,0,None,None,1], self.constructMaximumBinaryTree([3,2,1,6,0,5]).toList())
        self.assertEqual([6,3,5,None,2,0,None,None,1], self.constructMaximumBinaryTree2([3,2,1,6,0,5]).toList())

import unittest
from typing import List

class Solution(unittest.TestCase):
    def findDuplicate(self, nums: List[int]) -> int:
        """
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

---
Basic Idea: dup array will have cycle when loop `index=nums[index]`, cycle start is the dup one. Because when meet dup one, it will go back to a visited index, then it will continue and meet dup one again.
        now this is a linked list cycle detect problem
"""
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]

        fast = 0 # 0 is first
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow # met again one is dup one

    def testFind(self):
        self.assertEqual(2, self.findDuplicate([1,3,4,2,2]))
        self.assertEqual(3, self.findDuplicate([3,1,3,4,2]))

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

# Basic idea: recursive, find nums[i] which can one jump to end, then `jump(nums) = 1 + jump(nums[:i+1])`
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0
        if length == 2:
            return 1

        # if all nums are the same
        if len(set(nums)) == 1:
            return (length / nums[0]) - 1

        for i in range(length):
            if nums[i] >= length - 1 - i:
                return 1 + self.jump(nums[:i + 1])


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.jump([2,3,1]), 1)
        self.assertEqual(s.jump([1,2,1,1,1]), 3)
        self.assertEqual(s.jump([3,2,1]), 1)
        self.assertEqual(s.jump([2,3,1,1,4]), 2)

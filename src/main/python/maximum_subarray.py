import unittest
from typing import List

class Solution(unittest.TestCase):
    # Basic idea: keep current range only when sum > 0
    def maxSubArray(self, nums: List[int]) -> int:
        """
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
        """
        if not nums:
            return 0

        length = len(nums)
        if length == 1:
            return nums[0]

        l, r = 0, 0
        maxSum = nums[l]
        leftMove = False
        currSum = 0

        while l <= r and r < length:
            if l == r:
                currSum = nums[l]
            elif leftMove:
                currSum -= nums[l]
            else:
                currSum += nums[r]
            maxSum = currSum if currSum > maxSum else maxSum

            if nums[l] <= 0 or (nums[r] <= 0 and currSum <= 0):
                l += 1
                leftMove = True
                if l > r:
                    r = l
            else:
                r += 1
                leftMove = False

        return maxSum

    def testMaxSubArray(self):
        self.assertEqual(self.maxSubArray([8,-19,5,-4,20]), 21)
        self.assertEqual(self.maxSubArray([]), 0)
        self.assertEqual(self.maxSubArray([2]), 2)
        self.assertEqual(self.maxSubArray([-1, 2, -4]), 2)
        self.assertEqual(self.maxSubArray([-4, -2, -3]), -2)
        self.assertEqual(self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

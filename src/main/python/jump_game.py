import unittest
from typing import List

class Solution(unittest.TestCase):
    def canJump(self, nums: List[int]) -> bool:
        """Greedy"""
        # max index that can reach
        M, L = 0, len(nums)
        for i, n in enumerate(nums):
            # if current max cannot reach i, means fail
            if M < i:
                return False

            M = max(M, n + i)
            # if current max can reach last one, return true
            if M >= L-1:
                return True
        return False

    def canJump2(self, nums: List[int]) -> bool:
        """
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

---

Basic idea: from right to left, ensure every 0 is covered
        """
        if not nums:
            return False

        length = len(nums)
        zeroIndex = -1 # no zero found

        for i in range(length - 1, -1, -1):
            # last element can be 0
            if zeroIndex == -1 and nums[i] == 0 and i != length -1:
                zeroIndex = i
            elif zeroIndex != -1 and nums[i] > zeroIndex - i:
                # reset zero index when 0 covered
                zeroIndex = -1

        return zeroIndex == -1

    def testCanJump(self):
        self.assertFalse(self.canJump([]))
        self.assertTrue(self.canJump([0]))
        self.assertTrue(self.canJump([1, 0]))
        self.assertTrue(self.canJump([2, 3, 1, 1, 4]))
        self.assertFalse(self.canJump([3, 2, 1, 0, 4]))
        self.assertFalse(self.canJump([0, 3, 0, 2, 0, 4]))

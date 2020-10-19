import unittest
from typing import List

class Solution(unittest.TestCase):
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

-----
Basic Idea:
        If we need one more number to reach target, it can be any of vaild number.
        So overall = last one is N1 + last one is N2 + ...
        f(N, T) = f(N, T-N1) + F(N, T-N2) + ... + F(N, T-Nn) for any N <= T

        DP.
        state: target number

"""
        if not nums:
            return 0
        # dp[0] is terminate state
        dp = [1] + [0] * target
        # i starts with 1, because i will compare with n
        for i in range(1, target+1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i-n]

        return dp[target]

    # recursive version
    def combinationSum4Recur(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        res = 0
        for n in nums:
            if target >= n:
                res += self.combinationSum4Recur(nums, target-n)
        return res

    def test(self):
        self.assertEqual(0, self.combinationSum4([], 4))
        self.assertEqual(0, self.combinationSum4([9], 3))
        self.assertEqual(7, self.combinationSum4([1,2,3], 4))

import unittest
from typing import List

class Solution(unittest.TestCase):
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers, find the number of longest increasing subsequence.

        Example 1:

        Input: [1,3,5,4,7]
        Output: 2
        Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

        Example 2:

        Input: [2,2,2,2,2]
        Output: 5
        Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
        Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

       ---
        Basic Idea: DP.
        base state: 0
        state: start index j, end index i
        choice: if meet same max length, count[i] += count[j]; else length should +1
        result: max length of LIS end at i, count of LIS end at i
        """
        n, res, max_len = len(nums), 0, 0
        leng, cnt = [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                # increasing
                if nums[i] > nums[j]:
                    # leng[j] and cnt[j] is already calculated, while i is not.
                    # since nums[i] > nums[j], now we should have length `leng[j]+1`,
                    # if `leng[i]<leng[j]+1`, means we didn't meet same max length
                    if leng[i] < leng[j] + 1:
                        # set new length
                        leng[i] = leng[j] + 1
                        cnt[i] = cnt[j]
                    # if `leng[i]==leng[j]+1`, means meet same max length
                    elif leng[i] == leng[j] + 1:
                        # add count when meet same max length
                        cnt[i] += cnt[j]
            # count when same max len
            if max_len == leng[i]:
                res += cnt[i]
            # reset when found longer length
            if max_len < leng[i]:
                max_len = leng[i]
                res = cnt[i]

        return res;

    def test(self):
        self.assertEqual(2, self.findNumberOfLIS([1,5,3]))
        self.assertEqual(2, self.findNumberOfLIS([1,3,5,4,7]))
        self.assertEqual(5, self.findNumberOfLIS([2,2,2,2,2]))
        self.assertEqual(10, self.findNumberOfLIS([1,2,3,1,2,3,1,2,3]))

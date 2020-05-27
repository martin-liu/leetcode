import unittest
from typing import List

class Solution(unittest.TestCase):
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""
        # [1,2...] and [...8,9]
        if n < (1+k)*k/2 or (19-k)*k/2 < n:
            return []
        res = []
        def backtrack(path, start, t):
            if len(path) == k:
                if t == 0:
                    res.append(path)
            elif t > 0:
                for i in range(start, 10):
                    backtrack(path+[i], i+1, t-i)
        backtrack([], 1, n)
        return res

    def test(self):
        self.assertEqual([[1,2,4]], self.combinationSum3(3, 7))
        self.assertEqual([[1,2,6], [1,3,5], [2,3,4]], self.combinationSum3(3, 9))

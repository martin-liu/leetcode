import unittest
from typing import List

class Solution(unittest.TestCase):
    def countBits(self, num: int) -> List[int]:
        """
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

---
Basic Idea: DP.
        f(i) = f(i>>1) + i&1
        f(i) is number of 1 for i, which equals number of 1 for i without last number + 1 in last number
"""
        cache = {}
        def count(n):
            if n < 1:
                return 0
            if n in cache:
                return cache[n]
            res = count(n>>1) + (n&1)
            cache[n] = res
            return res

        return [count(n) for n in range(num+1)]

    def countBits2(self, num: int) -> List[int]:
        """
        n & (n-1) will remove last 1
        """
        def count(n):
            c = 0
            while n != 0:
                n = n & (n-1)
                c += 1
            return c

        return [count(n) for n in range(num+1)]

    def test(self):
        self.assertEqual([0,1,1], self.countBits(2))
        self.assertEqual([0,1,1,2,1,2], self.countBits(5))
        self.assertEqual([0,1,1,2,1,2], self.countBits2(5))

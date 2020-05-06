import unittest

class Solution(unittest.TestCase):
    def trailingZeroes(self, n: int) -> int:
        """
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

"""
        ret = 0
        while n != 0:
            n = n // 5
            ret += n
        return ret

    def testTrailing(self):
        self.assertEqual(0, self.trailingZeroes(3))
        self.assertEqual(1, self.trailingZeroes(5))
        self.assertEqual(6, self.trailingZeroes(25))

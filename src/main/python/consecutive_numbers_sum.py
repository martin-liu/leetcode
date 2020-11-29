import unittest
import math

class Solution(unittest.TestCase):
    def consecutiveNumbersSum(self, N: int) -> int:
        """
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.

---
Basic Idea:
       let's say we have k numbers sum to N, `x + x+1 + x+2 + ... x+k-1 = N`
        -> (x + x+k-1) * k/2 = N
        -> xk = N - (k-1) * k/2
        ->
        1. (k-1)*k = 2N - 2xk -> k^2 = 2N - 2xk + k < 2N -> `k < sqrt(2N)`
        2. for any k, if `(N - (k-1) * k/2) % k == 0`, means we found a `x` which matches
"""
        res = 1
        for k in range(2, math.ceil(math.sqrt(2 * N))):
            if (N - (k-1) * k/2) % k == 0:
                res += 1
        return res

    def test(self):
        self.assertEqual(2, self.consecutiveNumbersSum(5))
        self.assertEqual(3, self.consecutiveNumbersSum(9))
        self.assertEqual(4, self.consecutiveNumbersSum(15))

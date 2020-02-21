import unittest

class Solution(unittest.TestCase):
    def mySqrt(self, x: int) -> int:
        """
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

---

Basic idea: binary search
        """
        if x <= 0:
            return 0

        if x < 4:
            return 1

        t = 2
        while x / t > t:
            t *= 2
        if t * t == x:
            return t

        l, r = t//2, t
        while l < r:
            t = (l + r) // 2
            if t * t > x:
                if (t-1)*(t-1) < x:
                    return t - 1
                r = t
            elif t * t < x:
                if (t+1)*(t+1) > x:
                    return t
                l = t
            else:
                return t

        return t


    def testMySqrt(self):
        self.assertEqual(self.mySqrt(4), 2)
        self.assertEqual(self.mySqrt(5), 2)
        self.assertEqual(self.mySqrt(6), 2)
        self.assertEqual(self.mySqrt(7), 2)
        self.assertEqual(self.mySqrt(8), 2)
        self.assertEqual(self.mySqrt(9), 3)
        self.assertEqual(self.mySqrt(10), 3)

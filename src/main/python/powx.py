"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/2^2 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

# Basic idea: recursively do `n / 2`
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ret = self.doPow(x, n)
        return round(ret,5)

    def doPow(self, x, n):
        if n == 0:
            return 1
        elif x == 0:
            return 0

        if n < 0:
            return self.myPow(1/x, -n)

        z = self.doPow(x, n // 2)
        if n % 2 == 0:
            return z * z
        else:
            return z * z * x


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.myPow(2.00000, 10), 1024.00000)
        self.assertEqual(s.myPow(2.10000, 3), 9.26100)
        self.assertEqual(s.myPow(2.00000, -2), 0.25000)
        self.assertEqual(s.myPow(0.00001, 2147483647), 0)
        self.assertEqual(s.myPow(0.44894, -5), 54.83508)

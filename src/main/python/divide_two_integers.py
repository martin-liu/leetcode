# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

# Basic idea: increase divisor to *2 every round to reduce the time complexity
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # same prefix
        positive = (dividend < 0) == (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        ret = 0

        while dividend >= divisor:
            # set or reset new divisor and i
            newDivisor, i = divisor, 1
            # try get close to the final result
            # every time *2 of the divisor, if fail, then back to reset the divisor
            while dividend >= newDivisor:
                # reduce dividend and add ret
                dividend -= newDivisor
                ret += i

                # *2 for both i and newDivisor, so that we reduce the check to logN time
                i <<= 1 # same as i *= 2
                newDivisor <<= 1

        if not positive:
            ret = -ret
        # process overflow
        return min(max(-2147483648, ret), 2147483647)

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.divide(1, -1), -1)
        self.assertEqual(s.divide(-1, -1), 1)
        self.assertEqual(s.divide(5, 2), 2)
        self.assertEqual(s.divide(9, 2), 4)
        self.assertEqual(s.divide(-2147483648, -1), 2147483647)

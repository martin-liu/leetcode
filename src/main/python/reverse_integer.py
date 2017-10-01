# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Check before overflow (32 bit integer)

# Basic idea: iteratively mod 10 and build another number by remainder * 10
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxInt = 2 ** 31 - 1
        ret = 0

        if x == 0:
            return 0
        elif x < 0:
            return - self.reverse(-x)
        else:
            while x > 0:
                (x, r) = divmod(x, 10)
                # check overflow
                if (maxInt - r) / 10 < ret:
                    return 0
                ret = ret * 10 + r
            return ret



# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.reverse(123), 321)
        self.assertEqual(s.reverse(-123), -321)
        self.assertEqual(s.reverse(1534236469), 0)

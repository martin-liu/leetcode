# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# Basic idea: check from right to left, determine plus or minus
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanMap = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        ret = 0
        pre = 0
        # reverse for loop
        for c in s[::-1]:
            n = romanMap[c]
            if n >= pre:
                ret += n
            else:
                ret -= n
            pre = n

        return ret

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.romanToInt('IV'), 4)
        self.assertEqual(s.romanToInt('I'), 1)
        self.assertEqual(s.romanToInt('II'), 2)
        self.assertEqual(s.romanToInt('VIII'), 8)
        self.assertEqual(s.romanToInt('IX'), 9)
        self.assertEqual(s.romanToInt('XL'), 40)
        self.assertEqual(s.romanToInt('CDL'), 450)
        self.assertEqual(s.romanToInt('MCMXCVIII'), 1998)

import unittest

class Solution(unittest.TestCase):
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

---
Basic idea: divmod, if r repeat, means repeat
"""
        # deal with negative case
        negative = (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)

        q, r = divmod(numerator, denominator)
        prefix = '-' if negative else ''

        if r == 0:
            return prefix + str(q)

        prefix += str(q) + '.'
        rMap = {} # store start position of repeat part
        tail = ""
        while r != 0:
            if r in rMap:
                i = rMap[r]
                tail = tail[:i] + '(' + tail[i:] + ')'
                break
            else:
                # r -> position
                rMap[r] = len(tail)
                q, r = divmod(r*10, denominator)
                tail += str(q)
        return prefix + tail

    def testFraction(self):
        self.assertEqual("-2147483648", self.fractionToDecimal(-2147483648, 1))
        self.assertEqual("-6.25", self.fractionToDecimal(-50, 8))
        self.assertEqual("0.(003)", self.fractionToDecimal(1, 333))
        self.assertEqual("0.1(6)", self.fractionToDecimal(1, 6))
        self.assertEqual("0.5", self.fractionToDecimal(1, 2))
        self.assertEqual("2", self.fractionToDecimal(2, 1))
        self.assertEqual("0.(6)", self.fractionToDecimal(2, 3))
        self.assertEqual("0.(4)", self.fractionToDecimal(4, 9))
        self.assertEqual("0.(012)", self.fractionToDecimal(4, 333))

"""
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    # one solution
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))

    # another solution
    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return '0'
        elif num1 == '1':
            return num2
        elif num2 == '1':
            return num1
        elif len(num2) > len(num1):
            return self.multiply2(num2, num1)

        (q, r) = self.divide_2(num2)
        z = self.multiply2(num1, q)

        z2 = self.add(z, z)
        if r == 0:
            return z2
        else:
            return self.add(num1, z2)

    def divide_2(self, num):
        q, r = 0, 0
        ret = ''
        for c in num:
            q, r = divmod(int(c) + r * 10, 2)
            if not (ret == '' and q == 0):
                ret += str(q)
        return (ret, r)

    def add(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        maxLen = max(len1, len2)

        s, carry = 0, 0
        ret = ''
        for i in range(-1, -maxLen - 1, -1):
            if len1 + i < 0:
                sm = int(num2[i]) + carry
            elif len2 + i < 0:
                sm = int(num1[i]) + carry
            else:
                sm = int(num1[i]) + int(num2[i]) + carry

            if sm >= 10:
                carry = 1
                s = sm - 10
            else:
                carry = 0
                s = sm
            ret = str(s) + ret

        if carry == 1:
            ret = '1' + ret

        return ret


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.multiply('1', '2'), '2')
        self.assertEqual(s.multiply('3', '2'), '6')
        self.assertEqual(s.multiply('13', '27'), '351')

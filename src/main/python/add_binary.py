import unittest

class Solution(unittest.TestCase):
    def addBinary(self, a: str, b: str) -> str:
        """
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
        """
        if not a:
            return b
        elif not b:
            return a

        lenA = len(a)
        lenB = len(b)
        # ensure a < b
        if lenA > lenB:
            a, b = b, a
            lenA, lenB = lenB, lenA

        carry = 0
        ret = ''

        for i in range(lenB):
            aNum = a[lenA - i - 1] if i < lenA else '0'
            bNum = b[lenB - i - 1]

            carry, n = divmod(int(aNum) + int(bNum) + carry, 2)
            ret = str(n) + ret
            if i >= lenA and carry == 0:
                return b[:lenB-i-1] + ret

        if carry == 1:
            return "1" + ret
        else:
            return ret

    def testAddBinary(self):
        self.assertEqual(self.addBinary("", "1"), "1")
        self.assertEqual(self.addBinary("11", "1"), "100")
        self.assertEqual(self.addBinary("1010", "1011"), "10101")
        self.assertEqual(self.addBinary("100", "110010"), "110110")

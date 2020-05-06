import unittest

class Solution(unittest.TestCase):
    def convertToTitle(self, n: int) -> str:
        """
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
        ret = ""
        while n != 0:
            # n-1 since mod starts with 0 (0~25)
            n, r = divmod(n-1, 26)
            ret = chr(r+65) + ret
        return ret

    def testConvert(self):
        self.assertEqual('A', self.convertToTitle(1))
        self.assertEqual('AB', self.convertToTitle(28))
        self.assertEqual('ZY', self.convertToTitle(701))

import unittest

class Solution(unittest.TestCase):
    def titleToNumber(self, s: str) -> int:
        """
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

"""
        ret = 0
        for c in s:
            ret = ret * 26 + ord(c) - 64

        return ret

    def testTitle(self):
        self.assertEqual(1, self.titleToNumber('A'))
        self.assertEqual(28, self.titleToNumber('AB'))
        self.assertEqual(701, self.titleToNumber('ZY'))

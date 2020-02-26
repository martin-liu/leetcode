import unittest

class Solution(unittest.TestCase):
    def lengthOfLastWord(self, s: str) -> int:
        """
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

        """
        if not s:
            return 0

        l, r = 0, -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if r != -1:
                    return r - l + 1
            else:
                if r == -1:
                    r = i
                    l = r
                else:
                    l = i
        return r - l + 1

    def testLengthOfLastWord(self):
        self.assertEqual(self.lengthOfLastWord(""), 0)
        self.assertEqual(self.lengthOfLastWord("   "), 0)
        self.assertEqual(self.lengthOfLastWord("  hi "), 2)
        self.assertEqual(self.lengthOfLastWord("hi "), 2)
        self.assertEqual(self.lengthOfLastWord("Hello World"), 5)

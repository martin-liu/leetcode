
# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        l, r = 0, len(s)-1

        ls = list(s)
        while l < r:
            ls[l], ls[r] = ls[r], ls[l]
            l += 1
            r -= 1
        return "".join(ls)

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
       s = Solution()
       self.assertEqual(s.reverseString(None), None)
       self.assertEqual(s.reverseString(""), "")
       self.assertEqual(s.reverseString("hello"), "olleh")


# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None:
            return None
        else:
            ret = []
            length = len(s)
            for i in range(length - 1, -1, -1):
                ret.append(s[i])
            return "".join(ret)


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
       s = Solution()
       self.assertEqual(s.reverseString(None), None)
       self.assertEqual(s.reverseString(""), "")
       self.assertEqual(s.reverseString("hello"), "olleh")

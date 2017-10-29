# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ret = -1

        lenH = len(haystack)
        lenN = len(needle)

        # empty needle
        if lenN == 0:
            return 0
        # haystack less chars than needle
        elif lenH < lenN:
            return ret

        for i in range(0, lenH - lenN + 1):
            j = 0
            while j < lenN and haystack[i + j] == needle[j]:
                j += 1

            if j == lenN:
                # match
                return i

        return ret

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.strStr("abc", "b"), 1)
        self.assertEqual(s.strStr("abc", ""), -1)
        self.assertEqual(s.strStr("abc", "bc"), 1)
        self.assertEqual(s.strStr("", ""), 0)

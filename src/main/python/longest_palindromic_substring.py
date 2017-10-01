# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.

# Example:

# Input: "cbbd"

# Output: "bb"


# Basic idea: insert `#` between each char, so that `bb` -> `#b#b#`, now there's only one pattern of palindrome
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if s == None or length == 1:
            return s

        chars = ["#"]
        # insert `#` between each char, now length will be 2 * len + 1
        for i in range(length):
            chars.append(s[i])
            chars.append("#")

        ret = ""
        charsLen = len(chars)
        for i in range(charsLen):
            j = 0
            # s[i] as central, go check left and right until they are not equal
            while i - j >= 0 and i + j < charsLen and chars[i - j] == chars[i + j]:
                j += 1

            # j added 1 one more time which failed the while loop
            j -= 1

            # s[n] -> chars[2 * n + 1], so that chars `index // 2` will come to `n`
            # for example, `#!#a#b#a#?#` -> [2, 9) <=> `!aba?` -> [1, 4)
            # for example, `#!#b#b#?#` -> [2, 7) <=> `!bb?` -> [1, 3)
            start = (i - j) // 2
            end = (i + j) // 2
            p = s[start:end]

            # save longest one
            ret = ret if len(ret) >= len(p) else p

        return ret

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("babad"), "bab")
        self.assertEqual(s.longestPalindrome("cbbd"), "bb")

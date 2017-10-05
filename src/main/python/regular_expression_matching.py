# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true

# Basic idea: use a match array to iterate and record match state
# 1. For `x*` style, from right to left, mark true as much as it can
# 2. For `x` style, from left to right, find a match next to `True`, and mark it as True, mark non-match as False (this will overwrite some of True in #1, so that solved overlap issue)
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        lenS = len(s)
        charMatch = lambda s, p: p == '.' or s == p

        # fill an `lenS + 1` length array with False
        match = [False for i in range(lenS + 1)]
        # initially mark last one as True
        match[lenS] = True

        # iterate `p` from right to left
        i = len(p) - 1
        while i >= 0:
            if p[i] == '*':
                # in `*` mode, iterate `s` from right to left, match as many as it can
                for j in range(lenS - 1, -1, -1):
                    # mark continuous match part as True in match array, until a False happen
                    match[j] = match[j] or (match[j + 1] and charMatch(s[j], p[i - 1]))
                i -= 2
            else:
                # in non `*` mode, iterate `s` from left to right, match the char step by step
                for j in range(lenS):
                    match[j] = match[j + 1] and charMatch(s[j], p[i])
                # mark last one as False when not in initial state,
                # so that it will spread `False` from right to left step by step, after at most `len(s)` times, it will mark all the match array as False,
                # so when `s` travel finished while `p` is not, it will come to False
                match[lenS] = False
                i -= 1

        # if first one is True, means all matched, otherwise failed
        return match[0];

# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isMatch("aa","aa"))
        self.assertFalse(s.isMatch("aa","aaa"))
        self.assertTrue(s.isMatch("aa", "a*"))
        self.assertTrue(s.isMatch("aaa", "a*a"))
        self.assertTrue(s.isMatch("aaa", "a*aaa"))
        self.assertTrue(s.isMatch("aaa", "a*aab*"))
        self.assertTrue(s.isMatch("aa", ".*"))
        self.assertTrue(s.isMatch("ab", ".*"))
        self.assertTrue(s.isMatch("aab", "c*a*b"))
        self.assertTrue(s.isMatch("aabcc", "c*a*bc*"))
        self.assertFalse(s.isMatch("aa","a"))
        self.assertFalse(s.isMatch("aaa","aa"))

"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""

# Basic idea: save position for `*` and assume it match ZERO character,
# when failed match after that, then go back to the position and assume `*` match one more character
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        i, j, starS, starP = 0, 0, 0, -1
        lenS, lenP = len(s), len(p)

        while i < lenS:
            # eq or '?', then both go next
            if j < lenP and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < lenP and p[j] == '*':
                starS, starP = i, j  # mark start matching of string/pattern for `*`, so that we can go back for rematch
                j += 1          # j go next, assuming `*` match ZERO character
            elif starP != -1:
                # now not matching for above cases, means previous assumption is wrong,
                # need to go back of `*` position to retry
                starS += 1     # assuming `*` match one more character in string
                i = starS
                j = starP + 1  # j go back to the position after `*`
            else:
                # none of above cases, means failed to match
                return False

        # in case there's still tailing `*`
        while j < lenP and p[j] == '*':
            j += 1

        return j == lenP        # traversal all of pattern


# -----------------------------
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertTrue(s.isMatch("aa", "aa"))
        self.assertTrue(s.isMatch("aa", "*"))
        self.assertTrue(s.isMatch("aa", "a*"))
        self.assertTrue(s.isMatch("aa", "?*"))
        self.assertTrue(s.isMatch("aab", "*?b"))
        self.assertTrue(s.isMatch("aabb", "*?b"))
        self.assertTrue(s.isMatch("aab", "a*ab"))
        self.assertTrue(s.isMatch("", ""))
        self.assertFalse(s.isMatch("aa", "a"))
        self.assertFalse(s.isMatch("aaa", "a"))
        self.assertFalse(s.isMatch("aab", "c*a*b"))

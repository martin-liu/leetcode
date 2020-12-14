import unittest

class Solution(unittest.TestCase):
    def countSubstrings(self, s: str) -> int:
        """
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.

----
"""
        if not s:
            return 0

        L = len(s)
        dp = [[False for _ in range(L)] for _ in range(L)]
        res = 0
        for i in range(L-1, -1, -1):
            for j in range(i, L):
                dp[i][j] = s[i] == s[j] and (True if j-i < 2 else dp[i+1][j-1])
                res += dp[i][j]
        return res

    def countSubstrings2(self, s: str) -> int:
        """
Basic Idea: pal have 2 cases, even or odd, `aa`, `aba`. So for each index, try to extend left/right for both even and odd
"""
        if not s:
            return 0

        def extractPal(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        count = 0
        for i in range(len(s)):
            count += extractPal(i, i)
            count += extractPal(i, i+1)
        return count

    def test(self):
        self.assertEqual(3, self.countSubstrings("abc"))
        self.assertEqual(4, self.countSubstrings("abb"))
        self.assertEqual(6, self.countSubstrings("aaa"))

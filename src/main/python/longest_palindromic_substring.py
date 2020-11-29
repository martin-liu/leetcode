import unittest

class Solution(unittest.TestCase):
    def longestPalindrome(self, s):
        """
 Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

 Example:

 Input: "babad"

 Output: "bab"

 Note: "aba" is also a valid answer.

 Example:

 Input: "cbbd"

 Output: "bb"
----
 Basic Idea: DP.
        State: start index; end index
        Output: isPal?
        Choice: f(i,j) = True if s[i] == s[j] and f(i+1,j-1) == True
        Direction: i--, j++
        """
        if not s:
            return ""
        L = len(s)
        dp = [[False for i in range(L)] for j in range(L)]

        l, r = 0, 0
        # i from L-1 to 0, because f(i, j) depends on f(i+1, j-1)
        for i in range(L-1, -1, -1):
            # j from 0 to L+1, because f(i, j) depends on f(i+1, j-1)
            for j in range(i, L):
                dp[i][j] = s[i] == s[j] and (True if j-i < 2 else dp[i+1][j-1])

                if dp[i][j] and j-i >= r-l:
                    l, r = i, j

        return s[l:r+1]

    def longestPalindrome2(self, s):
        """
        Basic idea: insert `#` between each char, so that `bb` -> `#b#b#`, now there's only one pattern of palindrome
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
            # don't use `< charsLen - 1`, otherwise `chars[i-j]==chars[i+j]` will not check when `i+j==charsLen-1`
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

    def test(self):
        self.assertEqual(self.longestPalindrome("babad"), "bab")
        self.assertEqual(self.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.longestPalindrome("aaaa"), "aaaa")
        self.assertEqual(self.longestPalindrome("abac"), "aba")

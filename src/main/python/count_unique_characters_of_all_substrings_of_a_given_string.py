import unittest

class Solution(unittest.TestCase):
    def uniqueLetterString(self, s: str) -> int:
        """
Let's define a function countUniqueChars(s) that returns the number of unique characters on s, for example if s = "LEETCODE" then "L", "T","C","O","D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

On this problem given a string s we need to return the sum of countUniqueChars(t) where t is a substring of s. Notice that some substrings can be repeated so on this case you have to count the repeated ones too.

Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.



Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:

Input: s = "LEETCODE"
Output: 92


Constraints:

0 <= s.length <= 10^4
s contain upper-case English letters only.

--
Basic Idea: DP. dp[i] is number of all uniq chars that end at position i, final result is sum(dp). So that can use curr variable instead of dp array.
        dp[i] = dp[i-1] + 1 + (i-pre[c]) - (pre[c]-pree[c])
        `1` for new char itself as substr
        `i` for i sub strs ends at i (e.g. i=3, there're 3 sub strs ends at 3, [03,13,23])
        `-pre[c]` if char already in s[:i], e.g. AB + A, then only between curr and previous position of the char will count, so that `i-pre[c]`
        `-(pre[c]-pree[c])` if there's pree of char, means previous between `curr, pre` will not count any more (which already count in dp[i-1]), so that `-(pre[c]-pree[c])`

        e.g. ABC
        dp = [1, 3, 6]

        e.g. ABA
        dp = [1, 3, 4]

        e.g. ABACA
        dp = [1, 3, 4, 8, 8]
"""
        ret = curr = 0
        M = 1e9 + 7
        # pre and pree position of char
        pre, pree = {}, {}
        for i in range(len(s)):
            # curr = curr + 1 + (i - pre) - (pre - pree)
            curr += 1 + i - pre.get(s[i], 0) * 2 + pree.get(s[i], 0)
            ret = (ret + curr) % M
            pree[s[i]] = pre.get(s[i], 0)
            pre[s[i]] = i + 1
        return ret

    def testUniq(self):
        self.assertEqual(10, self.uniqueLetterString("ABC"))
        self.assertEqual(8, self.uniqueLetterString("ABA"))
        self.assertEqual(16, self.uniqueLetterString("ABAC"))
        self.assertEqual(24, self.uniqueLetterString("ABACA"))
        self.assertEqual(92, self.uniqueLetterString("LEETCODE"))

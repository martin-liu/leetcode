import unittest

class Solution(unittest.TestCase):
    def numDistinct(self, s: str, t: str) -> int:
        """
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
        """
        if not s or not t or len(s) < len(t):
            return 0
        if len(s) == len(t):
            return 1 if s == t else 0

        nums = [[0 for _ in range(len(t))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(t)):
                if i == 0 and j == 0:
                    nums[i][j] = 1 if s[i] == t[j] else 0
                elif i < j:
                    nums[i][j] = 0
                elif s[i] == t[j]:
                    # i cannot be 0, j can be 0
                    nums[i][j] = nums[i-1][j] + (nums[i-1][j-1] if j > 0 else 1)
                else:
                    nums[i][j] = nums[i-1][j]

        return nums[len(s)-1][len(t)-1]

    def testDistinc(self):
        self.assertEqual(3, self.numDistinct("rabbbit", "rabbit"))
        self.assertEqual(5, self.numDistinct("babgbag", "bag"))

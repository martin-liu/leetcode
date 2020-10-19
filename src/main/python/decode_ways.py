import unittest

class Solution(unittest.TestCase):
    def numDecodings(self, s: str) -> int:
        """
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

----
Basic idea: DP. Consider char is 0 and 2 char > 26 case.
        when s[i] == 0, dp[i] == dp[i-2] if s[i-1:i+1] is valid; when s[i] == 1, if s[i-1] == '0' or s[i-1:i+1] > 26, dp[i] = dp[i-1], else dp[i] = dp[i-2] + dp[i-1]
        """
        if not s or s[0] == '0':
            return 0

        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                dp[i] = 1
            else:
                n2 = int(s[i-1:i+1])
                if n2 == 0 or (n2 > 26 and s[i] == '0'):
                    return 0
                # pre of pre, when i == 1, use 1 because there's one way
                pree = dp[i-2] if i > 1 else 1
                if s[i] == '0':
                    # if curr is 0, only way is jump from pree + x0
                    dp[i] = pree
                elif s[i-1] == '0' or n2 > 26:
                    # if pre is 0 or n2 is invalid, only way is jump from pre
                    dp[i] = dp[i-1]
                else:
                    # can jump from both pree or pre
                    dp[i] = pree + dp[i-1]

        return dp[-1]

    def testNumDecodings(self):
        self.assertEqual(self.numDecodings(""), 0)
        self.assertEqual(self.numDecodings("0"), 0)
        self.assertEqual(self.numDecodings("00"), 0)
        self.assertEqual(self.numDecodings("10"), 1)
        self.assertEqual(self.numDecodings("100"), 0)
        self.assertEqual(self.numDecodings("101"), 1)
        self.assertEqual(self.numDecodings("110"), 1)
        self.assertEqual(self.numDecodings("012"), 0)
        self.assertEqual(self.numDecodings("27"), 1)
        self.assertEqual(self.numDecodings("12"), 2)
        self.assertEqual(self.numDecodings("226"), 3)
        self.assertEqual(self.numDecodings("227"), 2)
        self.assertEqual(self.numDecodings("230"), 0)
        self.assertEqual(self.numDecodings("1212"), 5)
        self.assertEqual(self.numDecodings("12120"), 3)

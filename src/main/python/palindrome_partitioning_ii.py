import unittest

class Solution(unittest.TestCase):
    def minCut(self, s: str) -> int:
        """
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Basic idea: DP. k->k+1, When add new char to the end, only if palindrome found, then it can have smaller number.

Use 2 dp, one `palindromes[j][i]` means s[j:i+1] is palindrome or not, and one `cuts[i]` means minimum number"""
        if not s or len(s) == 1:
            return 0
        n = len(s)
        cuts = [0] * n
        # n * n
        palindromes = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            # no more than `i`(i.e. len-1) times of cut
            cuts[i] = i
            for j in range(i+1):
                # only when s[j:i+1] is palindrome, then it will have smaller number of cut
                if (i-j<2 or palindromes[j+1][i-1]) and s[j] == s[i]:
                    palindromes[j][i] = True
                    # when s[j:i+1] is palindrome, if j is 0, means s is palindrome, return 0
                    # if j is not 0, check `cuts[j-1]+1`
                    cuts[i] = 0 if j == 0 else min(cuts[i], cuts[j-1]+1)
        return cuts[n-1]

    def testminCut(self):
        self.assertEqual(452, self.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))
        self.assertEqual(1, self.minCut("aab"))
        self.assertEqual(0, self.minCut("aabaa"))
        self.assertEqual(1, self.minCut("aabab"))
        self.assertEqual(1, self.minCut("aaba"))
        self.assertEqual(1, self.minCut("aabcb"))
        self.assertEqual(2, self.minCut("aabcbc"))

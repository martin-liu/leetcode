import unittest

class Solution(unittest.TestCase):
        def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
            """
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
            """
            if not s3:
                return not s1 and not s2
            elif not s1:
                return s2 == s3
            elif not s2:
                return s1 == s3
            elif len(s1) + len(s2) != len(s3):
                return False
            elif s1[0] != s3[0] and s2[0] != s3[0]:
                return False

            l1, l2, l3 = len(s1), len(s2), len(s3)
            checks = [[False for _ in range(l2+1)] for _ in range(l1+1)]
            for i in range(l1+1):
                for j in range(l2+1):
                    if i == 0 and j == 0:
                        checks[i][j] = True
                    elif i == 0:
                        checks[i][j] = checks[i][j-1] and s2[j-1] == s3[i+j-1]
                    elif j == 0:
                        checks[i][j] = checks[i-1][j] and s1[i-1] == s3[i+j-1]
                    else:
                        checks[i][j] = (checks[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                            (checks[i][j-1] and s2[j-1] == s3[i+j-1])

            return checks[l1-1][l2-1]

        def testIsInterleave(self):
            self.assertTrue(self.isInterleave("", "", ""))
            self.assertTrue(self.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
            self.assertFalse(self.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

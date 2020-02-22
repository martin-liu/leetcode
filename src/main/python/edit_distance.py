import unittest

class Solution(unittest.TestCase):
    def minDistance(self, word1: str, word2: str) -> int:
        """
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

---
Basic idea: DP of min(insert, delete, replace), from 0 to len+1, which 0 means empty string, i means word[i-1]
        """
        len1 = len(word1)
        len2 = len(word2)

        if not word1:
            return len2
        elif not word2:
            return len1

        dis = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0:
                    dis[i][j] = j
                elif j == 0:
                    dis[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dis[i][j] = dis[i-1][j-1]
                else:
                    # minimal of 3 type of actions (delete, insert, replace)
                    dis[i][j] = min(dis[i-1][j]+1, dis[i][j-1]+1, dis[i-1][j-1]+1)
        return dis[len1][len2]

    def testMinDistance(self):
        self.assertEqual(self.minDistance("", ""), 0)
        self.assertEqual(self.minDistance("", "e"), 1)
        self.assertEqual(self.minDistance("e", ""), 1)
        self.assertEqual(self.minDistance("e", "s"), 1)
        self.assertEqual(self.minDistance("e", "e"), 0)
        self.assertEqual(self.minDistance("ae", "e"), 1)
        self.assertEqual(self.minDistance("ae", "b"), 2)
        self.assertEqual(self.minDistance("ae", "a"), 1)
        self.assertEqual(self.minDistance("orse", "ros"), 3)
        self.assertEqual(self.minDistance("horse", "ros"), 3)
        self.assertEqual(self.minDistance("intention", "execution"), 5)

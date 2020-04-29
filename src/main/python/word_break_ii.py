import unittest
from typing import List

class Solution(unittest.TestCase):
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"

]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

---
Basic Idea: DP to verify if valid, then Backtracking to get all list
"""
        if not s or not wordDict:
            return []
        wordMap = {}
        minLen = float('inf')
        maxLen = 0
        for word in wordDict:
            wordMap[word] = True
            minLen = min(minLen, len(word))
            maxLen = max(maxLen, len(word))

        dp = [False] * len(s)
        for i in range(minLen-1, len(s)):
            if i == minLen - 1:
                dp[i] = s[:i+1] in wordMap
            elif i < maxLen and s[:i+1] in wordMap:
                dp[i] = True
            else:
                j = i - minLen
                while j >= 0 and j >= i - maxLen:
                    if s[j+1:i+1] in wordMap and dp[j]:
                        dp[i] = True
                        break
                    j -= 1

        if not dp[len(s)-1]:
            return []

        ret = []
        def backtrack(start, track):
            if start >= len(s):
                ret.append(" ".join(track))
            else:
                j = start + minLen - 1
                while j < len(s) and j < start + maxLen:
                    if s[start:j+1] in wordMap:
                        backtrack(j+1, track + [s[start:j+1]])
                    j += 1

        backtrack(0, [])
        return ret

    def testWordBreak(self):
        self.assertEqual([], self.wordBreak("catsandog", ["cat", "cats", "and", "sand", "dog"]))
        self.assertCountEqual(["cats and dog", "cat sand dog"], self.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
        self.assertCountEqual(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"], self.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
        self.assertEqual([], self.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))

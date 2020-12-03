import unittest
from typing import List

class Solution(unittest.TestCase):
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

---
Basic Idea: DP, `f(i) = any( f(i-len(word)) and for word in dict )`
"""
        dp = [False] * len(s)
        for i in range(len(s)):
            dp[i] = any(
                s[:i+1] == word or
                (
                    i >= len(word) and
                    dp[i-len(word)] and
                    s[i-len(word)+1:i+1] == word
                )
                for word in wordDict
            )
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False

        wordMap = {}
        minWordLen = float('inf')
        maxWordLen = 0
        for word in wordDict:
            wordMap[word] = True
            minWordLen = min(minWordLen, len(word))
            maxWordLen = max(maxWordLen, len(word))

        dp = [False] * len(s)
        for i in range(minWordLen-1, len(s)):
            if i == minWordLen - 1:
                dp[i] = s[:i+1] in wordMap
            elif i < maxWordLen and s[:i+1] in wordMap:
                dp[i] = True
            else:
                j = i - minWordLen
                while j >= 0 and j >= i - maxWordLen:
                    if s[j+1:i+1] in wordMap and dp[j]:
                        dp[i] = True
                        break
                    j -= 1

        return dp[len(s)-1]

    def testWorkBreak(self):
        self.assertTrue(self.wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(self.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertFalse(self.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

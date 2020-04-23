import unittest
from typing import List

class Solution(unittest.TestCase):
    def partition(self, s: str) -> List[List[str]]:
        """
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
        if not s:
            return []

        ret = []

        def isPalindome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(s, track):
            if not s:
               ret.append(track)
            else:
                for i in range(len(s)):
                   sub, rest = s[:i+1], s[i+1:]
                   if isPalindome(sub):
                       backtrack(rest, track + [sub])

        backtrack(s, [])
        return ret

    def testPartition(self):
        self.assertCountEqual(self.partition("aab"), [['aa','b'],['a','a','b']])

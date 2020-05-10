import unittest
from collections import Counter

class Solution(unittest.TestCase):
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

---
Basic Idea: Sliding window. Valid: meet same chars with same times. Invalid: more chars or same chars but more times
"""
        l, r = 0, 0
        need = Counter(s1)
        meet = Counter()
        ret = False
        while r < len(s2):
            meet[s2[r]] += 1
            r += 1

            # meet more chars, or meet same chars but more times
            while len(meet) > len(need) or (len(meet) == len(need) and sum(meet.values()) > sum(need.values())):
                if meet[s2[l]] == 1:
                    del meet[s2[l]]
                else:
                    meet[s2[l]] -= 1
                l += 1

            if meet == need:
                return True

        return ret

    def testCheckInclusion(self):
        self.assertTrue(self.checkInclusion("adc", "dcda"))
        self.assertTrue(self.checkInclusion("ab", "eidbaooo"))
        self.assertFalse(self.checkInclusion("ab", "eidboaoo"))

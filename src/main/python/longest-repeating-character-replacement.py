import unittest
from collections import Counter

class Solution(unittest.TestCase):
    def characterReplacement(self, s: str, k: int) -> int:
        """
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

---
Basic Idea: Sliding window, if `sum(meet) - max(meet) > k`, means invalid.
"""
        if not s:
            return 0
        elif k >= len(s):
            return len(s)
        meet = Counter()
        l, r = 0, 0
        ret = -float('inf')
        while r < len(s):
            meet[s[r]] += 1
            # valid situation: max(meets) + <=k replace, when sum - max > k, means no way to valid
            while sum(meet.values()) - max(meet.values()) > k:
                meet[s[l]] -= 1
                l += 1
            r += 1
            ret = max(ret, r-l)
        return ret

    def testReplace(self):
        self.assertEqual(2, self.characterReplacement("ABCDE", 1))
        self.assertEqual(4, self.characterReplacement("AAAA", 0))
        self.assertEqual(4, self.characterReplacement("ABAB", 2))
        self.assertEqual(4, self.characterReplacement("AABABBA", 1))

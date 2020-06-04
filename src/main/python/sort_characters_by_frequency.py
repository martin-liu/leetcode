import unittest
from collections import Counter

class Solution(unittest.TestCase):
    def frequencySort(self, s: str) -> str:
        """
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
        d = {}
        for c, n in Counter(s).items():
            d[n] = d.get(n, []) + [c] * n

        res = ""
        for i in range(len(s), -1, -1):
            if i in d:
                res += "".join(d[i])
        return res

    def test(self):
        self.assertEqual("eetr", self.frequencySort("tree"))
        self.assertEqual("cccaaa", self.frequencySort("cccaaa"))
        self.assertEqual("bbAa", self.frequencySort("Aabb"))

import unittest
from typing import List

class Solution(unittest.TestCase):
    def letterCasePermutation(self, S: str) -> List[str]:
        """
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
        if not S:
            return []
        res, L = [], len(S)
        def backtrack(path):
            i = len(path)
            if i == L:
                res.append("".join(path))
            else:
                char = S[i]
                choices = [char] if char.isdigit() else [char.lower(), char.upper()]
                for c in choices:
                    backtrack(path + [c])
        backtrack([])
        return res

    def test(self):
        self.assertEqual(["a1b2", "a1B2", "A1b2", "A1B2"], self.letterCasePermutation("a1b2"))
        self.assertEqual(["3z4","3Z4"], self.letterCasePermutation("3z4"))
        self.assertEqual(["12345"], self.letterCasePermutation("12345"))

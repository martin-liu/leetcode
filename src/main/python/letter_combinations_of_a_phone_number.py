import unittest
from functools import reduce

class Solution(unittest.TestCase):
    def letterCombinations(self, digits):
        """
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
        """
        if not digits:
            return []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res, L = [], len(digits)
        def backtrack(i, s):
            if i == L:
                res.append(s)
            else:
                for c in m[digits[i]]:
                    backtrack(i+1, s+c)

        backtrack(0, "")
        return res

    def letterCombinations2(self, digits):
        if not digits:
            return []

        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        return reduce(lambda a, d: [x + y for x in a for y in m[d]], digits, [''])

    def test(self):
        self.assertCountEqual(self.letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self.assertCountEqual(self.letterCombinations2("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

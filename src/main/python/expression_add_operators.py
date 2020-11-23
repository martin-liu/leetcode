import unittest
from typing import List

class Solution(unittest.TestCase):
    def addOperators(self, num: str, target: int) -> List[str]:
        """
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

---
Basic Idea: backtrack, deal with 0 starting case
"""
        def backtracking(idx=0, path='', value=0, prev=None):
            if idx == len(num) and value == target:
                rtn.append(path)
                return

            # try each sub num
            for i in range(idx+1, len(num) + 1):
                sub = num[idx:i]
                tmp = int(sub)
                # allow '0' but no '0..'
                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    if prev is None :
                        backtracking(i, sub, tmp, tmp)
                    else:
                        backtracking(i, path+'+'+sub, value + tmp, tmp)
                        backtracking(i, path+'-'+sub, value - tmp, -tmp)
                        # * is special, need to undo pre operation, then apply new one
                        backtracking(i, path+'*'+sub, value - prev + prev*tmp, prev*tmp)

        rtn = []
        backtracking()

        return rtn

    def test(self):
        self.assertEqual([], self.addOperators(num = "3456237490", target = 9191))
        self.assertCountEqual(["1+2+3", "1*2*3"], self.addOperators(num = "123", target = 6))
        self.assertCountEqual(["2*3+2", "2+3*2"], self.addOperators(num = "232", target = 8))

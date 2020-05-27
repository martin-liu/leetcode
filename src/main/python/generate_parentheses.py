import unittest

class Solution(unittest.TestCase):
    def generateParenthesis(self, n):
        """
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
---
Basic Idea: Backtracking. Find each `(` in path, add '()' after it.
        """
        res = set()
        def backtrack(path):
            if len(path) == n * 2:
                res.add("".join(path))
            else:
                # always add one parenthesis
                backtrack(path + ['(',')'])
                for i, c in enumerate(path):
                    # add parenthesis after each `(`
                    if c == '(':
                        backtrack(path[:i+1] + ['(',')'] + path[i+1:])
        backtrack([])
        return list(res)

    def generateParenthesis2(self, n):
        """
Basic idea: to get f(n), need find all pairs of f(i) and f(n - i - 1), denote as [x, y], then combine them together with another `()`, using `(x)y` style
e.g. f2 -> (f0)f1 | f1(f0)
e.g. f3 -> (f0)f2 | (f1)f1 | (f2)f0
e.g. fn -> (f0)fn-1 | (f1)fn-2 | ... | (fn-1)f0
        """
        if n <= 0:
            return []
        elif n == 1:
            return ["()"]

        # n + 1 array
        dp = [[] for _ in range(n + 1)]
        # first is ['']
        dp[0].append('')

        for i in range(1, n + 1):
            # j is [0, i). For f(i), need to check all pairs that have total `i - 1` brackets
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i - j - 1]:
                        # x has j brackets, y has `i - j - 1` brackets, so that to get i brackets, just need to combine them together and add another `()`
                        dp[i].append('(' + x + ')' + y)
        return dp[-1]

    def test(self):
        self.assertCountEqual(self.generateParenthesis(3), [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ])

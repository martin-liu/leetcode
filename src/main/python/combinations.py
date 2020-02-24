import unittest
from typing import List

class Solution(unittest.TestCase):
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
 [2,4],
 [3,4],
 [2,3],
 [1,2],
 [1,3],
 [1,4],
]

---
Basic idea: f(n,k) = f(n-1,k) + [a + [n] for a in f(n-1,k-1)]
        """
        if n <= 0 or k <= 0 or n < k:
            return []
        if k == 1:
            return [[i+1] for i in range(n)]
        else:
            return self.combine(n-1, k) + [a + [n] for a in self.combine(n-1, k-1)]

    def combine2(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or n < k:
            return []

        ret = [[[] for _ in range(k)] for _ in range(n)]
        for i in range(n):
            for j in range(k):
                if i < j:
                    break
                if j == 0:
                    ret[i][j] = [[e+1] for e in range(i+1)]
                else:
                    ret[i][j] = ret[i-1][j] + [a + [i+1] for a in ret[i-1][j-1]]
        return ret[n-1][k-1]

    def testCombine(self):
        self.assertCountEqual(self.combine(0, 2), [])
        self.assertCountEqual(self.combine(2, 0), [])
        self.assertCountEqual(self.combine(2, 3), [])
        self.assertCountEqual(self.combine(4, 1), [[1], [2], [3], [4]])
        self.assertCountEqual(self.combine(4, 2), [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]])
        self.assertCountEqual(self.combine(4, 3), [[1,2,3], [1,2,4], [1,3,4], [2,3,4]])

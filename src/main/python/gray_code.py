import unittest
from typing import List

class Solution(unittest.TestCase):
    def grayCode(self, n: int) -> List[int]:
        """
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1

Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 2*0 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

---
Basic idea: f(n) = ['0'+c for c in f(n-1)] + ['1'+c for c in f(n-1).reverse()]
        """
        def genCode(n):
            if n == 0:
                return ['0']
            elif n == 1:
                return ['0', '1']
            pre = genCode(n-1)
            curr = pre[::-1] # reverse

            return ['0'+c for c in pre] + ['1'+c for c in curr]

        return list(map(lambda d: int(d, 2), genCode(n)))

    def testGrayCode(self):
        self.assertCountEqual(self.grayCode(0), [0])
        self.assertCountEqual(self.grayCode(1), [0,1])
        self.assertCountEqual(self.grayCode(2), [0,1,3,2])

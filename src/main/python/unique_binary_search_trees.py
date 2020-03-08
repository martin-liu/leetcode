import unittest

class Solution(unittest.TestCase):
        def numTrees(self, n: int) -> int:
            """
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

----
number of trees only determined by length.
if i is root, then left length is `i-1`(less then i), right length is `n-i` (greater than i)
use each i from 1..n as root, f(i-1)*f(n-i) is the types' number

Basic idea: f(n) = sum([f(i-1) * f(n-i) for i in range(1,n+1)])
            """
            if n < 1:
                return 0

            nums = [1] * (n+1)
            for i in range(2, n+1):
                nums[i] = sum([nums[j-1] * nums[i-j] for j in range(1,i+1)])

            return nums[n]

        def testNumTrees(self):
            self.assertEqual(self.numTrees(0), 0)
            self.assertEqual(self.numTrees(1), 1)
            self.assertEqual(self.numTrees(2), 2)
            self.assertEqual(self.numTrees(3), 5)
            self.assertEqual(self.numTrees(4), 14)
            self.assertEqual(self.numTrees(5), 42)
            self.assertEqual(self.numTrees(6), 132)
            self.assertEqual(self.numTrees(7), 429)

import unittest
from typing import List

class Trie:
    def __init__(self, val = None):
        # 0
        self.left = None
        # 1
        self.right = None
        self.val = val

    def insertBinary(self, b):
        if b == 0:
            # insert when not exist
            self.left = self.left or Trie()
            return self.left
        else:
            # insert when not exist
            self.right = self.right or Trie()
            return self.right

    def insert(self, num):
        curr = self
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            curr = curr.insertBinary(bit)

        curr.val = num

class Solution(unittest.TestCase):
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2^31.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

-----
Basic Idea: Build Trie (32 bit from high to low), then iterate nums and found maximum
        In each round, check from high bit to low bit, 1 -> 0 or 1, 0 -> 1 or 0
"""
        trie = Trie()
        for n in nums:
           trie.insert(n)

        res = -float('inf')
        for n in nums:
            curr = trie
            for i in range(31, -1, -1):
                bit = (n >> i) & 1
                # when 0, try 1 or 0; when 1, try 0 or 1. (or for fallback)
                curr = curr.right or curr.left if bit == 0 else curr.left or curr.right

            res = max(res, n ^ curr.val)

        return res

    def findMaximumXOR2(self, nums: List[int]) -> int:
        """
        Use bit to bit check from left to right (high to low)
        """
        res = 0
        for i in range(31, -1, -1):
            # add one bit 0 to res
            res <<= 1
            # find all prefix (32 - i) bits of each num
            prefixes = [n >> i for n in nums]
            # res^1 is to make last one bit to 1 since previouly add 0
            # if we can find a q which p ^ q = res^1, means current max can be `res^1`
            # res^1 = p ^ q, and p ^ q ^ p = q, here check if q in prefixes, if yes, means we find a q, res += 1
            res += any(res^1 ^ p in prefixes for p in prefixes)
        return res

    def test(self):
        self.assertEqual(28, self.findMaximumXOR([3,10,5,25,2,8]))
        self.assertEqual(28, self.findMaximumXOR2([3,10,5,25,2,8]))

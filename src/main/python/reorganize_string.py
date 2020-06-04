import unittest
from heapq import heapify, heappush, heappop
from collections import Counter

class Solution(unittest.TestCase):
    def reorganizeString(self, S: str) -> str:
        """
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

Basic Idea: always append current max freq one, then current second max one, then max one, then second max, repeat
        Use Heap. Keep pop and push `previous one`, so that poped one will not exist in next round, but can back in next next round. Hence we have non adjacent same character.
"""
        heap = [(-v,k) for k,v in Counter(S).items()]
        heapify(heap)

        res = []
        preN, preC = 0, ''
        while heap:
            # pop, so that current one will never use in next round
            n, c = heappop(heap)
            res.append(c)
            # push previous one, so that it can back in next round (it maybe or not be next one depends on freq)
            if preN < 0:
                heappush(heap, (preN, preC))
            preN, preC = n+1, c
        res = "".join(res)
        return res if len(res) == len(S) else ""

    def test(self):
        self.assertEqual("aba", self.reorganizeString("aab"))
        self.assertEqual("", self.reorganizeString("aaab"))
        self.assertEqual("vlvov", self.reorganizeString("vvvlo"))
        self.assertEqual("ababababab", self.reorganizeString("abbabbaaab"))

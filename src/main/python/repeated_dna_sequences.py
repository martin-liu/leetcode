import unittest
from typing import List

class Solution(unittest.TestCase):
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
        """
        if len(s) < 10:
            return []
        counter = {}
        ret = []
        for i in range(len(s)-9):
            curr = s[i:i+10]
            if curr not in counter:
                counter[curr] = 1
            else:
                counter[curr] += 1
                if counter[curr] == 2:
                    ret.append(curr)

        return ret


    def testFind(self):
        self.assertEqual(["AAAAACCCCC", "CCCCCAAAAA"], self.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

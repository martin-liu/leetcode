import unittest
from typing import List

class Solution(unittest.TestCase):
    def minKBitFlips(self, A: List[int], K: int) -> int:
        """
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]

Note:

1 <= A.length <= 30000
1 <= K <= A.length

---
Basic Idea: use an array to store flip status of positions, if A[i] == 0 and flipped even times, need flip; if A[i] == 1 and flipped odd times, need flip, because it's 1 and we flipped it odd times, so now it's 0 and need to flip it again.

So that when A[i] == flipped % 2, need flip

A[i] may impact by i-K+1 until i-1, because it's K bits flip, so if even number of flip happend to A[i], flipped = 0, if odd number, flipped = 1
        """
        isFlipped = [0] * len(A)
        flipped = ret = 0
        for i in range(len(A)):
            if i >= K:
                # from `i-K+1` until `i-1`, there may be multiple flips which impact `i` (K bits)
                # when `isFlipped[i-K] == 1`, need to decrease flipped, because `i-K` will not impact `i`, so flipped numbers that will impact current i is `flipped - 1`
                if isFlipped[i-K]:
                    flipped -= 1

            # even with 0, or odd with 1, need to flip
            if flipped % 2 == A[i]:
                # need flip but no space to flip K bits, means no way to ensure all 1
                if (i + K > len(A)):
                    return -1
                isFlipped[i] = 1
                flipped += 1 # flipped how many times
                ret += 1

        return ret

    def testMinKBitFlips(self):
        self.assertEqual(2, self.minKBitFlips([0,1,0], 1))
        self.assertEqual(-1, self.minKBitFlips([1,1,0], 2))
        self.assertEqual(3, self.minKBitFlips([0,0,0,1,0,1,1,0], 3))

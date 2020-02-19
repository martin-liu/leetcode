import unittest

class Solution(unittest.TestCase):
    def getPermutation(self, n: int, k: int) -> str:
        """
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

---
Basic idea:

Say n = 4, k = 9, you have {1, 2, 3, 4}

If you were to list out all the permutations you have

1 + p(2, 3, 4)

2 + p(1, 3, 4)

3 + p(1, 2, 4)

4 + p(1, 2, 3)

so 9th = `2 + 3th of p(1,3,4)` = `2 + 3 + 1th of p(1,4)` = `2314`

To code it, we do `nums=[1,2,3,4]`, `k=k-1`, `q,k=divmod(8,6)=1,2`, choose `nums[1]=2`, then remove 2 from nums, `nums=[1,3,4]`. Repeat.
        """
        if n == 0 or k == 0:
            return ""

        nums = [i + 1 for i in range(n)]

        permNum = 1
        for i in range(n):
            permNum *= (i + 1)

        ret = []

        # subtract 1 because the natural of div and mod
        # e.g. `0..5 // 6 = 0`, while `6 // 6 = 1`. So that first 6 elements can only group together if starting at `0`
        # `k=k-1` ensure the divmod works well to group elements
        k = k - 1
        for i in range(n, 0, -1):
            permNum //= i # using previous total perm num
            q, k = divmod(k, permNum)
            ret.append(nums[q])
            # remove used number, next time will choosing from remaining numbers, which exactly mapping to the permutations.
            nums.pop(q)

        return "".join(map(str, ret))

    def testPermutation(self):
        self.assertEqual(self.getPermutation(1, 1), "1")
        self.assertEqual(self.getPermutation(2, 1), "12")
        self.assertEqual(self.getPermutation(2, 2), "21")
        self.assertEqual(self.getPermutation(3, 3), "213")
        self.assertEqual(self.getPermutation(3, 4), "231")
        self.assertEqual(self.getPermutation(4, 9), "2314")

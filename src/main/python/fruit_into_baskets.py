import unittest
from typing import List
from collections import Counter

class Solution(unittest.TestCase):
    def totalFruit(self, tree: List[int]) -> int:
        """
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length

--
Basic Idea: windowing, valid: meet only 2 types
"""
        if not tree:
            return 0

        l = r = ret = 0
        meet = Counter()
        while r < len(tree):
            meet[tree[r]] += 1
            r += 1

            while len(meet) > 2:
                if meet[tree[l]] == 1:
                    del meet[tree[l]]
                else:
                    meet[tree[l]] -= 1
                l += 1

            ret = max(ret, r-l)

        return ret

    def testFruit(self):
        self.assertEqual(3, self.totalFruit([1,2,1]))
        self.assertEqual(3, self.totalFruit([0,1,2,2]))
        self.assertEqual(4, self.totalFruit([1,2,3,2,2]))
        self.assertEqual(5, self.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

import unittest
from typing import List

class Solution(unittest.TestCase):
    def maxProfit(self, prices: List[int]) -> int:
        """
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

        """
        if not prices:
            return 0
        nums = [0] * len(prices)
        ret = 0
        for i in range(len(prices)):
            if i == 0:
                nums[i] = (prices[i], prices[i])
            else:
                l, r = nums[i-1]
                if prices[i] < l:
                    nums[i] = (prices[i], prices[i])
                elif prices[i] > r:
                    nums[i] = (l, prices[i])
                else:
                    nums[i] = (l, r)
                ret = max(ret, nums[i][1] - nums[i][0])
        return ret

    def testMaxProfix(self):
        self.assertEqual(5, self.maxProfit([7,1,5,3,6,4]))
k       self.assertEqual(0, self.maxProfit([7,6,4,3,1]))

import unittest
from typing import List

class Solution(unittest.TestCase):
    def candy(self, ratings: List[int]) -> int:
        """
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

---
Basic Idea:
        1. When keep same priority or in init state, only need one candy until change
        2. When keep going up, from start point, it should have [1,2,3,..] candies
        3. When keep going down, from start point, it should greater than next one.
           a) Need to check candies in start point, because it may not 1 when previous state is UP.
           b) e.g if startCandy is 3, then keep down will cause [3, 1] -> [3, 2, 1] -> [4, 3, 2, 1] -> ...
"""
        if not ratings:
            return 0
        elif len(ratings) == 1:
            return 1

        # True: down, False: up, None: not init or flat
        isDown = None
        start = -1
        ret = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                if isDown is None or isDown:
                    # chang to up
                    isDown = False
                    start = i - 1
                ret += i - start + 1
            elif ratings[i] == ratings[i-1]:
                # give one candy and back to init state
                isDown = None
                ret += 1
            else:
                if isDown is None or not isDown:
                    # how many candy at start point
                    startCandy = 1 if isDown is None else i - start
                    # chang to down
                    isDown = True
                    start = i - 1
                if startCandy > i - start:
                    # if startCandy greater than next one, then no need to increase at start point
                    ret += i - start
                else:
                    # otherwise start point also need to increase
                    ret += i - start + 1
        return ret

    def testCandy(self):
        self.assertEqual(5, self.candy([1,0,2]))
        self.assertEqual(4, self.candy([1,2,2]))
        self.assertEqual(6, self.candy([1,2,3]))
        self.assertEqual(7, self.candy([1,2,0,5,3]))
        self.assertEqual(7, self.candy([1,3,2,2,1]))

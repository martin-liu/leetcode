import unittest

class Solution(unittest.TestCase):
    def superEggDrop(self, K: int, N: int) -> int:
        """
You are given K eggs, and you have access to a building with N floors from 1 to N.
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N).
Your goal is to know with certainty what the value of F is.
What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

Example 1:
Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.

Example 2:
Input: K = 2, N = 6
Output: 3

Example 3:
Input: K = 3, N = 14
Output: 4

Note:
1 <= K <= 100
1 <= N <= 10000

----
        dp[M][K] means that, given K eggs and M moves,
        what is the maximum number of floor that we can check.

        The dp equation is:
        dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
        which means we take 1 move to a floor,
        if egg breaks, then we can check dp[m - 1][k - 1] floors.
        if egg doesn't breaks, then we can check dp[m - 1][k] floors.
"""
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N:
                return m

    def superEggDrop2(self, K: int, N: int) -> int:
        """
Basic idea: DP
        min of *worst case*
        if broken in floor j, then only need to consider N-j floors; otherwise only need to consider j-1 floors
        state: egg num K, floor num N
        base: f(0,N) = f(K,0) = 0
        definition:
          f(K,N) = max(f(K,N-j), f(K-1, j-1))
"""
        cache = {}
        def dp(K,N):
            if K == 0 or N == 0:
                return 0
            if K == 1:
                return N

            if (K,N) in cache:
                return cache[(K,N)]

            res = float('inf')
            for i in range(1, N+1):
                # either broken or not broken, +1 anyway
                res = min(res, 1 + max(dp(K, N-i), dp(K-1, i-1)))

            cache[(K,N)] = res
            return res

        return dp(K, N)


    def test(self):
        self.assertEqual(2, self.superEggDrop(1, 2))
        self.assertEqual(3, self.superEggDrop(2, 6))
        self.assertEqual(4, self.superEggDrop(3, 14))

# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 62-Unique Paths.py
@time: 2020/8/19 15:38
@desc:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?



Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9
"""

import math


class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     因为机器到底右下角，向下几步，向右几步都是固定的，
    #
    #     比如，m=3, n=2，我们只要向下 1 步，向右 2 步就一定能到达终点。
    #
    #     所以有 C_{m+n-2}^{m-1}C
    #     """
    #     return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(4, 5))
# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents. (The result may be large, so you should return it modulo 1000000007)
#
# Example1:
#
#  Input: n = 5
#  Output: 2
#  Explanation: There are two ways:
# 5=5
# 5=1+1+1+1+1
# Example2:
#
#  Input: n = 10
#  Output: 4
#  Explanation: There are four ways:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
# Notes:
#
# You can assume:
#
# 0 <= n <= 1000000


class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins = [1, 5, 10, 25]
        return self.change(n, coins) % 1000000007

    def change(self, amount, coins):
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # dp[i][j]的含义：
        # j代表所需要金额
        # i代表选到几种硬币，如i=0代表一种硬币都不用，i=1代表用coins[:1]类硬币（即只用coins[0]）,i=2代表用coins[:2]类硬币（即只用coins[0],coins[1]）,以此类推
        # 初始化状态
        for c in range(1, amount + 1):
            dp[0][c] = 0
        for r in range(len(coins) + 1):
            dp[r][0] = 1
        for r in range(1, len(coins) + 1):
            for c in range(1, amount + 1):
                dp[r][c] = dp[r - 1][c]
                if c - coins[r - 1] >= 0:
                    dp[r][c] += dp[r][c - coins[r - 1]]
        return dp[-1][-1]

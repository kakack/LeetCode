# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 714-Best Time to Buy and Sell Stock with Transaction Fee.py
@time: 2020/12/17 9:29
@desc:
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

每天交易结束后只可能存在手里有一支股票或者没有股票的状态。

定义状态 dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润，
dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始）。

状态转移方程：
dp[i][0]=max{dp[i−1][0],dp[i−1][1]+prices[i]−fee}
dp[i][1]=max{dp[i−1][1],dp[i−1][0]−prices[i]}

初始化
dp[0][0]=0 以及 dp[0][1]=−prices[0]



"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)

        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 188-Best Time to Buy and Sell Stock IV.py
@time: 2020/12/28 10:13
@desc:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 109
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

buy[i][j]表示对于数组 prices[0..i] 中的价格而言，第i天进行恰好 j 笔交易，并且当前手上持有一支股票，这种情况下的最大利润；
用 sell[i][j] 表示第i天恰好进行 j 笔交易，并且当前手上不持有股票，这种情况下的最大利润。
转移方程：
buy[i][j] = max{buy[i-1][j], sell[i-1][j] - prices[i]}
sell[i][j] = max{sell[i-1][j], buy[i-1][j-1] + prices[i]}

最终答案max{sell[n-1][0...k]}

初始状态:
buy[0][1..k]和sell[0][1...k]设置一个极小值 buy[0][0]=-prices[0], sell[0][0] = 0
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        k = min(k, n // 2)

        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        buy[0][0], sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")
        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
        return max(sell[n - 1])

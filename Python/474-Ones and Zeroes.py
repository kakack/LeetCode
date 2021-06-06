# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 474-Ones and Zeroes.py
@time: 2021/6/6 12:08 上午
@desc:
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.



Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.


Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        Len = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(Len + 1)]
        for k in range(1, Len + 1):
            cnt0 = strs[k - 1].count('0')
            cnt1 = strs[k - 1].count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[k][i][j] = dp[k - 1][i][j]  # 继承
                    if i - cnt0 >= 0 and j - cnt1 >= 0:  # 可更新则更新
                        dp[k][i][j] = max(dp[k][i][j], dp[k - 1][i - cnt0][j - cnt1] + 1)

        return dp[Len][m][n]


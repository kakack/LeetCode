# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 410-Split Array Largest Sum.py
@time: 2020/7/25 9:27
@desc:
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

"""
f[i][j]表示将数组的前i个数分割为j段所能得到的最大连续子数组的最小值；
考虑第j段的具体范围，枚举k，其中前k个数被分割为j-1段，而第k+1到第i个数位第j段；
sub(i, j)表示数组nums中下标落在区间[i, j]内数的和

"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        return f[n][m]


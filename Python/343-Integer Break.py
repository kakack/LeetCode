# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 343-Integer Break.py
@time: 2020/7/30 11:32
@desc:
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n - 1 if n < 4 else 3 ** (n // 3 - 1) * {3: 3, 4: 4, 5: 6}[(n - (n // 3 - 1) * 3)]

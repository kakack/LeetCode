# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 483-Smallest Good Base.py
@time: 2021/6/18 11:34
@desc:
Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.



Example 1:

Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:

Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:

Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.


Constraints:

n is an integer in the range [3, 1018].
n does not contain any leading zeros.
"""
import math


class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        for m in range(num.bit_length(), 2, -1):
            x = int(pow(num, 1.0 / (m - 1)))
            if num == (pow(x, m) - 1) // (x - 1):
                return str(x)
        return str(num - 1)

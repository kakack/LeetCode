# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 738-Monotone Increasing Digits.py
@time: 2020/12/15 9:04
@desc:
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        strN = str(N)
        for i in range(1, len(strN)):
            if strN[i - 1] > strN[i]:
                break
            else:
                return int(strN)

        for j in range(i - 1, 0, -1):
            if strN[j - 1] < strN[j] and strN[j] > '0':
                break
            else:
                j = 0
        return int(strN[:j] + chr(ord(strN[j]) - 1) + '9' * (len(strN) - j - 1))

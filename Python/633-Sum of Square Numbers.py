# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 633-Sum of Square Numbers.py
@time: 2021/4/28 10:54
@desc:
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true


Constraints:

0 <= c <= 231 - 1

"""

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            sum = left * left + right * right
            if sum == c:
                return True
            elif sum < c:
                left += 1
            else:
                right -= 1
        return False

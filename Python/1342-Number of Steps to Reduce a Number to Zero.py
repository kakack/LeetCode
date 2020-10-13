# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1342-Number of Steps to Reduce a Number to Zero.py
@time: 2020/10/13 9:19
@desc:
"""
class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
            if num % 2 == 1:
                count += 1
                num -= 1
            else:
                num = num // 2
                count += 1
        return count
# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1470-Shuffle the Array.py
@time: 2020/9/19 10:28
@desc:
"""


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        for i in range(n/2):
            res.append(nums[i])
            res.append(nums[i + n/2])
        return res

# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 剑指 Offer 53 - I. 在排序数组中查找数字 I.py
@time: 2021/7/16 10:56
@desc:
/*
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000

*/
"""
from collections import Counter

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return Counter(nums)[target]
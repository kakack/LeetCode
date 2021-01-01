# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 605-Can Place Flowers.py
@time: 2021/1/1 3:57 下午
@desc:

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        target = 0
        m = len(flowerbed)
        if m == 1:
            if flowerbed[0] == 0:
                return 1 >= n
            else:
                return 0 >= n

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            target = 1
            flowerbed[0] = 1


        for i in range(1, m - 1):
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    target += 1
                    flowerbed[i] = 1
        if flowerbed[-1] == flowerbed[-2] == 0:
            target += 1
        return target >= n

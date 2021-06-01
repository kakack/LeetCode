# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1744-Can You Eat Your Favorite Candy on Your Favorite Day.py
@time: 2021/6/1 10:34
@desc:
"""


class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # 前缀和
        total = list(accumulate(candiesCount))

        ans = list()
        for favoriteType, favoriteDay, dailyCap in queries:
            x1 = favoriteDay + 1
            y1 = (favoriteDay + 1) * dailyCap
            x2 = 1 if favoriteType == 0 else total[favoriteType - 1] + 1
            y2 = total[favoriteType]

            ans.append(not (x1 > y2 or y1 < x2))

        return ans


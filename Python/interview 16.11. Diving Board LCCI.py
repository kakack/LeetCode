# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: interview 16.11. Diving Board LCCI.py
@time: 2020/7/8 15:22
@desc:
You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of planks, one of length shorter and one of length longer. You must use exactly K planks of wood. Write a method to generate all possible lengths for the diving board.

return all lengths in non-decreasing order.

Example:

Input:
shorter = 1
longer = 2
k = 3
Output:  {3,4,5,6}
Note:

0 < shorter <= longer
0 <= k <= 100000

"""

class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        elif longer == shorter:
            return [k * shorter]
        res = []
        for i in range(k + 1):
            res.append(shorter * (k - i) + longer * i)
        return res

# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: interview16.01. 交换数字.py
@time: 2020/10/2 10:06 下午
@desc:
编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。

示例：
输入: numbers = [1,2]
输出: [2,1]
提示：

numbers.length == 2

"""


class Solution(object):
    def swapNumbers(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        # numbers[:] = numbers[::-1]
        # return numbers
        return numbers[::-1]

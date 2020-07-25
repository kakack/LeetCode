# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: interview17.01. 不用加号的加法.py
@time: 2020/7/25 10:32
@desc:
设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数

"""


class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        elif b == 0:
            return a
        return self.add((a & b) << 1, a ^ b)


if __name__ == '__main__':
    s = Solution()
    print(s.add(4, 7))

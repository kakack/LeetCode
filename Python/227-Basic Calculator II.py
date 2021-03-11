# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 227-Basic Calculator II.py
@time: 2021/3/11 9:28
@desc:
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = []
        num, sign = 0, "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            if c in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stk.append(num)
                elif sign == '-':
                    stk.append(-num)
                elif sign == '*':
                    stk[-1] *= num
                elif sign == '/':
                    stk[-1] = int(stk[-1] / float(num))
                num, sign = 0, c
        return sum(stk)

# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 224-Basic Calculator.py
@time: 2021/3/10 10:52
@desc:
Given a string s representing an expression, implement a basic calculator to evaluate it.



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops = [1]
        sign, ret, n, i = 1, 0, len(s), 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and ord('0') <= ord(s[i]) <= ord('9'):
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += sign * num
        return ret

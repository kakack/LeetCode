# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 32-Longest Valid Parentheses.py
@time: 2020/7/4 11:19 上午
@desc:

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, last = 0, -1
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        res = max(res, i - last)
                    else:
                        res = max(res, i - stack[-1])
        return res


if __name__ == '__main__':
    inputs = ["(()", "()", "(())"]
    s = Solution()
    for inp in inputs:
        print(s.longestValidParentheses(inp))

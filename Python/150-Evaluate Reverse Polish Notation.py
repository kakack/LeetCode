# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 150-Evaluate Reverse Polish Notation.py
@time: 2021/3/20 11:07 上午
@desc:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.



Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = ["+", "-", "*", "/"]
        stk = []
        for token in tokens:
            if token in operations:
                tmp2 = stk[-1]
                tmp1 = stk[-2]
                stk.pop()
                stk.pop()
                if token == "+":
                    stk.append(tmp1 + tmp2)
                elif token == "-":
                    stk.append(tmp1 - tmp2)
                elif token == "*":
                    stk.append(tmp1 * tmp2)
                else:
                    stk.append(int(tmp1 / float(tmp2)))
            else:
                stk.append(int(token))
        return stk[-1]


if __name__ == '__main__':
    s = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(s.evalRPN(tokens))


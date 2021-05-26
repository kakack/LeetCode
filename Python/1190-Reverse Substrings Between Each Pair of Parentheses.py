# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1190-Reverse Substrings Between Each Pair of Parentheses.py
@time: 2021/5/26 9:40
@desc:
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.



Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"


Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
"""


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk, str = [], ""
        for ch in s:
            if ch == '(':
                stk.append(str)
                str = ''
            elif ch == ')':
                str = stk.pop(-1) + str[::-1]
            else:
                str = str + ch
        return str


if __name__ == '__main__':
    str = "12345"
    print

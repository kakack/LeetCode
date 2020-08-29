# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 214-Shortest Palindrome.py
@time: 2020/8/29 10:12
@desc:
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        base, mod = 131, 10 ** 9 + 7
        left = right = 0
        mul, best = 1, -1
        for i in range(n):
            left = (left * base + ord(s[i])) % mod
            right = (right + mul * ord(s[i])) % mod
            if left == right:
                best = i
            mul = mul * base % mod
        add = ("" if best == n - 1 else s[best + 1:])
        return add[::-1] + s

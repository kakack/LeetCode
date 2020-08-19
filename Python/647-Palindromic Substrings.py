# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 647-Palindromic Substrings.py
@time: 2020/8/19 14:49
@desc:
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, res = len(s), 0
        for i in range(2 * n - 1):
            l = i / 2
            r = i / 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res

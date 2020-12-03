# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1081-Smallest Subsequence of Distinct Characters.py
@time: 2020/12/3 11:14
@desc:
Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

和 316 相同
"""

import collections

class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        counts = collections.Counter(s)

        for c in s:
            if c not in letters:
                while letters and c < letters[-1] and counts[letters[-1]] > 0:
                    letters.pop()
                letters.append(c)
            counts[c] -= 1
        return "".join(letters)
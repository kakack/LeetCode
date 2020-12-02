# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 316-Remove Duplicate Letters.py
@time: 2020/12/2 11:56
@desc:

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""

import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
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

# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 567-Permutation in String.py
@time: 2021/2/10 9:28
@desc:
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n > m:
            return False
        cnt1, cnt2 = [0] * 26, [0] * 26
        for i in range(n):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1
        if cnt1 == cnt2:
            return True
        for i in range(n, m):
            cnt2[ord(s2[i]) - ord('a')] += 1
            cnt2[ord(s2[i - n]) - ord('a')] -= 1
            if cnt1 == cnt2:
                return True
        return False

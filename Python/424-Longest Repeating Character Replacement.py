# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 424-Longest Repeating Character Replacement.py
@time: 2021/2/2 9:03
@desc:
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0
        while right < n:
            num[ord(s[right]) - ord('A')] += 1
            maxn = max(maxn, num[ord(s[right]) - ord('A')])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord('A')] -= 1
                left += 1
            right += 1
        return right - left

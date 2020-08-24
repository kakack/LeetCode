# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 459-Repeated Substring Pattern.py
@time: 2020/8/24 9:05
@desc:
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        left_str = s[left]
        while left < len(s) / 2:
            if left_str * (len(s) // len(left_str)) == s:
                return True
            else:
                left += 1
                left_str = left_str + s[left]
        return False


if __name__ == '__main__':
    s = Solution()
    for ipt in ["abab", "aba", "abcabcabcabc"]:
        print(s.repeatedSubstringPattern(ipt))

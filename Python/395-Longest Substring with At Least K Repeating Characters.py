# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 395-Longest Substring with At Least K Repeating Characters.py
@time: 2021/2/27 8:30
@desc:
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret, n = 0, len(s)
        for i in range(1, 27):
            l, r = 0, 0
            cnt = [0] * 26
            tot, less = 0, 0
            while r < n:
                cnt[ord(s[r]) - ord('a')] += 1
                if cnt[ord(s[r]) - ord('a')] == 1:
                    tot += 1
                    less += 1
                if cnt[ord(s[r]) - ord('a')] == k:
                    less -= 1
                while tot > i:
                    cnt[ord(s[l]) - ord('a')] -= 1
                    if cnt[ord(s[l]) - ord('a')] == (k - 1):
                        less += 1
                    if cnt[ord(s[l]) - ord('a')] == 0:
                        tot -= 1
                        less -= 1
                    l += 1
                if less == 0:
                    ret = max(ret, r - l + 1)
                r += 1
        return ret



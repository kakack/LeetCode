# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 763-Partition Labels.py
@time: 2020/10/22 11:15
@desc:
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord('a')] = i
        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord('a')])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        return partition

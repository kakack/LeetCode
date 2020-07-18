# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 97-Interleaving String.py
@time: 2020/7/18 11:15 上午
@desc:
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        boolean = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        boolean[0][0] = True
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                p = i + j - 1
                if i > 0:
                    boolean[i][j] = boolean[i][j] or (boolean[i - 1][j] and s1[i - 1] == s3[p])
                if j > 0:
                    boolean[i][j] = boolean[i][j] or (boolean[i][j - 1] and s2[j - 1] == s3[p])
        return boolean[n1][n2]


if __name__ == '__main__':
    s = Solution()
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    # print(s.isInterleave(s1, s2, s3))
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbbaccc"
    # print(s.isInterleave(s1, s2, s3))
    s1 = "db"
    s2 = "b"
    s3 = "cbb"
    print(s.isInterleave(s1, s2, s3))
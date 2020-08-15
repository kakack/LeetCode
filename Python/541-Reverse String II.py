# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 541-Reverse String II.py
@time: 2020/8/15 10:24 下午
@desc:
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n, i = len(s), 0
        tmp = []
        reverse = True
        while i + k <= n:
            if reverse:
                for c in reversed(s[i:i+k]):
                    tmp.append(c)
            else:
                print(s[i:i + k])
                for c in s[i:i + k]:
                    tmp.append(c)
            i += k
            reverse = not reverse
        if reverse:
            for c in reversed(s[i:]):
                tmp.append(c)
        else:
            for c in s[i:]:
                tmp.append(c)
        return "".join(tmp)



    def reverseStr2(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr2("abcdefg", 2))

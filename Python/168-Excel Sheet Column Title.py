# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 168-Excel Sheet Column Title.py
@time: 2020/7/27 10:07
@desc:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        res = []
        while n > 0:
            n -= 1
            c = n % 26
            res.insert(0, Alphabet[c])
            n = n // 26
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(28))

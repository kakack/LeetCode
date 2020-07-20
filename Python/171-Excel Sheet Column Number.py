# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 171-Excel Sheet Column Number.py
@time: 2020/7/20 9:59
@desc:
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            c = ord(s[i])
            res = 26 * res + (c - ord('A') + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    ipts = ['A', 'B', 'C', 'AB', 'BCD', 'ZY']
    for ipt in ipts:
        print(s.titleToNumber(ipt))

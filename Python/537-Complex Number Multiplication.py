# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 537-Complex Number Multiplication.py
@time: 2020/8/23 10:58 上午
@desc:
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
"""


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_t, a_f = int(a.split('+')[0]), int(a.split('+')[1].split('i')[0])
        b_t, b_f = int(b.split('+')[0]), int(b.split('+')[1].split('i')[0])
        res_t, res_f = a_t * b_t - a_f * b_f, a_t * b_f + a_f * b_t
        return str(res_t) + "+" + str(res_f) + "i"


if __name__ == '__main__':
    s = Solution()
    for a, b in [("1+1i", "1+1i"), ("1+-1i", "1+-1i"), ("1+-2i", "3+-4i")]:
        print(s.complexNumberMultiply(a, b))

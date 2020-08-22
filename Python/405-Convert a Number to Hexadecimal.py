# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 405-Convert a Number to Hexadecimal.py
@time: 2020/8/22 8:51 下午
@desc:
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        remainder = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        res = []
        max_arg = 16 ** 8
        if num == 0:
            return '0'
        elif num < 0:
            num = max_arg + num
        while num > 0:
            res.append(remainder[num % 16])
            num = num // 16
        return ''.join(reversed(res))


if __name__ == '__main__':
    s = Solution()
    print(s.toHex(26))
    print(s.toHex(-2))

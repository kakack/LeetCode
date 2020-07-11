# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 344-Reverse String.py
@time: 2020/7/8 10:04 下午
@desc:
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
        print(s)


if __name__ == '__main__':
    s = Solution()
    s.reverseString(["h", "e", "l", "l", "o"])
    s.reverseString(["H", "a", "n", "n", "a", "h"])

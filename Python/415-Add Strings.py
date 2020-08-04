# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 415-Add Strings.py
@time: 2020/8/3 9:33
@desc:
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

1-The length of both num1 and num2 is < 5100.
2-Both num1 and num2 contains only digits 0-9.
3-Both num1 and num2 does not contain any leading zero.
4-You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def add(char1, char2, carryIn):
            digit1 = ord(char1) - ord('0') if char1 else 0
            digit2 = ord(char2) - ord('0') if char2 else 0
            return str((digit1 + digit2 + carryIn) % 10), (digit1 + digit2 + carryIn) // 10

        n1, n2 = len(num1), len(num2)
        if n1 > n2:
            n = n1
            num2 = '0' * (n1 - n2) + num2
        else:
            n = n2
            num1 = '0' * (n2 - n1) + num1
        carry = 0
        res = []
        for i in range(-1, -n - 1, -1):
            resDigit, carry = add(num1[i], num2[i], carry)
            res.insert(0, resDigit)
        if carry > 0:
            res.insert(0, str(carry))
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    nums1 = "569"
    nums2 = "71233"
    print(s.addStrings(nums1, nums2))
    # for i in range(-1, -len(nums1) - 1, -1):
    #     print(nums1[i])

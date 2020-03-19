# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
# Input:
# "abccccdd"
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap = {}
        for item in s:
            if hashMap.get(item) is not None:
                hashMap[item] += 1
            else:
                hashMap[item] = 1

        carry = 0
        res = 0
        for value in hashMap.values():
            if value % 2 == 0:
                res += value
            else:
                res += value - 1
                carry = 1
        return res + carry
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
# Example:

# Input: "cbbd"

# Output: "bb"

# 从中间朝两边依次比较

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        max_len = 0
        for i in xrange(len(s)):
            tmp = self.palindrome(s, i, i)
            if len(tmp) >= max_len:
                res = tmp
                max_len = len(tmp)
            tmp = self.palindrome(s, i, i + 1)
            if len(tmp) >= max_len:
                res = tmp
                max_len = len(tmp)
        return res

    def palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j]

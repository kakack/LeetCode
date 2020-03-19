# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
#
# Example 2:
# Input: "abca"
# Output: True
#
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def Palindrome(s):
            first, second = 0, len(s) - 1
            while first < second:
                if s[first] != s[second]:
                    return False
                first += 1
                second -= 1
            return True

        fir, sec = 0, len(s) - 1
        while s[fir] == s[sec] and fir < sec:
            fir += 1
            sec -= 1
        if fir < sec:
            return Palindrome(s[fir:sec]) or Palindrome(s[fir + 1:sec + 1])
        else:
            return True
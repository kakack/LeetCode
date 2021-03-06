# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
# Example 2:
# Input: "race a car"
# Output: false

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        deque = []
        for char in s:
            if char.isalpha() or char.isdigit():
                deque.append(char.lower())
        while len(deque) > 1:
            if deque.pop(0) != deque.pop(-1):
                return False
        return True
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
# Example 3:
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
# Example 4:
# Input: S = "a#c", T = "b"
# Output: false
#
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# - 1 <= S.length <= 200
# - 1 <= T.length <= 200
# - S and T only contain lowercase letters and '#' characters.
#
# Follow up:
# Can you solve it in O(N) time and O(1) space?

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def result(S):
            stack = []
            for char in S:
                if char == '#' and len(stack) > 0:
                    stack.pop(-1)
                elif char != '#':
                    stack.append(char)
            res = ''
            for char in stack:
                res += char
            return res

        return True if result(S) == result(T) else False
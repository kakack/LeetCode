# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s += ' '
        stack = []
        res = ''
        for item in s:
            if item == ' ':
                for char in reversed(stack):
                    res += char
                res += ' '
                stack = []
            else:
                stack.append(item)

        return res[0: -1]

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
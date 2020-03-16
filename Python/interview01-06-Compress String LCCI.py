# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
#
# Example 1:
# Input: "aabcccccaaa"
# Output: "a2b1c5a3"
#
# Example 2:
# Input: "abbccd"
# Output: "abbccd"
#
# Explanation:
# The compressed string is "a1b2c2d1", which is longer than the original string.
#  
#
# Note:
# 0 <= S.length <= 50000


class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 0:
            return S
        pre = S[0]
        res = ''
        S_copy = S + '/'
        count = 0
        for item in S_copy:
            if pre == item:
                count += 1
            else:
                res += pre + str(count)
                count = 1
                pre = item
        return res if len(res) < len(S) else S
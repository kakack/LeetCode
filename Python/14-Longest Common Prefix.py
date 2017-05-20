# Write a function to find the longest common prefix string amongst an array of strings.

# 妙用zip方法打包

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
            return min(strs)
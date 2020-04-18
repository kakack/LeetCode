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
        
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        ans = strs[0]
        for str in strs[1:]:
            i = 0
            while i < len(ans) and i < len(str):
                if ans[i] != str[i]:
                    break
                i += 1
            ans = ans[:i]
            if ans == '':
                return ans
        return ans

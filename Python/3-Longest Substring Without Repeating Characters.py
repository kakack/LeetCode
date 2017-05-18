# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# 用hash表，也就是python中的字典dict来存储字符串中的内容

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, start, res = {}, 0, 0
        for i, ch in enumerate(s):
            # 这个enumerate用的很巧妙，精简了很多代码，不然要写成dict[s[i]]
            if ch in dic:
                res = max(res, i-start)
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        return max(res, len(s)-start)
        # 小心没重复的substring

        
# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 49-Group Anagrams.py
@time: 2020/7/10 15:59
@desc:
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def cal(s):
            str = list(s)
            str.sort()
            return "".join(str)
        digitMap = {}
        for str in strs:
            digit = cal(str)
            if digit not in digitMap.keys():
                digitMap[digit] = [str]
            else:
                digitMap[digit].append(str)
        return list(digitMap.values())
                

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))




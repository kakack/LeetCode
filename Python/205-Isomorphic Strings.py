# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
#
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in range(n):
            key, value = s[i], t[i]
            if hashmap.get(key) is None:
                if value in hashmap.values():
                    return False
                else:
                    hashmap[key] = value
            else:
                if hashmap[key] != value:
                    return False
        return True
# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 10-Regular Expression Matching.py
@time: 2020/6/20 11:30
@desc:
"""
"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0: return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1; length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]): return True
                i+=1
            return False

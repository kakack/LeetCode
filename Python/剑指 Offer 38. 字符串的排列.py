# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 剑指 Offer 38. 字符串的排列.py
@time: 2021/6/22 10:27
@desc:
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    rec = []
    vis = []
    def backtrack(self, s, i, n, perm):
        if i == n:
            self.rec.append(perm)
            return
        for j in range(n):
            if self.vis[j] or (j > 0 and not self.vis[j - 1] and s[j - 1] == s[j]):
                continue
            self.vis[j] = True
            perm = perm + s[j]
            self.backtrack(s, i + 1, n, perm)
            perm = perm[:-2]
            self.vis[j] = False

    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        self.vis = [False] * n
        sorted(s)
        nonlocal perm = ""
        self.backtrack(s, 0, n, perm)
        return self.rec

if __name__ == '__main__':
    s = Solution()
    print(s.permutation("abc"))

class Solution:
    def permutation(self, s: str) -> List[str]:
        return list(set([''.join(x) for x in permutations(s, len(s))]))
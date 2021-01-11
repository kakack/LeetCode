# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1202-Smallest String With Swaps.py
@time: 2021/1/11 19:45
@desc:
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.



Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"


Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""


class DisjointSetUnion:
    def __init__(self, n: int):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DisjointSetUnion(len(s))
        for x, y in pairs:
            dsu.unionSet(x, y)

        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[dsu.find(i)].append(ch)

        for vec in mp.values():
            vec.sort(reverse=True)

        ans = list()
        for i in range(len(s)):
            x = dsu.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()

        return "".join(ans)



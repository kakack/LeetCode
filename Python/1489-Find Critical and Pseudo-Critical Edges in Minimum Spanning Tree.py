# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1489-Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree.py
@time: 2021/1/21 10:15
@desc:
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.



Example 1:



Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
Example 2:



Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.


Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x, y):
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        # 计算 value
        uf_std = UnionFind(n)
        value = 0
        for i in range(m):
            if uf_std.unite(edges[i][0], edges[i][1]):
                value += edges[i][2]

        ans = [list(), list()]

        for i in range(m):
            # 判断是否是关键边
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i != j and uf.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if uf.setCount != 1 or (uf.setCount == 1 and v > value):
                ans[0].append(edges[i][3])
                continue

            # 判断是否是伪关键边
            uf = UnionFind(n)
            uf.unite(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and uf.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value:
                ans[1].append(edges[i][3])

        return ans

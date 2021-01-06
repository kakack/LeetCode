# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 399-Evaluate Division.py
@time: 2021/1/6 9:29
@desc:
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph, set_ = defaultdict(list), set()
        for i, x in enumerate(equations):
            set_.add(x[0])
            set_.add(x[1])
            graph[x[0]].append((x[1], values[i]))
            graph[x[1]].append((x[0], 1 / values[i]))
        res = []
        for idx, node in enumerate(queries):
            x, y = node
            if x not in set_ or y not in set_:
                res.append(-1.)
            elif x == y:
                res.append(1.)
            else:
                stack, seen = [(x, 1)], {}
                while stack:
                    jj, ans = stack.pop()
                    for ii, val in graph[jj]:
                        if y == ii:
                            res.append(ans * val)
                            stack = []
                            break
                        if ii in seen:
                            continue
                        else:
                            seen[ii] = 1
                            stack.append((ii, ans * val))
            if len(res) < idx + 1:
                res.append(-1.)
        return res

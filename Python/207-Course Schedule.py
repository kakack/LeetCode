# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 207-Course Schedule.py
@time: 2020/8/4 10:11
@desc:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

「拓扑排序」判断由安排图生成的DAG有无环路，如果有环路则表示有有循环依赖
拓扑排序思路：对于DAG中所有node进行排序，使得每一条有向边（u, v)均有u比v先出现
"""

from collections import deque


class Solution(object):
    # BFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            # 记录所有节点的入度，即本课程有多少个前置课程
            adjacency[pre].append(cur)
            # 记录pre这个节点的所有后置节点（即被pre依赖的），保存在adjacency[pre]内
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
            # queue保存所有入度为0的节点，即本课程当前没有任何依赖的前置课程
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            # 表示这个节点已访问了
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses

    # DFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 借助标志列表flags，未被访问0、已被其他节点启动的访问-1、已被当前节点节点启动的访问1
        # 对numCourse里每个点进行判断，是否存在环状
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            elif flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency,flags):
                    return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True

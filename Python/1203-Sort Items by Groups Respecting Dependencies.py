# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1203-Sort Items by Groups Respecting Dependencies.py
@time: 2021/1/12 10:16
@desc:
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.



Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.


Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
"""


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        dep = [0] * n
        group_dep = [0] * m
        other_queue = []
        group_queue = [[] for _ in range(m)]
        queue_queue = []
        dependedBy = [[] for _ in range(n)]

        for i, l in enumerate(beforeItems):
            dep[i] = len(l)
            gi = group[i]
            for j in l:
                dependedBy[j].append(i)
                if gi != -1 and group[j] != gi:
                    group_dep[gi] += 1
            if not l:
                (group_queue[gi] if gi != -1 else other_queue).append(i)
        for i, gd in enumerate(group_dep):
            if not gd:
                queue_queue.append(group_queue[i])
        result = []
        while True:
            if queue_queue:
                current_queue = queue_queue.pop()
            elif other_queue:
                current_queue = other_queue
            else:
                if len(result) < n:
                    return []
                else:
                    return result
            while current_queue:
                p = current_queue.pop()
                result.append(p)
                gp = group[p]
                for i in dependedBy[p]:
                    gi = group[i]
                    dep[i] -= 1
                    if not dep[i]:
                        (group_queue[gi] if gi != -1 else other_queue).append(i)
                    if gi != -1 and gi != gp:
                        group_dep[gi] -= 1
                        if not group_dep[gi]:
                            queue_queue.append(group_queue[gi])


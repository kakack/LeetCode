# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 959-Regions Cut By Slashes.py
@time: 2021/1/25 9:27
@desc:
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.



Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:



Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""

class disjoint_set():
    def __init__(self, n):
        self.father = [i for i in range(n)]

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.father[self.find(self.father[x])]
        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x == father_y:
            return True  # 构成闭环
        else:
            self.father[father_x] = father_y
            return False


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        num = n + 1
        dis_set = disjoint_set(num * num)
        # 将一维的列表结构转换为二维上的正方形结构
        for i in range(num * num):
            if int(i / num) == 0 or int(i / num) == num - 1 or int(i % num) == num - 1 or int(i % num) == 0:
                dis_set.union(i, 0)  # 先融合正方形的边上的顶点
        count = 1
        # 融合所给出的grid顶点
        for j in range(n):
            sub_str = grid[j]
            for c in range(len(sub_str)):
                if sub_str[c] == '/':
                    if dis_set.union((j + 1) * num + c, j * num + c + 1):
                        count += 1
                elif sub_str[c] == '\\':
                    if dis_set.union(j * num + c, (j + 1) * num + c + 1):
                        count += 1
        return count



###################################################################

# class Solution(object):
#     def regionsBySlashes(self, grid):
#         """
#         :type grid: List[str]
#         :rtype: int
#         """
#
#         def find(f, x):
#             if f[x] == x:
#                 return x
#             fa = find(f, f[x])
#             f[x] = fa
#             return fa
#
#         def merge(f, x, y):
#             fx = find(f, x)
#             fy = find(f, y)
#             f[fx] = fy
#
#         n = len(grid)
#         f = [_ for _ in range(n * n * 4)]
#
#         for i in range(n):
#             for j in range(n):
#                 idx = i * n + j
#                 if i < n - 1:
#                     bottom = idx + n
#                     merge(f, idx * 4 + 2, bottom * 4)
#                 if j < n - 1:
#                     right = idx + 1
#                     merge(f, idx * 4 + 1, right * 4 + 3)
#                 if grid[i][j] == '/':
#                     merge(f, idx * 4, idx * 4 + 3)
#                     merge(f, idx * 4 + 1, idx * 4 + 2)
#                 elif grid[i][j] == '\\':
#                     merge(f, idx * 4, idx * 4 + 1)
#                     merge(f, idx * 4 + 2, idx * 4 + 3)
#                 else:
#                     merge(f, idx * 4, idx * 4 + 1)
#                     merge(f, idx * 4 + 1, idx * 4 + 2)
#                     merge(f, idx * 4 + 2, idx * 4 + 3)
#         fathers = []
#         for i in range(n * n * 4):
#             fa = find(f, i)
#             fathers.append(fa)
#         return len(fathers)

#
# if __name__ == '__main__':
#     # n = 4
#     # test = [_ for _ in range(n * n * 4)]
#     # print(test)

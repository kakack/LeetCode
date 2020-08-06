# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 463-Island Perimeter.py
@time: 2020/8/6 9:52
@desc:
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    for dir in dirs:
                        i_, j_ = i + dir[0], j + dir[1]
                        if i_ < 0 or j_ < 0 or i_ >= row or j_ >= col or grid[i_][j_] == 0:
                            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    ipt = [[0, 1, 0, 0],
           [1, 1, 1, 0],
           [0, 1, 0, 0],
           [1, 1, 0, 0]]
    print(s.islandPerimeter(ipt))

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1
#
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3
from collections import deque
class Solution(object):
    # def dfs(self, grid, r, c):
    #     grid[r][c] = 0
    #     nr, nc = len(grid), len(grid[0])
    #     for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
    #         if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
    #             self.dfs(grid, x, y)
    #
    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     nr = len(grid)
    #     if nr == 0:
    #         return 0
    #     nc = len(grid[0])
    #
    #     ans = 0
    #     for r in range(nr):
    #         for c in range(nc):
    #             if grid[r][c] == '1':
    #                 ans += 1
    #                 self.dfs(grid, r, c)
    #     return ans
    def numIslands(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        ans = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    ans += 1
                    grid[r][c] = '0'
                    neighbours = deque([(r, c)])
                    while neighbours:
                        row, col = neighbours.popleft()
                        for x, y in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                neighbours.append((x, y))
                                grid[x][y] = "0"
        return ans
# On a N * N grid, we place some 1 * 1 * 1 cubes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
# Return the total surface area of the resulting shapes.
#
# Example 1:
# Input: [[2]]
# Output: 10
#
# Example 2:
# Input: [[1,2],[3,4]]
# Output: 34
#
# Example 3:
# Input: [[1,0],[0,2]]
# Output: 16
#
# Example 4:
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
#
# Example 5:
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
#
# Note:
# - 1 <= N <= 50
# - 0 <= grid[i][j] <= 50


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    ans += 2
                    for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= ni < N and 0 <= nj < N:
                            nval = grid[ni][nj]
                        else:
                            nval = 0
                        ans += max(grid[i][j] - nval, 0)
        return ans



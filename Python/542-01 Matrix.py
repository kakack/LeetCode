# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
#  
#
# Example 1:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# Example 2:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
#  
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        root = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    root.append([i, j])
                else:
                    matrix[i][j] = -1
        while root:
            x, y = root.pop(0)
            for x_bias, y_bias in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                x_ = x + x_bias
                y_ = y + y_bias
                if x_ >= 0 and x_ < m and y_ >= 0 and y_ < n and matrix[x_][y_] == -1:
                    matrix[x_][y_] = matrix[x][y] + 1
                    root.append([x_, y_])
        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))



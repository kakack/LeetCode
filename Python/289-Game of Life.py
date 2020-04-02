# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population..
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# Example:

# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:

# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
import copy
class Solution(object):
    def judge(self, board, i, j, row, col):
        sum = 0
        for i_ in [i - 1, i, i + 1]:
            for j_ in [j - 1, j, j + 1]:
                if i_ >= 0 and i_ < row and j_ >= 0 and j_ < col:
                    sum += board[i_][j_]
        sum -= board[i][j]
        if board[i][j] == 1 and (sum == 2 or sum == 3):
            return True
        elif board[i][j] == 0 and sum == 3:
            return True
        else:
            return False

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        # res = [[0] * col for _ in range(row)]
        board_ = copy.deepcopy(board)
        for i in range(row):
            for j in range(col):
                if self.judge(board_, i, j, row, col):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        # board = res
if __name__ == '__main__':
    s = Solution()
    input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.gameOfLife(input)
    print(input)
# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 37-Sudoku Solver.py
@time: 2020/9/15 9:32
@desc:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        self.valid = False
        spaces = list()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        def dfs(pos):

            if pos == len(spaces):
                self.valid = True
                return

            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if self.valid:
                    return

        dfs(0)

        def publish(board):
            for row in board:
                print(row)

        publish(board)


if __name__ == '__main__':
    s = Solution()
    ipt = [
        [".", ".", "5", ".", "2", "9", ".", ".", ".", ],
        [".", "3", ".", ".", ".", ".", ".", "7", ".", ],
        [".", ".", ".", "4", "8", ".", ".", ".", "2", ],
        ["3", ".", ".", ".", ".", ".", "4", ".", ".", ],
        ["1", ".", "2", ".", ".", ".", "9", ".", "8", ],
        [".", ".", "9", ".", ".", ".", ".", ".", "7", ],
        ["9", ".", ".", ".", "1", "5", ".", ".", ".", ],
        [".", "2", ".", ".", ".", ".", ".", "6", ".", ],
        [".", ".", ".", "2", "3", ".", "5", ".", ".", ]
    ]
    s.solveSudoku(ipt)


#
# [['8', '7', '5', '3', '2', '9', '1', '4', '6'],
#  ['2', '3', '4', '5', '6', '1', '8', '7', '9'],
#  ['6', '9', '1', '4', '8', '7', '3', '5', '2'],
#  ['3', '6', '7', '8', '9', '2', '4', '1', '5'],
#  ['1', '5', '2', '6', '7', '4', '9', '3', '8'],
#  ['4', '8', '9', '1', '5', '3', '6', '2', '7'],
#  ['9', '4', '6', '7', '1', '5', '2', '8', '3'],
#  ['5', '2', '3', '9', '4', '8', '7', '6', '1'],
#  ['7', '1', '8', '2', '3', '6', '5', '9', '4']]

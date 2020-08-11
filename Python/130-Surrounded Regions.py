# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 130-Surrounded Regions.py
@time: 2020/8/11 9:28
@desc:
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

Solution:
- 对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；
- 最后我们遍历这个矩阵，对于每一个字母：
    - 如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
    - 如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X。

"""

import collections


class Solution(object):
    # def solve(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: None Do not return anything, modify board in-place instead.
    #     深度优先遍历
    #     """
    #     if not board:
    #         return
    #     n, m = len(board), len(board[0])
    #
    #     def dfs(x, y):
    #         if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
    #             return
    #         board[x][y] = 'A'
    #         dfs(x + 1, y)
    #         dfs(x - 1, y)
    #         dfs(x, y + 1)
    #         dfs(x, y - 1)
    #
    #     for i in range(n):
    #         dfs(i, 0)
    #         dfs(i, m - 1)
    #     for i in range(1, m - 1):
    #         dfs(0, i)
    #         dfs(n - 1, i)
    #
    #     for row in board:
    #         print(row)
    #
    #     for i in range(n):
    #         for j in range(m):
    #             if board[i][j] == 'A':
    #                 board[i][j] = 'O'
    #             elif board[i][j] == 'O':
    #                 board[i][j] = 'X'

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        广度优先遍历
        """
        if not board:
            return

        n, m = len(board), len(board[0])
        que = collections.deque()
        for i in range(n):
            if board[i][0] == 'O':
                que.append((i, 0))
            if board[i][m - 1] == 'O':
                que.append((i, m - 1))
        for i in range(1, m - 1):
            if board[0][i] == 'O':
                que.append((0, i))
            if board[n - 1][i] == 'O':
                que.append((n - 1, i))
        print(que)
        while que:
            x, y = que.popleft()
            board[x][y] = 'A'
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'O':
                    que.append((nx, ny))

        for row in board:
            print(row)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    # ipt = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    ipt = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]

    s = Solution()
    s.solve(ipt)
    # print(ipt)

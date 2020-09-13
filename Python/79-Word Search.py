# -*- coding: utf-8 -*
"""
@author: Kaka Chen
@license: (C) Copyright Personal Uncommercial Limited.
@contact: kakachen1990@gmail.com
@file: 79-Word Search.py
@time: 2020/9/13 11:26 上午
@desc:
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        height, width = len(board), len(board[0])

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                n_i, n_j = i + di, j + dj
                if 0 <= n_i < height and 0<= n_j < width:
                    if (n_i, n_j) not in visited:
                        if dfs(n_i, n_j, k+1):
                            result = True
                            break
            visited.remove((i, j))
            return result

        for i in range(height):
            for j in range(width):
                if dfs(i, j, 0):
                    return True
        return False


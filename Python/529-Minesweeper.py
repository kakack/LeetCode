# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 529-Minesweeper.py
@time: 2020/8/20 9:38
@desc:

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board.
'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent
(above, below, left, right, and all 4 diagonals) mines,
digit ('1' to '8') represents how many mines are adjacent to this revealed square,
and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed,
then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed,
then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:



Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'),
which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem.
For example, you don't need to reveal all the unrevealed mines when the game is over,
consider any cases that you will win the game or flag any squares.
"""

from collections import deque


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row, col = len(board), len(board[0])
        x, y = click

        def nearMine(x, y):
            ans = 0
            for mx in [-1, 0, 1]:
                for my in [-1, 0, 1]:
                    if (mx, my) != (0, 0) and 0 <= x + mx < row and 0 <= y + my < col and \
                            board[x + mx][y + my] == 'M':
                        ans += 1
            return ans

        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                i, j = queue.popleft()
                flag = nearMine(i, j)
                if flag > 0:
                    board[i][j] = str(flag)
                    continue
                else:
                    board[i][j] = 'B'
                    for mx in [-1, 0, 1]:
                        for my in [-1, 0, 1]:
                            if (mx, my) == (0, 0):
                                continue
                            i_, j_ = i + mx, j + my
                            if i_ < 0 or j_ < 0 or i_ >= row or j_ >= col:
                                continue
                            elif board[i_][j_] == "E":
                                queue.append((i_, j_))
                                board[i_][j_] = "B"

        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            bfs(x, y)
        return board


if __name__ == '__main__':
    s = Solution()
    # ipt = [['B', '1', 'E', '1', 'B'],
    #        ['B', '1', 'M', '1', 'B'],
    #        ['B', '1', '1', '1', 'B'],
    #        ['B', 'B', 'B', 'B', 'B']]
    # click = [1, 2]
    ipt = [['E', 'E', 'E', 'E', 'E'],
           ['E', 'E', 'M', 'E', 'E'],
           ['E', 'E', 'E', 'E', 'E'],
           ['E', 'E', 'E', 'E', 'E']]

    click = [3, 0]
    print(s.updateBoard(ipt, click))

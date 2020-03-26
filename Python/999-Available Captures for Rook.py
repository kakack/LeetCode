# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.
# # The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.
# # Return the number of pawns the rook can capture in one move.
# #
# # Example 1:
# # Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# # Output: 3
# # Explanation:
# # In this example the rook is able to capture all the pawns.
# #
# # Example 2:
# # Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# # Output: 0
# # Explanation:
# # Bishops are blocking the rook to capture any pawn.
# #
# # Example 3:
# # Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# # Output: 3
# # Explanation:
# # The rook can capture the pawns at positions b5, d6 and f5.
# #  
# #
# # Note:
# # - board.length == board[i].length == 8
# # - board[i][j] is either 'R', '.', 'B', or 'p'
# # - There is exactly one cell with board[i][j] == 'R'

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        res = 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rockRow = i
                    rockCol = j
        left, right, up, down = rockCol, 8 - rockCol - 1, rockRow, 8 - rockRow - 1
        print(left, right, up, down)
        i = 1
        while i <= left:
            if board[rockRow][rockCol - i] == 'p':
                res += 1
                break
            elif board[rockRow][rockCol - i] == 'B':
                break
            else:
                i += 1
        i = 1
        while i <= right:
            if board[rockRow][rockCol + i] == 'p':
                res += 1
                break
            elif board[rockRow][rockCol + i] == 'B':
                break
            else:
                i += 1
        i = 1
        while i <= up:
            if board[rockRow - i][rockCol] == 'p':
                res += 1
                break
            elif board[rockRow - i][rockCol] == 'B':
                break
            else:
                i += 1
        i = 1
        while i <= down:
            if board[rockRow + i][rockCol] == 'p':
                res += 1
                # print('down')
                # print()
                break
            elif board[rockRow + i][rockCol] == 'B':
                break
            else:
                i += 1
        return res

if __name__ == '__main__':
    s = Solution()
    # board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(s.numRookCaptures(board))
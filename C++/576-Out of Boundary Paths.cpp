/*
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.



Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12


Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
*/

#include <vector>

using namespace std;

class Solution {
public:
    // vector<vector<vector<int >>> dp;

    int solve(vector<vector<vector<int >>> dp, int i, int j, int m, int n, int maxMove) {
        if (maxMove < 0) {
            return 0;
        } else if (i < 0 || i >= m || j < 0 || j >= n) {
            return 1;
        } else if (dp[i][j][maxMove] != -1) {
            return dp[i][j][maxMove];
        }
        dp[i][j][maxMove] = solve(dp, i - 1, j, m, n, maxMove - 1) + solve(dp, i + 1, j, m, n, maxMove - 1) + solve(dp, i, j - 1, m, n, maxMove - 1) + solve(dp, i, j + 1, m, n, maxMove - 1);
            return dp[i][j][maxMove];
        } 
    
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        vector<vector<vector<int >>> dp(m, vector<vector<int>>(n, vector<int>(maxMove + 1, -1)));
        return solve(dp, startRow, startColumn, m, n, maxMove) % 1000000007;
    }
};
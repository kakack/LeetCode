/*
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
*/

class Solution {
private:
    vector<vector<int>> neighbors = {{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};

public:
    int slidingPuzzle(vector<vector<int>>& board) {
        // 枚举 status 通过一次交换操作得到的状态
        auto get = [&](string& status) -> vector<string> {
            vector<string> ret;
            int x = status.find('0');
            for (int y: neighbors[x]) {
                swap(status[x], status[y]);
                ret.push_back(status);
                swap(status[x], status[y]);
            }
            return ret;
        };

        string initial;
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 3; ++j) {
                initial += char(board[i][j] + '0');
            }
        }
        if (initial == "123450") {
            return 0;
        }

        queue<pair<string, int>> q;
        q.emplace(initial, 0);
        unordered_set<string> seen = {initial};

        while (!q.empty()) {
            auto [status, step] = q.front();
            q.pop();
            for (auto&& next_status: get(status)) {
                if (!seen.count(next_status)) {
                    if (next_status == "123450") {
                        return step + 1;
                    }
                    q.emplace(next_status, step + 1);
                    seen.insert(move(next_status));
                }
            }
        }

        return -1;
    }
};

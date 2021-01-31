/*
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
*/

#include <vector>
#include <algorithm>

using namespace std;

class Djset {
    public:
    vector<int> parent;
    vector<int> rank;
    Djset(int n):parent(vector<int>(n)), rank(vector<int>(n)) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void merge(int x, int y) {
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            if (rank[rootx] < rank[rooty]) {
                swap(rootx, rooty);
            }
            parent[rooty] = rootx;
            if (rank[rooty] == rank[rooty]) rank[rooty] += 1;
        }
    }

    bool isSame(int x, int y) {
        return find(x) == find(y);
    }
};

struct Edge {
    int start;
    int end;
    int len;
};

class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<Edge> edges;
        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j ++) {
                if (i + 1 < n) {
                    edges.push_back({i * n + j, (i + 1) * n + j, max(grid[i][j], grid[i + 1][j])});
                }
                if (j + 1 < n) {
                    edges.push_back({i * n + j, i * n + j + 1, max(grid[i][j], grid[i][j + 1])});
                }
            }
        }
        sort(edges.begin(), edges.end(), [](auto& a, auto& b){
            return a.len < b.len;
        });
        Djset ds(n * n);
        for (const auto& e : edges) {
            ds.merge(e.start, e.end);
            if (ds.isSame(0, n * n - 1)) return e.len;
        }
        return 0;
    }
};
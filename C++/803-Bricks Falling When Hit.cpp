/*
You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

 

Example 1:

Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].
Example 2:

Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [1,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is 0 or 1.
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
All (xi, yi) are unique.
*/

# include "vector"

using namespace std;
class Solution {
public:
    int n, m;
    int dx[4] = {0, 1, 0, -1}, dy[4] = {1, 0, -1, 0};

    vector<int> p, cnt;

    int find(int x)
    {
        if(p[x] !=  x) p[x] = find(p[x]);
        return p[x];
    }

    void merge(int x, int y)
    {
        int a = find(x), b = find(y);
        if(a != b){
            if(cnt[a] < cnt[b]){
                p[a] = b; 
                cnt[b] += cnt[a];
            }   
            else{
                p[b] = a;
                cnt[a] += cnt[b];
            }
        }
    }

    void init(int n)
    {
        for(int i = 0; i < n; i++){
            p[i] = i;
            cnt[i] = 1;
        }
    }
    
    int get(int x, int y)
    {
        return x * m + y;
    }

    vector<int> hitBricks(vector<vector<int>>& _grid, vector<vector<int>>& hits) {
        vector<vector<int>> grid = _grid;
        n = grid.size();
        m = grid[0].size();
        int len = hits.size();
        //## step1 全部击碎 后维护集合关系
        // 把砖头🧱打掉
        for(auto &h : hits)  grid[h[0]][h[1]] = 0;
        // 开始集合初始化 0 ～n*m 
        int roof = n * m; // 屋顶元素的下标
        p.resize(n * m + 1 );  // 0 ～ n * m
        cnt.resize(n * m  + 1);
        init(n * m + 1);
        
        // 合并集合
        for(int i = 0; i < m; i ++)
            if(grid[0][i] == 1) merge(i, roof);
       // 遍历其余  上到下  左到右
        for(int i = 1; i < n; i++)
            for(int j = 0; j < m; j ++)
                if(grid[i][j] == 1)
                {
                    if(grid[i - 1][j] == 1) 
                        merge(get(i, j), get(i - 1, j));
                    if(j > 0 && grid[i][j - 1] == 1) 
                        merge(get(i, j), get(i, j - 1));
                }

       // ## step2 倒序补砖头🧱  维护集合  ，补一块 前后差- 1为生效的砖头数量
        vector<int>  res(len);
        for(int i = len - 1; i >= 0; i --){
            int x = hits[i][0], y = hits[i][1];

            if(_grid[x][y] == 0) continue; // 本身是0，而不是打掉而造成的0
            // 补之前
            int before = cnt[find(roof)]; 

            // 开始补操作
            if(x == 0) merge(y, roof);
            for(int d = 0; d < 4; d ++){
                int nx = x + dx[d], ny = y + dy[d];
                if(nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == 1)
                    merge(get(x, y), get(nx, ny));
            }

            // 补之后
            int cur = cnt[find(roof)];
            res[i] = max(0, cur - before - 1);

            grid[x][y] = 1; 
        }

        return res;
        
    }
};
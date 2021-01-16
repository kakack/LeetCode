# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 803. Bricks Falling When Hit
@time: 2021/1/16 9:31
@desc:
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

"""

class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}
    
    def get_size_of_set(self,x):
        """
        获取所在连通块的大小
        """
        return self.size_of_set[self.find(x)]
    
    def find(self,x):
        root = x
        
        while self.father[root] != None:
            root = self.father[root]
        
        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root
    
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        
        if root_x != root_y:
            self.father[root_x] = root_y
            # 更新根节点连通块数量
            self.size_of_set[root_y] += self.size_of_set[root_x]
            del self.size_of_set[root_x]
    
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            self.size_of_set[x] = 1
            

class Solution:
    def __init__(self):
        self.CEILING = (-1,-1)
        self.DIRECTION = ((1,0),(-1,0),(0,1),(0,-1))
    
    def initialize(self,uf,m,n,grid,hits):
        """
        初始化
        """
        # 添加天花板
        uf.add(self.CEILING)
        
        # 敲掉所有要敲掉的砖块
        for x,y in hits:
            grid[x][y] -= 1
        
        # 连接，合并剩余的砖块
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.add((i,j))
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.merge_neighbors(uf,m,n,grid,i,j)
        
        # 与天花板合并
        for j in range(n):
            if grid[0][j] == 1:
                uf.merge((0,j),self.CEILING)
    
    def is_valid(self,x,y,grid,m,n):
        return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
    
    def merge_neighbors(self,uf,m,n,grid,x,y):
        """
        与上下左右的砖块合并
        """
        for dx,dy in self.DIRECTION:
            nx,ny = x+dx,y+dy
            if not self.is_valid(nx,ny,grid,m,n):
                continue
            uf.merge((x,y),(nx,ny))
    
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        uf = UnionFind()
        m,n = len(grid),len(grid[0])
        res = [0] * len(hits)
        
        # 初始化
        self.initialize(uf,m,n,grid,hits)

        for i in range(len(hits)-1,-1,-1):
            x,y = hits[i][0],hits[i][1]
            
            # 还原敲击
            grid[x][y] += 1
            
            # 敲的地方原本就不是砖块
            if grid[x][y] != 1:
                continue
            
            # 敲完以后与天花板连接的数量
            after_hit = uf.get_size_of_set(self.CEILING)
            
            # 填回砖块，合并
            uf.add((x,y))
            self.merge_neighbors(uf,m,n,grid,x,y)
            if x == 0:
                uf.merge((x,y),self.CEILING)
            
            # 被敲的地方和天花板连接
            if uf.is_connected((x,y),self.CEILING):
                # 敲之前和天花板连接的数量
                before_hit = uf.get_size_of_set(self.CEILING)
                res[i] = before_hit - after_hit - 1
        return res

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 通过深度优先搜索来遍历所有相邻陆地节点
        def dfs(i:int,j:int):
            # 把已经遍历到的陆地节点赋值成海水，表示该几点已经遍历过了，后续会跳过
            grid[i][j] = '0'
            # 四个方向
            directions = [
                (-1,0),
                (1,0),
                (0,-1),
                (0,1)
            ]
            # 每个节点遍历四个方向
            for di,dj in directions:
                ni = i+di
                nj = j+dj
                # 若该节点未超出边界且是陆地节点，则开始不断传递
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]=='1':
                    dfs(ni,nj)
        
        m = len(grid) # 行数
        n = len(grid[0])# 列数
        count = 0 # 岛屿计数
        # 遍历每个节点
        for i in range(m):
            for j in range(n):
                # 检测到节点是陆地，岛屿数量加一，遍历该陆地节点所有相邻的陆地节点
                if grid[i][j] == '1':
                    count+= 1
                    dfs(i,j)
        # 返回岛屿数量
        return count
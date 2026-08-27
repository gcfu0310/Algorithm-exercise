import collections
from typing import List

class Solution:
    # 时间复杂度是O(mn).空间复杂度是O(min(m,n))
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        queue = collections.deque()
        directions = {
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        }
        # 广度遍历
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append((i,j))
                    count += 1
                grid[i][j] = '0'
                while queue:
                    x,y = queue.popleft()
                    for dx,dy in directions:
                        nx = x+dx
                        ny = y+dy
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny]=='1':
                            queue.append((nx,ny))
                            grid[nx][ny] = '0'
        return count
                    





        
import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0 # 计算时间
        queue = collections.deque() # queue存放腐烂的橘子
        fresh = 0 # 记录健康橘子书
        directions = {
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        }
        # 将第0min的腐烂橘子添加进队列中并记录健康橘子的数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    grid[i][j] = 0
                if grid[i][j] == 1:
                    fresh += 1

        # 开始模拟腐烂过程      
        while queue:
            level_size = len(queue) # 当前时间下有几个腐烂橘子
            rotted_flag = False # 记录当前这一轮是否有橘子被感染
            for _ in range(level_size):
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                        queue.append((nx,ny))
                        grid[nx][ny] = 0
                        rotted_flag = True # 有橘子被感染
                        fresh -= 1 # 健康橘子数减一
            # 有橘子被感染，时间数加一(当grid中只有一个腐烂橘子时)
            if rotted_flag:
                count += 1

        # 如果健康橘子的数量为0，返回时间，否则返回-1
        if not fresh:
            return count
        else:
            return -1

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    S = Solution()
    ans = S.orangesRotting(grid)                 
    print(ans)





        
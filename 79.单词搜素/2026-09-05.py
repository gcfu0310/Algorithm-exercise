from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x,y,i):
            nonlocal f
            if i < len(word):
                if board[x][y] != word[i]:
                    return
                else:
                    path.append(board[x][y]) 
                    t[(x,y)] = True
                if ''.join(path) == word:
                    f = True
                    return 
                for dx,dy in direction:
                    new_x = x+dx
                    new_y = y+dy
                    if 0<=new_x<m and 0<=new_y<n and not t[(new_x,new_y)]:
                        backtrack(new_x,new_y,i+1)
                
                if not f:
                    t[(x,y)] = False
                    path.pop()

        m = len(board)
        n = len(board[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        t = dict()
        path = []
        f = False
        for i in range(m):
            for j in range(n):
                t[(i,j)] = False
        for i in range(m):
            for j in range(n):
                backtrack(i,j,0)
        
        return f
        
# 优化后：
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x,y,i):
            if board[x][y] != word[i]:
                return False
            if i == len(word)-1:
                return True
            temp = board[x][y]
            board[x][y] = '#'
            for dx,dy in direction:
                new_x = x+dx
                new_y = y+dy
                if 0<=new_x<m and 0<=new_y<n and board[new_x][new_y]!='#':
                    if backtrack(new_x,new_y,i+1):
                        return True
            
            board[x][y] = temp
            return False

        m = len(board)
        n = len(board[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    t = backtrack(i,j,0)
                    if t:
                        return t
        return False
        



        


        
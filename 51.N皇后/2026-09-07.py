from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path,ans = [],[]
        cols,diag1,diag2 = set(),set(),set()
        # 回溯查找每一行的位置
        def backtrack(row):
            # 此时n行已经全部确定了
            if row == n:
                board = []
                for col in path:
                    board.append('.'*col+'Q'+'.'*(n-col-1))
                ans.append(board)
                return 
            # 遍历每一列，从而确定(row,col)
            for col in range(n):
                # 检测当前这个位置是否符合条件
                # cols存放已存在棋子所在列，diag1存放已存在棋子的右斜线，diag2存放已存在棋子的左斜线
                if col in cols or (row+col) in diag1 or (row-col) in diag2:
                    continue
                else:
                    # 利用path存放每个棋子的位置，下标表示行，值代表列
                    path.append(col)
                    # 把当前棋子的列以及斜线放进存储区域
                    cols.add(col)
                    diag1.add(row+col)
                    diag2.add(row-col)

                    # 开始回溯
                    backtrack(row+1)

                    # 撤销当前棋子的位置，add是随机添加到某个位置，所以应当用remove，而不是pop
                    cols.remove(col)
                    diag1.remove(row+col)
                    diag2.remove(row-col)
                    path.pop() # 把当前这个棋子位置弹出
        backtrack(0)
        return ans
                    
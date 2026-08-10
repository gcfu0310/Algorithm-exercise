from typing import List

class Solution:
    # 时间复杂度是O(mn),空间复杂度是O(m+n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        set_row = set()
        set_column = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_row.add(i)
                    set_column.add(j)

        for i in range(m):
            for j in range(n):
                if i in set_row or j in set_column:
                    matrix[i][j] = 0

    # 时间复杂度是O(mn),空间复杂度是O(1)
    def setZeroes_2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        Flag_c = False
        for i in range(m):
            if matrix[i][0] == 0:
                Flag_c = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if Flag_c:
            for i in range(m):
                matrix[i][0] = 0

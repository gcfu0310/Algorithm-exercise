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
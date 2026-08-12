from typing import List

class Solution:
    # 时间复杂度为O(n^2),空间复杂度也是O(n^2)
    # 引用辅助矩阵，来标记是否遍历过
    def rotate_1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                row,column = i,j
                prev = matrix[row][column]
                while not visited[row][column]:
                    visited[row][column] = True
                    row,column = column,n-1-row
                    curr = matrix[row][column]
                    matrix[row][column] = prev
                    prev = curr

    # 时间复杂度为O(n^2),空间复杂度是O(1)
    # 用翻转来代替旋转，先水平翻转，再延主对角线翻转
    def rotate_2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[i][j],matrix[n-i-1][j] = matrix[n-i-1][j],matrix[i][j]

        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    # 时间复杂度是O(n^2)，空间复杂度是O(1)
    # 把整个矩阵分成四块来直接旋转
    def rotate_3(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
        
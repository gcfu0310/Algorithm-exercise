class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def reversed(row:int,left:int,right:int)->None:
            while left<right:
                matrix[row][left],matrix[row][right]=matrix[row][right],matrix[row][left]
                left+=1
                right-=1

        n=len(matrix)
        # 用翻转代替旋转 先矩阵转置，再沿竖轴翻转
        # 时间复杂度为O(n^2),空间复杂度为O(1)
        for i in range(n):
            for j in range(i,n):
                temp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=temp
        for i in range(n):
            reversed(i,0,n-1)
        
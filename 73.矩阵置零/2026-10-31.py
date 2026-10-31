class Solution:
    def setZeroes_1(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        用原矩阵第一行和第一列用来标记存在零的行和列，第一行和第一列是否有零，则是用matrix[0][0]和Flag_c来标记
        """
        # 时间复杂度为O(mn),空间复杂度为O(1)
        # 优点节省空间，缺点代码可读性太差
        m=len(matrix)
        n=len(matrix[0])
        Flag_c=False
        for i in range(m):
            if matrix[i][0]==0:
                Flag_c=True
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j]=0
        if Flag_c:
            for i in range(m):
                matrix[i][0]=0
    
    def setZeroes_2(self, matrix: list[list[int]]) -> None:
        # 时间复杂度为O(mn),空间复杂度为O(1)
        # 与方法一相比，用了两个标记变量分别标记第一行和第一列是否存在零，寻找和标记零的位置与方法一相同
        # 遍历矩阵一个数为0，把该数对应的同行第0列和同列第0行元素标记为0，再遍历矩阵每个数，若这个数的同行第0列或是第0行同列为0，则把这个数赋值成0
        # 可读性比方法一更好，空间复杂度高于方法一
        m=len(matrix)
        n=len(matrix[0])
        Flagr=any(matrix[0][j]==0 for j in range(n)) # any的用法，只要迭代式中有一个数为真，即为真
        Flagc=any(matrix[i][0]==0 for i in range(m))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if Flagr:
            for j in range(n):
                matrix[0][j]=0

        if Flagc:
            for i in range(m):
                matrix[i][0]=0
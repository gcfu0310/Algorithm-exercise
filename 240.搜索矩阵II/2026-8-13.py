from typing import List

class Solution:
    # 时间复杂度O(mn),空间复杂度O(1)
    # 最简单的方法：一行行搜索
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False

    # 时间复杂度：O(mlogn),空间复杂度：O(1)
    # 利用二分查找的方法代替"in",从而降低时间复杂度
    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        def b_search(matrix:List[int],target:int)->bool:
            left,right = 0,len(matrix)-1
            while left <= right:
                mid = (left+right) // 2
                if matrix[mid] > target:
                    right = mid - 1
                elif matrix[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False

        for row in matrix:
            if b_search(row,target):
                return True

    # 时间复杂度:O(m+n),空间复杂度:O(1)
    # 利用矩阵行和列都是升序的特性，从矩阵的右上角进行搜索，左侧的数小，下方的数大，当搜索点的数大于目标时，向左移动；反之向下移动
    def searchMatrix_3(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix)-1,len(matrix[0])-1
        x,y = 0,n
        while 0<=x<=m and 0<=y<=n:
            curr = matrix[x][y]
            if curr > target:
                y -= 1
            elif curr < target:
                x += 1
            else:
                return True
        
        return False
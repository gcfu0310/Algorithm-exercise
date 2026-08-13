from typing import List

class Solution:
    # 时间复杂度O(n^2),空间复杂度O(1)
    # 最简单的方法：一行行搜索
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False

    # 时间复杂度：O(nlogn),空间复杂度：O(1)
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
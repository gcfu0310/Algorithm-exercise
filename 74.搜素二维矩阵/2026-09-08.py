from typing import List
class Solution:
    # 两次二分查找
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def binary_search()->bool:
            left,right,row = 0,m-1,-1
            while left<=right:
                mid = (left+right)//2
                if matrix[mid][0]<=target<=matrix[mid][-1]:
                    row = mid
                    break
                if target<matrix[mid][0]:
                    right = mid-1
                elif target>matrix[mid][-1]:
                    left = mid+1
            if row==-1:
                return False
            left,right = 0,n-1
            while left<=right:
                mid = (left+right)//2
                if matrix[row][mid] == target:
                    return True
                if matrix[row][mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return False
        return binary_search()

    # 一次二分查找
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def binary_search()->bool:
            left,right=0,m*n-1
            while left<=right:
                mid = (right-left)//2+left
                row = mid//n
                col = mid%n
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        return binary_search()


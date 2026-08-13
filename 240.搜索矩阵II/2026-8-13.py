from typing import List

class Solution:
    # 时间复杂度O(n^2),空间复杂度O(1)
    # 最简单的方法：一行行搜索
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False
        
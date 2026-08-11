from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 记录答案
        ans = list()
        # 初始化上边界和左边界
        top,left = 0,0
        # 初始化下边界和右边界
        bottom,right = len(matrix)-1,len(matrix[0])-1
        # 顺时针方向，本质上就是右->下->左->上，我们通过确定边界来模拟顺时针移动，通过判断边界是否符合条件，来确定移动是否应该停止

        # 只有当上边界不大于下边界和左边界不大于右边界，才进入循环开始移动
        while top <= bottom and left <= right:
            # 先是向右移动
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            # 向右移动完成后，上边界向下移动
            top += 1

            # 再向下移动
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            # 向下移动完成后，右边界向左移动
            right -= 1

            # 当矩阵只用一行时，此时所有元素已经遍历完了，就不需要再向左移动了
            if top <= bottom:
                # 接着向左移动
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                # 向左移动完成后，下边界向上移动
                bottom -= 1

            # 当矩阵只有一列时，此时所有元素已经遍历完了，就不需要再向上移动了
            if left <= right:
                # 最后向上移动
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                # 向上移动完成后，左边界向右移动
                left += 1
        
        return ans
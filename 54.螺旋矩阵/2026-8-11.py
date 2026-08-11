class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 记录答案
        ans = list()
        # 初始化上边界和左边界
        top,left = 0,0
        # 初始化下边界和右边界
        bottom,right = len(matrix)-1,len(matrix[0])-1
        # 只有当上边界不大于下边界或是左边界不大于右边界，才进入循环开始移动
        while top <= bottom and left <= right:
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top += 1

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
        
        return ans
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # 每一个位置能组成的最大面积就是右边第一个小于它的位置-左边第一个小于它的位置-1再乘这个位置的高度
        n,ans = len(heights),-1
        stack_left,stack_right = list(),list()
        ans_left,ans_right = [-1]*n,[n]*n
        for i in range(n):
            while stack_right and heights[i]<heights[stack_right[-1]]:
                idx = stack_right.pop()
                ans_right[idx] = i
            stack_right.append(i)
            while stack_left and heights[n-i-1]<heights[stack_left[-1]]:
                idx = stack_left.pop()
                ans_left[idx] = n-i-1
            stack_left.append(n-i-1)
        for j in range(n):
            if (ans_right[j]-ans_left[j]-1)*heights[j]>ans:
                ans = (ans_right[j]-ans_left[j]-1)*heights[j]
        return ans
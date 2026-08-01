from typing import List

class Solution:
    # 动态规划
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)

        # 初始化max_left,max_right
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[n-1] = height[n-1]

        # 计算每个位置的max_left和max_right
        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i])
            max_right[n-i-1] = max(max_right[n-i],height[n-i-1])
        
        total = 0
        for i in range(n):
            # 计算每个位置的接水量，计算公式：min(max_left[i],max_right[i]) - height[i]
            total += ( min(max_left[i],max_right[i]) - height[i])
        return total

    # 双指针
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left,right = 0,n-1
        left_max,right_max = 0,0
        total = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max,height[left])
                total += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max,height[right])
                total += right_max - height[right]
                right -= 1
        return total


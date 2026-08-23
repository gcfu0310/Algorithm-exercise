from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        left_max,right_max = 0,0 
        total = 0 # 每格能接的雨水量由左右两边柱子最高值中较小的那个决定，我们只用维护left_max与right_max即可
        while left <= right:
            if left_max<right_max:
                left_max = max(height[left],left_max)
                total += left_max-height[left]
                left += 1
            else:
                right_max = max(height[right],right_max)
                total += right_max-height[right]
                right -= 1
        return total
from math import inf
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        min_num = inf
        while left<=right:
            mid = (right-left)//2+left
            if nums[mid]>=nums[left]:
                if min_num > nums[left]:
                    min_num = nums[left]
                left = mid + 1
            else:
                if min_num > nums[mid]:
                    min_num = nums[mid]
                right = mid-1
        return min_num
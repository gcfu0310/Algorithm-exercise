from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left,right = 0,n-1
        while left<=right:
            mid = (right-left)//2+left
            if nums[mid] == target:
                return mid
            # mid左边有序
            elif nums[left]<=nums[mid]:
                # target 有没有落在左侧有序部分
                if nums[left]<=target<nums[mid]:
                    # 有的话右指针左移
                    right = mid-1
                else:
                    left = mid+1
            # mid右边有序
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


                
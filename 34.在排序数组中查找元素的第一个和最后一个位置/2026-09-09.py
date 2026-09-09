from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def binary_search(left_flag:bool)->int:
            left,right,ans=0,n-1,-1
            while left<=right:
                mid = (right-left)//2+left
                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    ans=mid
                    if left_flag:
                        right=mid-1
                    else:
                        left=mid+1
            return ans
        return [binary_search(True),binary_search(False)]
        
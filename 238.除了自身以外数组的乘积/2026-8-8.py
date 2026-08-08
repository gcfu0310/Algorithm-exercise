from typing import List
class Solution:
    # 与接雨水一致的方法
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        ans = list()
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i-1] = right[n-i] * nums[n-i]
        for i in range(n):
            ans.append(left[i]*right[i])
        return ans
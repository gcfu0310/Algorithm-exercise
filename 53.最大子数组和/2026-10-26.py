from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        max_sum = float("-inf")
        pre=0
        # 以每个num结尾的最大子数组和为f(nums[i]) = max(f(nums[i-1])+nums[i],nums[i])
        for num in nums:
            pre = max(pre+num,num)
            max_sum = max(max_sum,pre)
        return max_sum
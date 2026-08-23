from typing import List

class Solution:
    # 时间复杂度是O(n)，空间复杂度是O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0 # 前缀和为0
        sum_max = nums[0] # 最大和定义为数组第一个元素
        for i in range(len(nums)):
            pre = max(pre+nums[i],nums[i]) # 取前缀和+nums[i]与nums[i]中的最大值，相当于如果当前数比前面所有数加起来都大，就舍弃前面的全部子数组，新的子数组从当前开始
            sum_max = max(pre,sum_max) # 最大和取当前最大和与前缀和的最大值
        return sum_max
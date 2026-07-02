class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i ,num in enumerate(nums):
            if i == 0:
                pre = num
                sum_max = pre
                continue
            if num + pre > num:
                pre = num + pre
            else:
                pre = num
            if pre > sum_max:
                sum_max = pre
        return sum_max
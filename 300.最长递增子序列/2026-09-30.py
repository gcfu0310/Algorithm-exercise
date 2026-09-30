class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # dp[i]存放的是第i个数能组成的最长递增子序列长度
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # 当前nums[i]>nums[j]时
                if nums[i]>nums[j]:
                    # dp[i]应该等于当前最长长度和新组成序列长度的较大值
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
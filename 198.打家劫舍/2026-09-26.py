from typing import List
class Solution:
    # 时间复杂度为O(n^2),空间复杂度为O(n)
    def rob(self, nums: List[int]) -> int:
        # 记录每一家能获取的最大收益
        dp = [0]*len(nums)
        dp[0] = (nums[0])
        if len(nums) == 1:
            return dp[0]
        dp[1] = nums[1]
        max_money = max(dp[0],dp[1])
        for i in range(2,len(nums)):
            for j in range(2,i+1):
                money = nums[i] + dp[i-j]
                if money > dp[i]:
                    dp[i] = money
                if money > max_money:
                    max_money = money
        return max_money

class Solution:
    def rob_1(self, nums: List[int]) -> int:
        """
        作为小偷一定是要偷到最后的,所以没有必要用max_money来记录最大
        dp列表用来记录每一家能获取的最大收益
        动态转移方程:dp[i] =  max(dp[i-2]+nums[i],dp[i-1])
        时间复杂度为O(n),空间复杂度也为O(n)
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(dp[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
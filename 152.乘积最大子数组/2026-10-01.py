class Solution:
    # 思路正确，但是时间复杂度太高，提交时超出时间限制
    # 改进思路：空间换时间
    def maxProduct(self, nums: list[int]) -> int:
        dp = [float('-inf')]*(len(nums))
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            product = 1
            for j in range(i,-1,-1):
                product *= nums[j]
                dp[i] = max(dp[i],product)
        return max(dp)

    # 改进1：增加一个维护列表，为了防止负数，因此还要维护最小乘积
    # 时间复杂度:O(n),空间复杂度:O(n)
    def maxProduct_1(self, nums: list[int]) -> int:
        dp_max = [float('-inf')]*(len(nums))
        dp_min = [float('inf')]*(len(nums))
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1,len(nums)):
            # 因为存在负数，所以要把三个数进行比较
            dp_max[i] = max(nums[i],dp_max[i-1]*nums[i],dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i],dp_min[i-1]*nums[i],dp_max[i-1]*nums[i])
        return max(dp_max)

    # 改进2：每个状态只与它的上一个状态相关，因此只用常量维护即可，进一步降低空间复杂度
    # 时间复杂度:O(n),空间复杂度:O(1)
    def maxProduct_2(self, nums: list[int]) -> int:
        dp_max = nums[0]
        dp_min = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            # 因为存在负数，所以要把三个数进行比较
            t_max = dp_max
            t_min = dp_min
            dp_max = max(nums[i],t_max*nums[i],t_min*nums[i])
            dp_min = min(nums[i],t_min*nums[i],t_max*nums[i])
            ans = max(ans,dp_max)
        return ans
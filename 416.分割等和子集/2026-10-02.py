from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # 奇数和不能被分割成等和
        if total % 2==1:
            return False
        # 目标应该是判断nums数组中是否能构成总和的一半
        target = total//2
        dp = [False]*(target+1)
        dp[0] = True
        # dp[j]表示：能否从已经遍历过的数字中选取若干个，使它们的和恰好为j
        for num in nums:
            # 逆序的原因：一个num只能使用一次，如果是正序可能会造成一个num使用两次的情况，比如：num=5，target=10，一开始dp[5]=True,遍历到dp[10]=True,可此时num=5使用了两次，不符合题目要求
            for j in range(target,num-1,-1):
                dp[j] = dp[j] or dp[j-num]
        return dp[-1]
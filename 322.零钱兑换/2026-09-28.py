class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        # 遍历1到amount所有数
        for i in range(1,amount+1):
            for coin in coins:
                if i >=coin:
                    # 动态转移方程
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return -1 if dp[-1]==float("inf") else dp[-1]
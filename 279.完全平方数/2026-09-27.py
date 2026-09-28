class Solution:
    def numSquares(self, n: int) -> int:
        # dp初始化为无穷大
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        # i从1开始遍历到n
        for i in range(1,n+1):
            # j遍历所有比i小的完全平方数
            for j in range(1,int(i**0.5)+1):
                # 更新出i这个位置的最小完全平方数和的个数
                dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[-1]
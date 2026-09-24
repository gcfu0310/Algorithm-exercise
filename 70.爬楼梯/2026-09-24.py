class Solution:
    def climbStairs(self, n: int) -> int:
        # 写出状态转移方程：dp[i] = dp[i-1]+dp[i-2]
        # 第i层楼梯的走法只能等于第i-1层楼梯的走法+第i-2层楼梯的走法，因为一次最多只能走一个台阶或是两个台阶
        p,q,r = 1,1,1
        for i in range(2,n+1):
            r = p+q
            p = q
            q = r
        return r
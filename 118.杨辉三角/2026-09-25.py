class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = []
        n = numRows
        for i in range(0,n):
            dp.append([1]*(i+1)) 
        if n<=2:
            return dp
        for i in range(2,n):
            for j in range(1,i):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp
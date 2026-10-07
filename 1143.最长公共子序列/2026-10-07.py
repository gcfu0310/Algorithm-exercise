class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        # dp[i][j]代表text1[:i]和text2[:j]的最长公共子序列长度
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1 if text1[0]==text2[0] else 0
        # 确定第一行和第一列
        for i in range(1,m):
            if text1[i]==text2[0]:
                dp[i][0]=1
            else:
                dp[i][0]=dp[i-1][0]
        for j in range(1,n):
            if text1[0]==text2[j]:
                dp[0][j]=1
            else:
                dp[0][j]=dp[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                # 第i和第j字符相同时
                if text1[i]==text2[j]:
                    # 当前的最长长度等于前1个的长度加一
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    # 不等时取两个字符串当前点前一个的较大的最大值
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
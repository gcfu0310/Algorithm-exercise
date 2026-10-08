class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        # dp[i][j]指的是word1[:i]与word2[:j]编辑相同的最小操作数
        dp=[[0]*(n+1) for _ in range(m+1)]
        # 当word2为空，需要的最小操作数(不断插入)
        for i in range(1,m+1):
            dp[i][0] = i
        # 当word1为空，需要的最小操作数(不断插入)
        for j in range(1,n+1):
            dp[0][j] = j
        # 遍历word1和word2
        for i in range(1,m+1):
            for j in range(1,n+1):
                # 当word[i-1]与word[j-1]相同时，当前dp[i][j]等于上一次相同时的dp[i-1][j-1]，不需要任何操作
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                # 不相等时，就应该是三种情况中最小次数再加上1次
                # dp[i][j-1]:向word1执行插入(等同于删除word2最后一个字符)；dp[i-1][j]:删除word1最后一个字符；dp[i-1][j-1]:替换word1字符
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        # return矩阵最后一个值，即为最小操作数
        return dp[-1][-1]
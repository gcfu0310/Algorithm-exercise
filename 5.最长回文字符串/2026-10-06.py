class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start,max_len=0,1
        dp=[[False]*n for _ in range(n)]
        for length in range(1,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if length==1:
                    dp[i][j]=True
                elif length==2:
                    dp[i][j]=(s[i]==s[j])
                else:
                    dp[i][j]=(s[i]==s[j]and dp[i+1][j-1])
                if dp[i][j] and j-i+1>max_len:
                    max_len=j-i+1
                    start=i
        return s[start:start+max_len]
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        dp=[0]*n
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=(dp[i-2] if i>=2 else 0 )+2
                elif s[i-1]==')':
                    j=i-dp[i-1]-1
                    if j>=0 and s[j]=='(':
                        dp[i]=(dp[j-1]if j>=1 else 0)+dp[i-1]+2
            
        return max(dp) if n!=0 else 0
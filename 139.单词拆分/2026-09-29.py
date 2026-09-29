from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i]代表s的前i个字符能否用wordDict里面的单词拆分出来
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for word in wordDict:
                # i应当大于这个word的长度且前i-len(word)个字符能被wordDict的单词拆分且当前len(word)长度的字符串要和单词相等
                if i>=len(word) and dp[i-len(word)]==True and s[i-len(word):i]==word:
                    dp[i] = True
        return dp[-1]
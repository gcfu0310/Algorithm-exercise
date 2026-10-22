class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,max_len=0,0
        n = len(s)
        substring = set()
        for right in range(n):
            while s[right] in substring:
                substring.remove(s[left])
                left+=1
            substring.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len

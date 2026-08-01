class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substring = set()
        n = len(s)
        max_length = 0
        for right in range(n):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            
            substring.add(s[right])
            max_length = max(right - left + 1,max_length)
        return max_length
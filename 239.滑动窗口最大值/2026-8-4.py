from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = list()
        queue = deque()
        i = 0
        n = len(nums)
        while i < n:
            if queue and queue[0] < i - k + 1:
                    queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                    queue.pop()
            queue.append(i)
            if i >= k-1:
                ans.append(nums[queue[0]])
            i += 1
        return ans

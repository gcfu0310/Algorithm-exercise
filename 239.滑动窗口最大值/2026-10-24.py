from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 存放长度为k的窗口中最大值的下标，最大值下标在队列最底部
        queue = deque()
        ans = list()
        # 指向窗口的右端
        right = 0
        n = len(nums)
        while right<n:
            # 判断当前队列的最大值下标有没有在当前窗口范围内，没在范围内需要移除
            if queue and queue[0]<=right-k:
                queue.popleft()
            # 将新窗口的值添加进队列中，原本队列中小于新值的就可以移除了，因为旧的值比新值先添加进队列，所以比新值更早离开队列且较小值无法再成为最大值了
            while queue and nums[queue[-1]]<nums[right]:
                queue.pop()
            # 将新值添加进队列
            queue.append(right)
            # 第一个窗口形成之后，将每个窗口的最大值添加进ans列表中
            if right>=k-1:
                ans.append(nums[queue[0]])
            right+=1
        return ans

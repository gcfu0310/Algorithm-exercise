from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # stack中存储还未在右边找到比当前温度高的下标
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx]=i-idx
            stack.append(i)
        return ans
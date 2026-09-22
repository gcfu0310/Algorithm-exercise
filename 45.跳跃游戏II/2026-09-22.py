from typing import List
class Solution:
    # 时间复杂度为O(n),空间复杂度为O(1)
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # 维护当前能到达的最远位置以及能到达的最远边界(end)
        maxPos, end, step = 0, 0, 0
        for i in range(n-1):
            # 更新能到达的最远位置
            maxPos = max(maxPos,i+nums[i])
            # 遍历到最远边界，说明此时需要再跳一次，此时跳完能到达的最远位置就是新的边界
            if i==end:
                end = maxPos
                step+=1
            # 当边界超过或是等于最后一个位置，说明此时已经到达，可以退出循环
            if end>=n-1:
                break
        return step
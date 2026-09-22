class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        # max_reach记录当前能到达的最远距离
        max_reach = 0
        for i in range(n):
            # 当前遍历到的位置已经超出了能到达的最远距离，直接返回False(无需考虑是否能到达最后一个位置)
            if i>max_reach:
                return False
            # 更新能到达的最远距离，取能到达的最远距离与当前能到距离的较大值
            max_reach = max(max_reach,i+nums[i])
            # 如果能到达的最远距离超过最后一个位置，直接返回True
            if max_reach>=n-1:
                return True
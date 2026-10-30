from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 哈希表方法 时间复杂度:O(n),空间复杂度:O(1)
        # 一个1*n的正数数组，它的最小正数范围在[1,n+1]
        # 利用哈希表的方法，数组下标相当于是key，我们把非正数赋值为n+1，如果key对应值存在，就把下标为key的值赋值成负数，代表该值存在
        n=len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i]=n+1
        for i in range(n):
            num=abs(nums[i])
            if num<=n:
                nums[num-1]=-abs(nums[num-1])
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1
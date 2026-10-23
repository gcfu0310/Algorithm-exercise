from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        前缀和的思想:记录以i与j结尾的前缀和total,当total[i]+k=total[j]时,就找到了和为k的子数组
        """
        hashmap = dict()
        total,count = 0,0
        n = len(nums)
        hashmap[total]=1
        for i in range(n):
            total+=nums[i]
            if total - k in hashmap:
                count+=hashmap[total-k]
            if total not in hashmap:
                hashmap[total]=0
            hashmap[total]+=1
        return count
            
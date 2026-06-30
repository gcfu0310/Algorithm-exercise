class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        count = 0
        while i < len(nums):
            sum = 0
            j = i + 1
            if nums[i] == k :
                count += 1
            while j < len(nums):
                sum = sum + nums[i] + nums[j]
                if sum == k:
                    count += 1
            i += 1
        return count
    

# 前缀和+哈希表
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = dict()
        count = 0
        total = 0
        hashmap[total] = 1
        for num in nums:
            total += num   
            if (total - k) in hashmap.keys():
                count += hashmap[total-k]
            if total not in hashmap.keys():
                hashmap[total] = 0
            hashmap[total] += 1
        return count

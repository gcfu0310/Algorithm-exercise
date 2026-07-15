class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        total = 0
        count = 0
        hashmap[total] = 1
        for num in nums:
            total += num
            if (total-k) in hashmap.keys():
                count += hashmap[total-k]
            if total not in hashmap.keys():
                hashmap[total] = 0
            hashmap[total] += 1
        return count
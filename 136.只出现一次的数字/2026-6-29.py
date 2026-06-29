class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = dict()
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                hashmap[num] += 1
            
            if hashmap[num] == 2:
                del hashmap[num]
        
        return list(hashmap.keys())[0]
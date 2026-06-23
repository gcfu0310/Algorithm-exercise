class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    j += 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i,j in enumerate(nums):
            need = target - j
            if need in hashmap:
                return [hashmap[need],i]
            else:
                hashmap[j] = i
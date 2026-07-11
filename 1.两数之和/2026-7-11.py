class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in dicts.keys():
                return [i,dicts[res]]
            else:
                dicts[nums[i]] = i
                    
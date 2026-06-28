class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] += 1
            if dic[num] > len(nums) / 2:
                return num
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        return(sort_nums[len(nums)//2])
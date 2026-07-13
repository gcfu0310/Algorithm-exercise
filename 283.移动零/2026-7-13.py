class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[non_zero],nums[cur] = nums[cur],nums[non_zero]
                non_zero += 1
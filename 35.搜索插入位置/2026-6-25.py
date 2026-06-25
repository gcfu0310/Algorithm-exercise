class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            k = (i+j) // 2 
            if target > nums[k]:
                i = k + 1
            if target <= nums[k]:
                j = k
        return j      
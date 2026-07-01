class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums = sorted(nums)
        out = []
        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            thrid = n - 1
            for second in range(first+1,n):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                while second < thrid and nums[first] + nums[second] + nums[thrid] > 0:
                    thrid -= 1
                if second == thrid:
                    break
                if nums[first] + nums[second] + nums[thrid] == 0:
                    out.append([nums[first],nums[second],nums[thrid]])

        return out
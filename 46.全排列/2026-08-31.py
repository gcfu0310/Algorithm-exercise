from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = dict()
        for num in nums:
            used[num] = False
        ans = list()
        path = list()
        def backtrack():
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            
            for num in nums:
                if used[num]:
                    continue
                used[num] = True
                path.append(num)

                backtrack()

                path.pop()
                used[num] = False
        backtrack()
        return ans
                
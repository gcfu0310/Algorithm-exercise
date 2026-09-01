from typing import List
class Solution:
    # 时间复杂度是O(n2^n),空间复杂度是O(n)
    # 回溯方法，每次都只选择start之后的数构成子集，防止出现重复
    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        path = list()

        # 每次都只选择start之后(包括start)的数构成子集
        def backtrack(start:int): 
            for i in range(start,len(nums)):
                path.append(nums[i])
                ans.append(path.copy())

                backtrack(i+1)

                path.pop()
        
        backtrack(0)
        return ans

    # 时间复杂度:O(n2^n),空间复杂度O(1)
    # BFS方法，每次都把新的数和数组中已有的数进行拼接
    def subset_2(self,nums:List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            for j in range(len(ans)):
                ans.append(ans[j]+[nums[i]])
        return ans
from typing import List
class Solution:
    # 与接雨水一致的方法
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        ans = list()
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i-1] = right[n-i] * nums[n-i]
        for i in range(n):
            ans.append(left[i]*right[i])
        return ans

    # 输出不算在空间复杂度中，所以直接用ans数组存放左乘积，然后右乘积就进一步跟着在ans上做更新就行
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        right = 1
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(1,n):
            right *= nums[n-i]
            ans[n-i-1] = right * ans[n-i-1]
        return ans
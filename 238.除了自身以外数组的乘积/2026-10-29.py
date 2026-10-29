from typing import List
class Solution:
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        # 计算每个节点的前缀积和后缀积，二者相乘就是除该节点外所有数的乘积
        # 时间复杂度:O(n),空间复杂度:O(n)
        ans=list()
        n=len(nums)
        pre,suffix=[1]*n,[1]*n
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i-1]
            suffix[n-i-1]=suffix[n-i]*nums[n-i]
        for j in range(n):
            ans.append(pre[j]*suffix[j])
        return ans
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        # 输出数组不计算在空间复杂度内，所以先走一遍循环，计算数组的前缀积，再循环一次把后缀积乘上就完成了
        # 时间复杂度为O(n),空间复杂度为O(1)
        n=len(nums)
        ans=[1]*n
        right=1
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i]
        for j in range(1,n+1):
            ans[n-j]*=right
            right*=nums[n-j]
        return ans    
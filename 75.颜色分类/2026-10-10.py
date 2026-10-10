from typing import list
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # p0指向下一个0应该放置的位置
        # p1指向下一个1应该放置的位置
        p0,p1=0,0
        for i in range(n):
            if nums[i]==1:
                nums[p1],nums[i]=nums[i],nums[p1]
                p1+=1
            elif nums[i]==0:
                nums[p0],nums[i]=nums[i],nums[p0]
                # 若p0 < p1，说明p0处原本是1
                # 第一次交换会把这个1放到i处
                # 因此需要再次交换，将1放到p1位置
                if p0<p1:
                    nums[p1],nums[i] = nums[i],nums[p1]
                # 0区域扩大，同时1区域的右边界向后移动
                p0+=1
                p1+=1

    def sortColors_2(self, nums: list[int]) -> None:
        n = len(nums)
        p0,p2=0,n-1
        i=0
        while i<=p2:
            # 使用while的原因：p2原位置的数也可能是2，需要把换到前面的2，换到后面去
            while i<=p2 and nums[i]==2:
                nums[p2],nums[i] = nums[i],nums[p2]
                p2-=1
            if nums[i]==0:
                nums[p0],nums[i] = nums[i],nums[p0]
                p0+=1
            i+=1
import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left,right):
            lt,gt = left,right
            i = left
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            while i<=gt:
                if nums[i]<pivot:
                    nums[lt],nums[i] = nums[i],nums[lt]
                    i+=1
                    lt+=1
                elif nums[i]==pivot:
                    i+=1
                else:
                    nums[gt],nums[i] = nums[i],nums[gt]
                    gt-=1
            return lt,gt,pivot
        target = len(nums)-k
        left,right = 0,len(nums)-1
        while True:
            lt,gt,pivot = partition(left,right)
            if lt<=target<=gt:
                return pivot
            elif lt > target:
                right = lt-1
            else:
                left = gt+1
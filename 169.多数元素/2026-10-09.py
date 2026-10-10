# 投票方法 时间复杂度为O(n),空间复杂度为O(1)
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            if count==0:
                candidate=num
            if num != candidate:
                count-=1
            else:
                count+=1
        return candidate
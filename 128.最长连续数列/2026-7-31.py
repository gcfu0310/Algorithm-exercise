from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            cur_length = 0
            # 确保待遍历数前面没有数
            if num - 1 not in nums_set:
                cur_num = num
                cur_length = 1

                while cur_num + 1 in nums_set:
                    cur_num += 1
                    cur_length += 1
            
            max_length = max(max_length,cur_length)
        
        return max_length
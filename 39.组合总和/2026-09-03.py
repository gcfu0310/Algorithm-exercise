from typing import List

class Solution:
    # 时间复杂度O(S),所有可行解的长度之和；空间复杂度O(target),主要来自递归使用的空间栈
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = list()
        ans = list()
        def backtrack(start,remain):
            if remain == 0:
                ans.append(path.copy())
                return 
            # candidates全是正数>=2,当remain小于0时，说明此时path的和已经超过了target
            if remain < 0:
                return 
            # start标记遍历起点，防止出现[2,2,3]与[3,2,2]这种重复的情况
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                remain-=candidates[i]

                backtrack(i,remain)

                remain+=candidates[i] # 回溯之后，remain需要加回即将被pop出去的数，remain还原成这个数path加入之前
                path.pop()
        backtrack(0,target)
        return ans
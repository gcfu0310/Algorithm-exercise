from typing import List

# 超级大笨蛋方法
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            def merged(a:List[int],b:List[int]) -> List[List[int]]:
                t = []
                if b[0] <= a[1] <=b[1]:
                    t.append([a[0],b[1]])
                elif a[1] > b[1]:
                    t.append(a)
                else:
                    t.extend([a,b])
                return t
            
            intervals.sort(key=lambda x:x[0])
            n = len(intervals[:])
            if n == 1:
                return intervals
            sub = intervals[0]
            i = 1
            ans = list()
            while i < n:
                sub_i = intervals[i]
                k = merged(sub,sub_i)
                i += 1
                while len(k[:]) == 1 and i < n:
                    sub_i = intervals[i]
                    sub = k[0]
                    k = merged(sub,sub_i)
                    i += 1
                if k[0] not in ans and i != n:
                    ans.append(k[0])
                elif i == n:
                    ans.extend(k[:])
                sub = sub_i
                
            return ans

# 优化之后的
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 大列表按着每个小列表的首项进行升序排序
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)

        #current记录当前合并完成的区间 
        current = intervals[0]
        i = 1
        # 存放最终答案
        ans = list()
        # 开始遍历
        while i < n:
            # next_interval记录待合并区间
            next_interval = intervals[i]
            # 当合并已完成区间的右边界大于待合并区间的左边界即可合并，反之不能合并
            if current[1] >= next_interval[0]:
                # 更新已完成合并区间的右边界
                current[1] = max(current[1],next_interval[1])
            else:
                # 不能合并了，说明当前合并已完成区间不能再与后续区间进行合并了，将结果添加进最终答案列表
                ans.append(current)
                # 更新合并已完成区间，更新为待合并区间
                current = next_interval
            i += 1
        # 把最后一个已完成合并区间添加进最终答案列表
        ans.append(current)
        return ans

# 继续优化
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        current = intervals[0]
        ans = list()
        for i in range(1,n):
            next_interval = intervals[i]
            if current[1] >= next_interval[0]:
                current[1] = max(current[1],next_interval[1])
            else:
                ans.append(current)
                current = next_interval
        ans.append(current)
        return ans
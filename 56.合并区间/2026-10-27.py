class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # 先把所有区间按照区间的start进行升序排序
        intervals.sort()
        n=len(intervals)
        # current是当前区间
        current=intervals[0]
        ans=list()
        for i in range(1,n):
            # next_interval是待合并的区间
            next_interval=intervals[i]
            # 若当前区间的end>待合并区间的start，说明此时可以合并
            if current[1]>=next_interval[0]:
                # 更新新区间的end，end应该是current的end与next_interval的end的最大值
                current[1]=max(current[1],next_interval[1])
            else:
                # 若无法合并，把当前区间添加进ans中
                ans.append(current)
                # 当前区间更新成待合并区间
                current=next_interval
        # 循环结束，current区间还没有添加进ans中，补充一个添加语句
        ans.append(current)
        return ans
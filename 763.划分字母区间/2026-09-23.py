class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = dict()
        ans = list()
        n = len(s)
        # 记录每个字符最后一次出现的位置
        for i,ch in enumerate(s):
            last[ch] = i
        start,end = 0,0
        for i in range(n):
            ch = s[i]
            # 实时更新当前片段的end
            end = max(end,last[ch])
            # 当遍历到当前片段的end，就可以开始切分了
            if i==end:
                ans.append(end-start+1)
                start = i+1
                continue
        return ans



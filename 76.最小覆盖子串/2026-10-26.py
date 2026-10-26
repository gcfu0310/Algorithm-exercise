from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        needs=defaultdict(int)
        windows=defaultdict(int)
        left,right=0,0
        valid = 0
        n = len(s)
        start,min_len=n+1,n+1

        # 确定t中所需的字符种类以及数量
        for c in t:
            needs[c]+=1
        # 遍历s字符串
        while right < n:
            c=s[right]
            # 当前字符是所需时，在Windows中添加
            if c in needs:
                windows[c]+=1
                # 当字符数量相同时，valid+=1
                if windows[c]==needs[c]:
                    valid+=1
            # 当valid==len(needs)说明此时窗口内包含了字符串t
            while valid==len(needs):
                # 更新当前最短窗口子串
                if min_len > right-left+1:
                    start=left
                    min_len=right-left+1
                # 开始缩减左边界
                # 两种情况：1、left是needs中的字符；2、left不是needs的字符(这种直接left+=1即可)
                # 情况1又分为两种情况：1)此时Windows中left的数量和needs中的数量相等(这种情况valid-1，跳出循环);2)windows中left的数量大于needs中数量(这种直接把Windows中对应的left字符数量减一即可)
                if s[left] in needs:
                    if windows[s[left]]==needs[s[left]]:
                        valid-=1
                    windows[s[left]]-=1
                left+=1
            right+=1
        return s[start:start+min_len]
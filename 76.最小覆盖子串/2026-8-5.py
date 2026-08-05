from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 当t字符串长度大于s字符串长度直接返回空值
        if len(t) > len(s):
            return ""
        
        # 初始化一些变量
        m,n = len(s),len(t)
        # 当没有找到子串时，默认就是s的长度，不会有子串的长度会大于字符串本身
        start,min_len = m + 1,m+1
        # 当valid和字符串t中的字符种类相等时，说明窗口满足条件
        valid = 0
        # 定义左右指针
        left,right = 0,0

        # 统计t字符串每个字符的出现次数
        needs = defaultdict(int)
        # 统计当前窗口中待寻找字符的出现次数
        windows = defaultdict(int)
        for char in t:
            needs[char] += 1
        
        # 开始遍历
        while right < m:
            # 加入一个右指针对应字符
            c = s[right]

            # 当前字符是待寻找字符
            if c in needs:
                # 窗口记录+1
                windows[c] += 1
                # 当这个字符数量已经和t字符串中的数量一致时
                if windows[c] == needs[c]:
                    valid += 1

            # 判断当前窗口满足条件
            while valid == len(needs):
                # 记录当前窗口长度，并更新最短长度和start指针
                length = right - left + 1
                if length < min_len:
                    start = left
                    min_len = length

                # 通过左指针右移，缩短窗口长度
                # 当左指针所指的数恰好是待查找字符时，分两种情况
                if s[left] in needs:
                    # 情况1：此时窗口内该字符的数量和t中该字符数量相等时，此时需要valid-=1，因为移除之后，窗口就不满足条件了
                    # 情况2：移除之后，窗口中仍然满足条件
                    if needs[s[left]] == windows[s[left]]:
                        valid -= 1
                    # 更新窗口内字符数量
                    windows[s[left]] -= 1
                # 左指针右移
                left += 1
            
            # 右指针不断右移
            right += 1
        
        # 通过start指针以及记录的最短长度，返回最小覆盖子串
        return s[start:start+min_len]
                

        
        
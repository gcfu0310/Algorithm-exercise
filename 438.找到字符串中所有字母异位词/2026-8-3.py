from typing import List

# 笨蛋方法
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexs = list()
        p = sorted(p)
        n = len(p)
        N = len(s)
        i = 0
        while i + n <= N:
            sub = sorted(s[i:i+n])
            if sub == p:
                indexs.append(i)
            i += 1
        return indexs

# 空间换时间的滑动窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexs = list()
        s_len,p_len = len(s),len(p)

        if s_len < p_len:
            return indexs

        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        if s_count == p_count:
            indexs.append(0)
        for i in range(s_len-p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i+p_len]) - 97] += 1

            if s_count == p_count:
                indexs.append(i+1)

        return indexs

# 优化对比条件的滑动窗口,添加diff来统计与p字符串数量不同字符的个数
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def update(idx,delta):
            nonlocal diff
            if s_count[idx] == p_count[idx]:
                diff += 1
            s_count[idx] += delta
            if s_count[idx] == p_count[idx]:
                diff -= 1

        indexs = list()
        s_len,p_len = len(s),len(p)
        diff = 0

        if s_len < p_len:
            return []

        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        for i in range(26):
            if s_count[i] != p_count[i]:
                diff += 1

        if diff == 0:
            indexs.append(0)

        for i in range(s_len-p_len):
            update(ord(s[i])-97,-1)
            update(ord(s[i+p_len])-97,1)
            if diff == 0:
                indexs.append(i+1)

        return indexs

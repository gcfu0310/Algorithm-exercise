from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = [0]*26
        p_len = len(p)
        s_len = len(s)
        ans = []
        if s_len<p_len:
            return []
        # s中前p_len是否是异位词
        for i in range(p_len):
            count[ord(p[i])-97]-=1
            count[ord(s[i])-97]+=1
        diff = [c!=0 for c in count].count(True)
        if diff==0:
            ans.append(0)
        for i in range(s_len-p_len):
            # 删除滑动窗的首，当首对应count值为1，diff-1，当首对应count值为0，diff+1
            if count[ord(s[i])-97] == 1:
                diff-=1
            elif count[ord(s[i])-97] == 0:
                diff+=1
            count[ord(s[i])-97]-=1

            # 向滑动窗口尾部添加元素，当尾对应的count值为-1，diff-1，当尾对应的count值为0，diff+1
            if count[ord(s[i+p_len])-97] == -1:
                diff-=1
            elif count[ord(s[i+p_len])-97] == 0:
                diff+=1
            count[ord(s[i+p_len])-97]+=1
            # 对应的首为i+1
            if diff == 0:
                ans.append(i+1)
        return ans
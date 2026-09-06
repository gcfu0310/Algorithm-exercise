from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 标记从哪里开始切
        def backtrack(start):
            # 当起始点等于s的长度时，代表整个字符串已经被切完了
            if start == len(s):
                ans.append(path.copy())
                return 
            # 遍历每个字符串的结尾，范围应该是起点+1到字符串末尾
            for end in range(start+1,len(s)+1):
                current = s[start:end]
                # 如果当前截取的字符串是回文字符串，就在path中添加
                if current == current[::-1]:
                    path.append(current)

                    # 现在的end就是下一次切割的起始点
                    backtrack(end)
                    # 撤销
                    path.pop()
        
        ans = []
        path = []
        backtrack(0)
        return ans
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start):
            if start == len(s):
                ans.append(path.copy())
                return 
            for end in range(start+1,len(s)+1):
                current = s[start:end]
                if current == current[::-1]:
                    path.append(current)
                
                    backtrack(end)
                    path.pop()
        
        ans = []
        path = []
        backtrack(0)
        return ans